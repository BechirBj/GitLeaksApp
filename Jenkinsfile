pipeline {
    agent any

    environment {
        IMAGE_NAME = 'devsecops-lab'
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

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
                        gitleaks detect \
                            --config .gitleaks.toml \
                            --no-banner \
                            -v
                    '''
                }
            }
        }

        stage('SAST - Bandit') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    sh '''
                        .venv/bin/bandit \
                            -r . \
                            -x ./.venv
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

        stage('Trivy - Filesystem Scan') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    sh '''
                        trivy fs \
                            --scanners vuln,misconfig,secret \
                            --severity HIGH,CRITICAL \
                            --exit-code 1 \
                            --no-progress \
                            .
                    '''
                }
            }
        }

        stage('Tests') {
            steps {
                sh '''
                    echo "Running application tests..."
                    echo "Add pytest or other tests here."
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build \
                        -t ${IMAGE_NAME}:${IMAGE_TAG} \
                        .
                '''
            }
        }

        stage('Trivy - Container Scan') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    sh '''
                        trivy image \
                            --severity HIGH,CRITICAL \
                            --exit-code 1 \
                            --no-progress \
                            ${IMAGE_NAME}:${IMAGE_TAG}
                    '''
                }
            }
        }
    }

    post {
        always {
            echo "Security pipeline completed."
        }

        success {
            echo "All pipeline stages passed."
        }

        failure {
            echo "One or more security checks failed."
        }
    }
}
