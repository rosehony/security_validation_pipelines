pipeline {
    agent any
    environment {
        OTX_API_KEY = credentials('otx-api-key')
    }
    stages {
        stage('Static Analysis') {
            steps {
                script {
                    sh 'python3 bandit_script.py'
                }
            }
        }
        stage('Dependency Scanning') {
            steps {
                script {
                    sh 'python3 safety_script.py'
                }
            }
        }
        stage('Dynamic Analysis') {
            steps {
                script {
                    sh 'python3 zap_script.py'
                }
            }
        }
        stage('Fetch Threat Intelligence') {
            steps {
                script {
                    sh 'python3 otx_script.py ${OTX_API_KEY}'
                }
            }
        }
    }
}
