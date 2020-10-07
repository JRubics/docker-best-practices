pipeline {
    agent any
    parameters {
        string(name:"tag", defaultValue: 'latest', description: "Docker image tag")
    }
    stages {
        stage('Docker build') {
            steps {
                sh "docker build  ./back/ -t fe:latest"
            }
        }
        stage('Docker login') {
            steps {
                withCredentials ([
                    usernamePassword(credentials: 'docker-hub', usernameVariable: USER, passwordVariable: PASS)
                ]) {
                    sh "docker login -u=$USER -p=$PASS" 
                }
            }
        }
        stage('Docker push') {
            steps {
                sh "docker push jrubics/jenkins-test:${params.tag}"
            }
        }
    }
}