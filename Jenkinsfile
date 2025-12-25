pipeline {
    agent any
    
    // This ensures Jenkins looks for the Docker tool
    tools {
        dockerTool 'default' 
    }

    stages {
        stage('Build') {
                steps {
                sh 'docker build -t my-image-downloader .'
            }
        }
        stage('Test') {
                steps {
                sh 'docker run --rm my-image-downloader pytest'
            }
        }
    }
}