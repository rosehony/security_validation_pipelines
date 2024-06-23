pipeline {
    agent any
    environment {
        OTX_API_KEY = credentials('otx-api-key')
    }
    stages {
        stage('Static Analysis') {
            steps {
                script {
                    sh 'pip3 install bandit --user'
                    sh 'python3 bandit_script.py'
                }
            }
        }
        stage('Dependency Scanning') {
            steps {
                script {
                    sh 'pip3 install safety --user'
                    sh 'python3 safety_script.py'
                }
            }
        }
        stage('Dynamic Analysis') {
            steps {
                script {
                    sh 'docker run -d -u zap -p 8080:8080 --name zap ghcr.io/zaproxy/zaproxy:stable zap.sh -daemon -port 8080'
                    sh 'python3 zap_script.py'
                    sh 'docker stop zap'
                    sh 'docker rm zap'
                }
            }
        }
        stage('Fetch Threat Intelligence') {
            steps {
                script {
                    sh 'pip3 install OTXv2 --user'
                    withCredentials([string(credentialsId: 'otx-api-key', variable: 'OTX_API_KEY')]) {
                        sh 'python3 otx_script.py $OTX_API_KEY'
                    }
                }
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '*.txt, *.html', allowEmptyArchive: true
        }
    }
}
