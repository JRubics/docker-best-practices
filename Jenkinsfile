pipeline {
    agent any
    stages {
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
                    cat README.md
                }
            }
        }
    }
}