pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/YvaishaliR/cold.git'
            }
        }

        stage('Test') {
            steps {
                bat 'python3 -m unittest discover tests'
            }
        }

        stage('Package') {
            steps {
                bat 'zip -r cold.zip cold'
            }
        }
    }

    post {
        success {
            echo 'All tests passed and package built successfully!'
        }
        failure {
            echo 'Something went wrong during the pipeline!'
        }
    }
}
