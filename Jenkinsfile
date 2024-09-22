pipeline {
    agent { label 'build-agent' }
    environment {
        APP_NAME = "SDPX"
        DOCKER_REGISTRY = "" //any registry or build own?
        GIT_REPO_URL = "https://github.com/CE-RELATIONSHIP/jenkins-assignment.git"
        BRANCH = "jenkins-pipeline-peqch-only"
        APP = "app.py"
        UNIT_TEST = "unit_test.py"
    }

    stages {
        stage("Build") {
            steps {
                sh "echo Build"
            }
        }

        stage("Test"){
            steps {
                sh "echo Test"
            }
        }

        stage("Deliver") {
            steps {
                sh "echo Deliver"
            }
        }

        stage("Deploy") {
            agent { label 'deploy-server||build-agent' }
            steps {
                sh "echo Deploy"
            }
        }

    }
}