pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'build.bat'
            }
        }
        stage('Test') {
            steps {
                bat 'make test'
            }
        }
    }
    post {
        success {
            archiveArtifacts artifacts: 'firmware.bin', fingerprint: true
        }
    }
}