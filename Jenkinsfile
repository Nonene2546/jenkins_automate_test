pipeline {
    agent { label 'build-agent' }
    environment {
        IMAGE_NAME = "spdx:${env.BUILD_NUMBER}"
    }

    stages {
        stage("Build") {
            steps {
                sh "echo Build"
                sh "docker build --tag ${IMAGE_NAME} ."
                sh "docker image ls"
            }
        }

        stage("Test"){
            steps {
                sh "echo Test"
                sh "docker rmi ${IMAGE_NAME}"
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