#include <stdio.h>

// 模拟LED状态
int led_status = 0;

// 模拟传感器读取
int read_temperature() {
    return 25; // 25摄氏度
}

int read_humidity() {
    return 40; // 40%
}

void toggle_led() {
    led_status = !led_status;
    printf("LED is now %s\n", led_status ? "ON" : "OFF");
}

int main(void) {
    printf("固件启动...\n");
    
    // 模拟固件主循环
    for (int i = 0; i < 5; i++) {
        toggle_led();
        printf("读取传感器：温度 %d°C，湿度 %d%%\n", read_temperature(), read_humidity());
        printf("上传数据中...\n");
    }

    printf("固件运行结束。\n");
    return 0;
}
//tejhsadkha
// Jenkins 自动触发测试：2025年8月7日