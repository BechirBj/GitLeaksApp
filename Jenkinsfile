pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/pip install -r requirements.txt
                    .venv/bin/pip install bandit pip-audit
                '''
            }
        }

        stage('Secret Scanning - Gitleaks') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    sh '''
                        gitleaks detect                             --config .gitleaks.toml                             --no-banner                             -v
                    '''
                }
            }
        }

        stage('SAST - Bandit') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    sh '''
                        .venv/bin/bandit app.py
                    '''
                }
            }
        }

        stage('SCA - Dependency Scan') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    sh '''
                        .venv/bin/pip-audit
                    '''
                }
            }
        }

        stage('Tests') {
            steps {
                sh '''
                    echo Run application tests here
                '''
            }
        }
    }
}

