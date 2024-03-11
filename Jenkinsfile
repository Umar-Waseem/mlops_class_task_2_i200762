pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo "Cloning Repo"
                sh "ls"
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Umar-Waseem/mlops_class_task_2_i200762.git']])
            }
        }
        stage('Install Dependencies') {
            steps {
                echo 'Installing Dependencies'
                sh "pip3 install -r requirements.txt"
            }
        }
        stage('Testing') {
            steps {
                echo 'Running Tests'
                sh "python3 -m pytest test.py"
            }
        }
        stage('Branch Name Check') {
            steps {
                echo 'Checking branch name'
                script {
                    def branchName = "${env.GIT_BRANCH}"
                    if (branchName == 'main') {
                        echo "Branch Name: ${branchName}"
                    }
                }
            }
        }
    }
}
