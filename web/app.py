import requests
import time
import os
from requests.auth import HTTPBasicAuth
from flask import Flask, render_template, Response, jsonify
from flask_cors import CORS
from waitress import serve

app = Flask(__name__)
CORS(app)

# ===== Jenkins 配置 =====
JENKINS_URL = "http://localhost:8080"
JOB_NAME = "ovo"
USERNAME = "admin2"
API_TOKEN = "11369cb034458008d79dba35d2083f1630"
TRIGGER_TOKEN = "mytoken123"

def get_jenkins_data(fetch_real_data=False):
    """获取 Jenkins 制品和日志"""
    if not fetch_real_data:
        return {"name": "待构建", "size": 0, "url": None}, "点击构建按钮开始流水线测试。"

    try:
        api_url = f"{JENKINS_URL}/job/{JOB_NAME}/lastSuccessfulBuild/api/json?t={int(time.time())}"
        r = requests.get(api_url, auth=HTTPBasicAuth(USERNAME, API_TOKEN), timeout=5)
        r.raise_for_status()
        data = r.json()

        firmware_info = {"name": "未发现固件", "size": 0, "url": None}
        logs = "构建成功，但未找到相关的测试日志。"
        build_num = data.get("number")
        base_artifact_url = f"{JENKINS_URL}/job/{JOB_NAME}/{build_num}/artifact/"

        for art in data.get("artifacts", []):
            file_name = art['fileName']
            # 识别固件
            if file_name.endswith(".bin") or file_name.endswith(".hex") or "firmware" in file_name:
                firmware_info['name'] = file_name
                file_url = base_artifact_url + art['relativePath']
                firmware_info['url'] = file_url
                head = requests.head(file_url, auth=HTTPBasicAuth(USERNAME, API_TOKEN), timeout=5)
                firmware_info['size'] = int(head.headers.get('Content-Length', 0))
            # 识别日志
            elif "test_log" in file_name.lower() or file_name.endswith(".txt"):
                log_url = base_artifact_url + art['relativePath']
                log_r = requests.get(log_url, auth=HTTPBasicAuth(USERNAME, API_TOKEN), timeout=5)
                log_r.encoding = 'utf-8'
                logs = log_r.text
        
        return firmware_info, logs
    except Exception as e:
        return {"name": "获取失败", "size": 0, "url": None}, f"API 连接异常: {e}"

# --- 新增：构建历史接口 ---
@app.route('/history')
def get_history():
    """获取最近 5 次构建记录"""
    try:
        # tree 参数只抓取需要的字段，减轻服务器压力
        api_url = f"{JENKINS_URL}/job/{JOB_NAME}/api/json?tree=builds[number,result,timestamp]"
        r = requests.get(api_url, auth=HTTPBasicAuth(USERNAME, API_TOKEN), timeout=5)
        builds = r.json().get("builds", [])[:5]  # 只展示前 5 条
        
        history = []
        for b in builds:
            # 转换 Jenkins 的毫秒时间戳为可读格式
            formatted_time = time.strftime("%H:%M:%S", time.localtime(b.get("timestamp")/1000))
            history.append({
                "number": b.get("number"),
                "result": b.get("result") or "BUILDING", # 如果正在跑，result 是 None
                "time": formatted_time
            })
        return jsonify(history)
    except Exception as e:
        print(f"History API Error: {e}")
        return jsonify([])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_latest')
def get_latest():
    firmware, logs = get_jenkins_data(fetch_real_data=True)
    return jsonify({"firmware": firmware, "logs": logs})

@app.route('/run')
def run_firmware():
    firmware, _ = get_jenkins_data(fetch_real_data=True)
    if firmware['size'] == 0:
        return ">>> [ERROR] 尚未检测到有效固件！"
    
    return (f">>> [BOOT] 载入镜像: {firmware['name']}\n"
            f">>> [INFO] 镜像大小: {firmware['size']} Bytes\n"
            f">>> [HAL] 仿真硬件初始化...\n"
            f">>> [SUCCESS] 虚拟 IoT 设备运行正常。")

@app.route('/build', methods=['POST'])
def build_firmware():
    trigger_url = f"{JENKINS_URL}/job/{JOB_NAME}/build?token={TRIGGER_TOKEN}"
    try:
        requests.post(trigger_url, auth=HTTPBasicAuth(USERNAME, API_TOKEN), timeout=5)
        info_r = requests.get(f"{JENKINS_URL}/job/{JOB_NAME}/api/json", auth=HTTPBasicAuth(USERNAME, API_TOKEN))
        return jsonify({"next_build_number": info_r.json().get("nextBuildNumber")})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/status/<int:build_number>')
def get_status(build_number):
    try:
        r = requests.get(f"{JENKINS_URL}/job/{JOB_NAME}/{build_number}/api/json", auth=HTTPBasicAuth(USERNAME, API_TOKEN), timeout=5)
        if r.status_code == 404: 
            return jsonify({"building": True, "result": None})
        data = r.json()
        return jsonify({"building": data.get("building", False), "result": data.get("result")})
    except: 
        return jsonify({"building": True, "result": None})

@app.route('/download')
def download_firmware():
    firmware, _ = get_jenkins_data(fetch_real_data=True)
    if firmware['url']:
        r = requests.get(firmware['url'], auth=HTTPBasicAuth(USERNAME, API_TOKEN), stream=True)
        return Response(r.iter_content(chunk_size=1024), 
                        content_type='application/octet-stream', 
                        headers={"Content-Disposition": f"attachment; filename={firmware['name']}"})
    return "文件未找到", 404

if __name__ == '__main__':
    print(">>> 毕设后端已启动：http://127.0.0.1:5000")
    serve(app, host='0.0.0.0', port=5000)