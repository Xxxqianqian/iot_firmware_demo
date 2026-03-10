pipeline {
    // 1. 指定任何可用的 Jenkins Agent
    agent any

    // 2. 定义全局环境变量（可选，如果在构建时需要）
    environment {
        PATH = "C:\\Windows\\System32;${env.PATH}"
    }

    stages {
        stage('Build Firmware') {
            steps {
                echo '=== 开始构建固件 ==='
                // 直接调用项目根目录下的 build.bat
                bat 'build.bat'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo '=== 开始执行单元测试 ==='
                // 推荐优先使用 run_tests.bat 以保证 Windows 环境兼容性
                // 如果你确实需要 make，请确认系统已配置环境变量
                bat 'run_tests.bat'
            }
        }

        stage('Archive Results') {
            steps {
                echo '=== 归档构建产物 ==='
                // 将编译出的二进制文件存档，方便后期下载
                archiveArtifacts artifacts: 'firmware.bin', fingerprint: true
            }
        }
    }

    // 3. 构建后处理逻辑
    post {
        success {
            echo '流水线执行成功！'
        }
        failure {
            echo '流水线执行失败，请检查控制台日志。'
        }
    }
}