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
                sh 'python3 -m unittest discover tests'
            }
        }
    }

    post {
        success {
            echo 'All tests passed and package built successfully!Yayyyyyyyyyy! From ec2!Added webhook :)'
        }
        failure {
            echo 'Something went wrong during the pipeline!'
        }
    }
}
