def unitStatus
def robotStatus

pipeline {
    agent { label 'vm2test' }
    environment {
        APP_NAME = "web-api"
        IMAGE_NAME = 'spdx:${BUILD_NUMBER}'
        ROBOT_REPO = 'https://github.com/Nonene2546/jenkins_robot.git'
        ROBOT_BRANCH = 'main'
        MAIN_REPO = 'https://https://github.com/CE-RELATIONSHIP/jenkins-assignment/'
        MAIN_BRANCH = 'jenkins-pipeline-peqch-only'
    }

    stages {
        stage("Remove old images/containers"){
            steps{
                sh "docker stop \$(docker ps -a -q) || true"
                sh "docker rm \$(docker ps -a -q) || true"
                sh "docker rmi -f \$(docker images -q) || true"
            }
        }
        stage("Build") {
            steps {
                sh "docker build --tag ${IMAGE_NAME} ."
                sh "docker image ls"
            }
        }

        stage("Run and Test"){
            steps {
                ////// update and start container //////
                script {
                    sh(script: "docker stop ${APP_NAME}", returnStatus: true)
                    sh(script: "docker rm ${APP_NAME} -f", returnStatus: true)

                    sh(script: "docker run --name ${APP_NAME} -d -p 80:5000 ${IMAGE_NAME}")
                }

                ////// unit test running batch  //////
                script {
                    def output = sh(
                        returnStatus: true,
                        returnStdout: true, 
                        script: "docker exec ${APP_NAME} sh -c 'python -m unit_test -v;'"
                        )
                }
                /////////////////////////////////////////
            }
        }
        stage("Clone robot repo"){
            steps {
                git branch: "${ROBOT_BRANCH}", url: "${ROBOT_REPO}"
            }
        }

        stage("Robot Test") {
            steps {
                sh "pip install -r requirements.txt"
                sh "robot test_suite.robot"
            }
        }

    }
}