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

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip3 install --user -r test_web/requirements.txt'
                }
            }
        }

        stage('Static Analysis') {
            steps {
                script {
                    sh 'pip3 install --user bandit'
                    sh 'export PATH=$PATH:$HOME/.local/bin && python3 bandit_script.py'
                }
            }
        }

        stage('Dependency Scanning') {
            steps {
                script {
                    sh 'pip3 install --user safety'
                    sh 'export PATH=$PATH:$HOME/.local/bin && python3 safety_script.py'
                }
            }
        }

        stage('Dynamic Analysis') {
            steps {
                script {
                    sh 'export PATH=$PATH:$HOME/.local/bin && python3 zap_script.py'
                }
            }
        }

        stage('Fetch Threat Intelligence') {
            steps {
                script {
                    sh 'export PATH=$PATH:$HOME/.local/bin && python3 otx_script.py $OTX_API_KEY'
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
