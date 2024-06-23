pipeline {
    agent any

    environment {
        OTX_API_KEY = credentials('otx-api-key')
    }

    stages {
        stage('Checkout Security Validation Pipelines') {
            steps {
                git url: 'https://github.com/rosehony/security_validation_pipelines.git', branch: 'main'
            }
        }

        stage('Checkout Test Web Project') {
            steps {
                dir('test_web') {
                    git url: 'https://github.com/rosehony/test_web.git', branch: 'main'
                }
            }
        }

        stage('Static Analysis') {
            steps {
                script {
                    // Install Bandit and run bandit_script.py
                    sh 'pip3 install --user bandit'
                    sh 'python3 bandit_script.py'
                }
            }
        }

        stage('Dependency Scanning') {
            steps {
                script {
                    // Install Safety and run safety_script.py
                    sh 'pip3 install --user safety'
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
