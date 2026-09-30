pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/pip install bandit
                '''
            }
        }

        stage('Secret Scanning - Gitleaks') {
            steps {
                sh '''
                    gitleaks detect                         --config .gitleaks.toml                         --no-banner                         -v
                '''
            }
        }

        stage('SAST - Bandit') {
            steps {
                sh '''
                    .venv/bin/bandit app.py
                '''
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

