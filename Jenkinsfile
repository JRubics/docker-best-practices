pipeline {
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
                    sh "docker build docker-best-practices/. -t test"
                    sh "docker images"
                }
            }
        }
    }
}