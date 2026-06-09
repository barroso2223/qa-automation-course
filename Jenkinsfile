pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'pip install pytest requests --break-system-packages'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running automated tests...'
                sh 'pytest test_basics.py test_api.py -v'
            }
        }

        stage('Results') {
            steps {
                echo 'All tests completed'
            }
        }
    }

    post {
        success {
            echo 'Pipeline passed - All tests green!'
        }
        failure {
            echo 'Pipeline failed - check test results!'
        }
    }
}
