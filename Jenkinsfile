pipeline {
    agent any

    environment {
        // Set OTX_API_KEY here or use Jenkins Credentials to inject it securely
        OTX_API_KEY = credentials('your-otx-api-key-id')
    }

    stages {
        stage('Static Analysis') {
            steps {
                script {
                    // Install bandit and run bandit_script.py
                    sh 'pip3 install bandit --user'
                    sh 'python3 bandit_script.py'
                }
            }
        }

        stage('Dependency Scanning') {
            steps {
                script {
                    // Install safety and run safety_script.py
                    sh 'pip3 install safety --user'
                    sh 'export PATH=$PATH:$HOME/.local/bin && python3 safety_script.py'
                }
            }
        }

        stage('Dynamic Analysis') {
            steps {
                script {
                    // Run OWASP ZAP dynamic analysis
                    sh 'python3 zap_script.py'
                }
            }
        }

        stage('Fetch Threat Intelligence') {
            steps {
                script {
                    // Run OTX script to fetch threat intelligence
                    sh 'python3 otx_script.py'
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/*', allowEmptyArchive: true
        }
    }
}
