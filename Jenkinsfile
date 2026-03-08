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
                git branch: 'main', url: 'https://github.com/Xxxqianqian/iot_firmware_demo.git'
            }
        }

        stage('Build Firmware') {
            steps {
                echo 'Building firmware...'
                bat 'build.bat'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                bat 'make test'
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
