pipeline {
    agent any

    environment {
        PYTHON_VENV = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Cloning repository..."
                git branch: 'main', url: 'https://github.com/haritha7592/interviewpracticeprograms.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo "Creating virtual environment and installing dependencies..."
                sh '''
                python3 -m venv ${PYTHON_VENV}
                source ${PYTHON_VENV}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Smoke Tests') {
            steps {
                echo "Running Behave smoke tests..."
                sh '''
                source ${PYTHON_VENV}/bin/activate
                behave --tags @smoke --junit --junit-directory=reports
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                echo "Generating Allure report..."
                sh '''
                allure generate ./reports -o ./allure-report --clean
                '''
            }
        }
    }

    post {
        always {
            echo "Cleaning workspace..."
            cleanWs()
        }
    }
}
