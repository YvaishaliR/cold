pipeline {
    agent any

    stages {

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover tests'
            }
        }
    }

    post {
        success {
            echo 'All tests passed and package built successfully!Meow!'
        }
        failure {
            echo 'Something went wrong during the pipeline! :('
        }
    }
}
