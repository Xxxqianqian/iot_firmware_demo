pipeline {
    agent any

    stages {
        stage('Build Firmware') {
            steps {
                echo 'Building firmware...'
                // 直接执行 bat，去掉 wrap 包装
                bat 'build.bat'
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                bat 'make test'
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: 'firmware.bin', fingerprint: true
            echo 'Build and tests completed successfully.'
        }
        failure {
            echo 'Build failed. Please check the logs.'
        }
    }
}
