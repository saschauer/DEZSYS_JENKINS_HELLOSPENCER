pipeline {
    agent any

    environment {
        IMAGE_NAME = 'hellospencer-app'
        CONTAINER_NAME = 'spencer-api-container'
    }

    stages {
        stage('Checkout') {
            steps {
                cleanWs()
                checkout scm
            }
        }

        stage('Test (Unit Tests)') {
            agent {
                docker {
                    image 'python:3.11-slim'
                    reuseNode true
                }
            }
            steps {
                echo '--- Führe automatisierte Unit-Tests aus ---'
                sh '''
                    pip install -r requirements.txt
                    if [ ! -f count.txt ]; then echo "0" > count.txt; fi
                    python -m pytest tests/test_hello.py -v
                '''
            }
        }

        stage('Build Image') {
            steps {
                echo '--- Baue das App-Docker-Image ---'
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Deploy (Run Container)') {
            steps {
                echo '--- Deploye den API-Container auf dem Notebook ---'
                sh "docker rm -f ${CONTAINER_NAME} || true"
                sh "docker run -d -p 5556:5556 --name ${CONTAINER_NAME} ${IMAGE_NAME}:latest"
                sh 'sleep 3'
            }
        }

        stage('Integration Test (API Check)') {
            steps {
                echo '--- Verifiziere die Live-API mit curl und Integrationstests ---'
                sh 'curl http://localhost:5556/api/hello'
                sh 'python -m pytest tests/test_api.py -v'
            }
        }
    }
}