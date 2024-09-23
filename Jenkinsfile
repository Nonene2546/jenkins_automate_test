def unitStatus
def robotStatus

pipeline {
    agent { label 'vm2test' }
    environment {
        APP_NAME = "web-api"
        IMAGE_NAME = 'spdx'

        ROBOT_REPO = 'https://github.com/Nonene2546/jenkins_robot.git'
        ROBOT_BRANCH = 'main'
        ROBOT_FILE = 'test_suite.robot'

        MAIN_REPO = 'https://https://github.com/CE-RELATIONSHIP/jenkins-assignment/'
        MAIN_BRANCH = 'jenkins-pipeline-peqch-only'

        NAMESPACE = 'nonene2546'
        GITHUB_CRED = credentials('ghcr-token')
        GITHUB_CRED_USR = 'nonene2546'
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
                script {
                    sh(script: "docker run --name ${APP_NAME} -d -p 80:5000 ${IMAGE_NAME}")
                }

                script {
                    def output = sh(
                        returnStatus: true,
                        returnStdout: true, 
                        script: "docker exec ${APP_NAME} sh -c 'python -m unit_test -v;'"
                        )
                }
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
                sh "robot ${ROBOT_FILE}"
            }
        }

        stage("Release") {
            steps {
                echo "Release ${GITHUB_CRED_PSW}"
                sh "docker tag ${IMAGE_NAME} ghcr.io/${NAMESPACE}/${IMAGE_NAME}"
                sh "docker tag ${IMAGE_NAME} ghcr.io/${NAMESPACE}/${IMAGE_NAME}:${BUILD_NUMBER}"

                sh "docker login ghcr.io -u ${GITHUB_CRED_USR} -p ${GITHUB_CRED_PSW}"

                sh "docker push ghcr.io/${NAMESPACE}/${IMAGE_NAME}"
                sh "docker push ghcr.io/${NAMESPACE}/${IMAGE_NAME}:${BUILD_NUMBER}"

                sh "docker inspect ghcr.io/${NAMESPACE}/${IMAGE_NAME}"
                sh "docker inspect ghcr.io/${NAMESPACE}/${IMAGE_NAME}:${BUILD_NUMBER}"

                sh "docker image prune -a -f"
            }
        }

        stage("Deploy") {
            agent { label 'preprod' }
            steps {
                sh "docker login ghcr.io -u ${GITHUB_CRED_USR} -p ${GITHUB_CRED_PSW}"
                sh "docker pull ghcr.io/${NAMESPACE}/${IMAGE_NAME}"

                sh returnStatus: true, script: "docker stop ${APP_NAME}"
                sh returnStatus: true, script: "docker rm ${APP_NAME} -f"
                sh "docker run --name ${APP_NAME} -d -p 5000:5000 ghcr.io/${NAMESPACE}/${IMAGE_NAME}"
            }
        }

    }
}