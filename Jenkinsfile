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

            step {
                stages {
                    stage("Clone") {
                        step {
                            sh "echo cloning repo" 
                            sh "git pull origin jenkins-pipeline-peqch-only"
                        }
                    }
                    // stage("Build") {

                    // }
                    // stage("Test") {

                    // }
                    // stage("Deliver") {

                    // }
                }
            }
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