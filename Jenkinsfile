pipeline {
    agent any
    environment {
        OTX_API_KEY = credentials('otx-api-key')
    }
    stages {
        stage('Static Analysis') {
            steps {
                script {
                    // Run Bandit for static analysis
                    sh 'python3 bandit_script.py'
                }
            }
        }
        stage('Dependency Scanning') {
            steps {
                script {
                    // Run Safety for dependency scanning
                    sh 'python3 safety_script.py'
                }
            }
        }
        stage('Dynamic Analysis') {
            steps {
                script {
                    // Run ZAP for dynamic analysis
                    sh '''
                    docker run -u zap -d -p 8080:8080 ghcr.io/zaproxy/zaproxy:stable zap.sh -daemon -port 8080 -config api.disablekey=true
                    sleep 30  # Give ZAP some time to start
                    python3 zap_script.py
                    '''
                }
            }
        }
        stage('Fetch Threat Intelligence') {
            steps {
                script {
                    // Fetch Threat Intelligence from OTX
                    sh 'python3 otx_script.py ${OTX_API_KEY}'
                }
            }
        }
    }
    post {
        always {
            // Archive the ZAP report
            archiveArtifacts artifacts: 'zap_report.html', allowEmptyArchive: true
        }
    }
}
