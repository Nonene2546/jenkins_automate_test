pipeline {
    agent { label 'build-agent' }
    environment {
        APP_NAME = "SDPX"
        DOCKER_REGISTRY = "" //any registry or build own?
        APP = "app.py"
        UNIT_TEST = "unit_test.py"
    }

    stages {
        stage("Build and Test") {
            steps {
                sh "echo cloning repo"
                sh "git pull origin jenkins-pipeline-peqch-only" 
            }
        }
        stage("Build") {
            steps {
                sh "echo Build" 
            }
        }

        stage("Test") {
            steps {
                sh "echo Test" 
            }
        }

        stage("Deliver") {
            steps {
                sh "echo Deliver" 
            }
        }
    }
}