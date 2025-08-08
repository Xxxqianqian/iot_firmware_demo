pipeline {
    agent any

    options {
        ansiColor('xterm')
        timestamps()
    }

    stages {
        stage('Clone Code') {
            steps {
                echo 'Cloning code from GitHub...'
                git branch: 'main', credentialsId: 'Xxxqianqian', url: 'https://github.com/Xxxqianqian/iot_firmware_demo.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Starting build process...'
                bat 'build.bat'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running JUnit tests...'
                bat 'run_tests.bat'  // 你可以自己写一个 run_tests.bat 执行测试
            }
        }

        stage('Archive Firmware') {
            steps {
                echo 'Archiving firmware binary...'
                archiveArtifacts artifacts: 'bin/firmware.bin', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Build and tests completed successfully.'
        }
        failure {
            echo 'Build or tests failed. Check logs.'
        }
        always {
            echo "Build finished at: ${new Date()}"
        }
    }
}
