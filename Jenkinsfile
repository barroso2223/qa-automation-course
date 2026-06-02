pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'pip install pytest selenium requests --break-system-packages'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh 'pytest test_basics.py test_api.py -v'
            }
        }
    }

    post {
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
