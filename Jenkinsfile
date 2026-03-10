pipeline {
    agent any

    options {
        // options 块里只能放标准的流水线选项，移除了 ansiColor
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Clone Code') {
            steps {
                echo 'Cloning code from GitHub...'
                // 如果使用 Pipeline SCM，这一步其实是冗余的，但保留也没问题
                git branch: 'main', url: 'https://github.com/Xxxqianqian/iot_firmware_demo.git'
            }
        }

        stage('Build Firmware') {
            steps {
                // 使用 wrap 包装器来开启 ANSI 颜色支持
                wrap([$class: 'AnsiColorBuildWrapper', 'colorMapName': 'xterm']) {
                    echo 'Building firmware...'
                    bat 'build.bat'
                }
            }
        }

        stage('Run Tests') {
            steps {
                wrap([$class: 'AnsiColorBuildWrapper', 'colorMapName': 'xterm']) {
                    echo 'Running tests...'
                    bat 'make test'
                }
            }
        }

        stage('Archive Firmware') {
            steps {
                echo 'Saving firmware artifact...'
                archiveArtifacts artifacts: 'firmware.bin', fingerprint: true
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
