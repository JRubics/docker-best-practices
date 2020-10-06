pipeline {
    environment { 
        tag = "jrubics/test:latest" 
    }
    agent any
    stages {
        stage('Cloning from Git') { 
            steps { 
                git 'https://github.com/JRubics/docker-best-practices.git' 
            }
        }
        stage('Docker build') {
            steps {
                script {
                    sh "ls -la"
                }
            }
        }
    }
}