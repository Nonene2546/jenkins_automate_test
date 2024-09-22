pipeline {
    agent { label 'build-agent' }
    environment {
        APP_NAME = "SDPX"
        DOCKER_REGISTRY = "" //any registry or build own?
        REPO_URL_SIMPLE_API = "https://github.com/CE-SDPX/simple-api.git"
        APP = "app.py"
        UNIT_TEST = "unit_test.py"
    }

    stages {
        stage("Build and Test") {
            stage("Clone") {
                step {
                    sh "echo cloning repo" 
                    sh "git remote -v"
                    sh "robot --version"
                }
            }
            // stage("Build") {

            // }
            // stage("Test") {

            // }
            // stage("Deliver") {

            // }
        }

        // stage("Deploy") {
        //     stage("Build") {

        //     }
        //     stage("Build") {

        //     }
        //     stage("Test") {

        //     }
        // }
    }

}