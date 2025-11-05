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
                bat 'python -m unittest discover tests'
            }
        }
    }

    post {
        success {
            echo 'All tests passed and package built successfully!Yayyyyyyyyyy'
        }
        failure {
            echo 'Something went wrong during the pipeline! :('
        }
    }
}
