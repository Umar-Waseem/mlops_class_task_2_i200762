pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo "Cloning Repo"
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Umar-Waseem/learn-jenkins.git']])
            }
        }
        stage('Install Dependencies') {
            steps {
                echo 'Installing Dependencies'
                sh "pip install -r requirements.txt"
            }
        }
        stage('Testing') {
            steps {
                echo 'Running Tests'
                sh "pytest test.py"
            }
        }
        stage('Branch Name Check') {
            steps {
                echo 'Checking branch name'
                script {
                    def branchName = env.BRANCH_NAME
                    if (branchName == 'main') {
                        echo "Branch Name: ${branchName}"
                    }
                }
            }
        }
    }
}