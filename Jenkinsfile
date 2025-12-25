pipeline {
    agent any

    stages {
        stage('Build Image') {
            steps {
                // This builds the Docker image using the same command you used manually
                sh 'docker build -t my-image-downloader .'
            }
        }
        stage('Run Tests') {
            steps {
                // This runs your pytest inside the container to make sure the code is healthy
                sh 'docker run --rm my-image-downloader pytest'
            }
        }
        stage('Run App') {
            steps {
                // This runs the actual downloader
                sh 'docker run --rm my-image-downloader'
            }
        }
    }
}