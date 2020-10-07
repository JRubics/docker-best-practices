pipeline {
    agent any
    parameters {
        string(name:"tag", defaulValue: 'latest', description: "Docker image tag")
    }
    stages {
        stage('Docker build') {
            steps {
                docker build  ./back/ -t "fe:latest"
            }
        }
        stage('Docker login') {
            steps {
                withCredentials ([
                    usernamePassword(credentials: 'docker-hub', usernameVariable: USER, passwordVariable: PASS)
                ]) {
                    docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD"
                }
            }
        }
        stage('Docker push') {
            steps {
                docker push "jrubics/jenkins-test:${params.tag}"
            }
        }
    }
}