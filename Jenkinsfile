pipeline {
    agent any
    parameters {
        string(name:"tag", defaultValue: 'latest', description: "Docker image tag")
    }
    environment {
        DOCKER_HUB = credentials('docker-hub')
    }
    stages {
        stage('Docker build') {
            steps {
                sh "docker build  ./back/ -t fe:latest"
            }
        }
        stage('Docker login') {
            steps {
                sh "docker login -u=${DOCKER_HUB_USR} -p=DOCKER_HUB_PSW"
            }
        }
        stage('Docker push') {
            steps {
                sh "docker push jrubics/jenkins-test:${params.tag}"
            }
        }
    }
}