pipeline {
    agent any
    environment {
        // 强制指定路径，确保 Jenkins 能找到安装的 GCC 和 Make
        PATH = "C:\\msys64\\ucrt64\\bin;C:\\msys64\\usr\\bin;${env.PATH}"
    }
    stages {
        stage('Build Firmware') {
            steps {
                bat 'call build.bat'
            }
        }
        stage('Run Unit Tests') {
            steps {
                // 假设你的测试程序是 unit_test.elf
                bat 'unit_test.elf'
            }
        }
    }
}