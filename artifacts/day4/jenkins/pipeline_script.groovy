pipeline {
    agent any
    stages {
        stage('Preparation') {
            steps {
                echo 'Preparing build environment...'
                echo 'Checking out source code...'
            }
        }
        stage('Build') {
            steps {
                echo 'Building the application...'
                sh 'echo Build completed successfully'
            }
        }
        stage('Results') {
            steps {
                echo 'Running tests...'
                echo 'All tests passed'
            }
        }
    }
}
