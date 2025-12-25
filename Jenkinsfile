pipeline {
    agent any

    stages {
        // --- CI PHASE ---
        stage('Build Image') {
            steps {
                sh 'docker build -t my-image-downloader .'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'docker run --rm my-image-downloader pytest'
            }
        }

        // --- CD PHASE ---
        stage('Deploy') {
            steps {
                echo 'CI Passed! Deploying...'
                // Remove old container if it exists, then start new one
                sh 'docker rm -f production-app || true'
                sh 'docker run -d --name production-app my-image-downloader'
            }
        }
    }
}