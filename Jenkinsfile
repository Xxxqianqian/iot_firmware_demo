pipeline {
    agent any
    environment {
        PATH = "C:\\msys64\\ucrt64\\bin;C:\\msys64\\usr\\bin;${env.PATH}"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', 
                    branches: [[name: '*/main']], 
                    userRemoteConfigs: [[
                        url: 'git@github.com:Xxxqianqian/iot_firmware_demo.git', 
                        credentialsId: 'github-token'
                    ]]
                ])
            }
        }
        stage('Build Firmware') {
            steps {
                bat 'make clean'
                bat 'make'
            }
        }
        stage('Run Unit Tests') {
            steps {
                bat 'unit_test.elf'
            }
        }
    }
}