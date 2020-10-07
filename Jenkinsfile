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
        stage('Docker run') {
            steps {
                script {
                    sh "docker-compose build"
                    sh "docker-compose up -d"
                }
            }
        }
    }
}