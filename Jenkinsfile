pipeline {
    agent any
    stages {
        stage('Stage one') {
            steps {
                script {
                    echo "Parameter from template creation: " + templateParams.someParam
                }
            }
        }
        stage('Stage two') {
            steps {
                script {
                    echo "Job input parameter: " + params.myInput
                }
            }
        }
    }
}