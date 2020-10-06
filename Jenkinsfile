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
        stage('Stage one') {
            steps {
                script {
                    echo "Hello"
                }
            }
        }
        stage('Stage two') {
            steps {
                script {
                    dockerImage = docker.build tag
                }
            }
        }
    }
}