pipeline {
    environment { 
        tag = "jrubics/test:latest" 
    }
    agent any
    stages {
        stage('Cloning from Git master') {
            when {
                branch 'master'
            }
            steps { 
                sh "git clone https://github.com/JRubics/docker-best-practices.git"
            }
        }
        stage('Cloning from Git test') {
            when {
                branch 'test'
            }
            steps { 
                sh "git clone -b test https://github.com/JRubics/docker-best-practices.git"
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