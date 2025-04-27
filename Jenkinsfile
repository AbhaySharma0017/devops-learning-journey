pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Build Code') {
            steps {
                bat 'javac HelloWorld.java'
            }
        }
        stage('Run Code') {
            steps {
                bat 'java HelloWorld'
            }
        }
    }
}
