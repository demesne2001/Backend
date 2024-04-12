
pipeline {
    agent any
   
    
    stages {
        stage('checkout') {
            steps {
               checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'python207', url: 'https://github.com/demesne2001/Backend.git']])
                echo 'checkout done'
            }
        }
        

        stage('Docker Image') {
            steps {                
                script{
                    def a=0
                    bat 'docker build . -f dockerfile.txt -t  webreportback'
                    a=1
                    if(a>0)
                    {
                         bat 'docker stop  webreportback'
                         bat 'docker rm  webreportback'
                    }
                }
                echo 'Docker Image done'
            }
        }
        stage('Docker Run') {
            steps {
                script{
                    bat 'docker run -p 7000:7000 -it -v SharedImages:/BackendForWebReport/Utility/Image -v SharePDF:/BackendForWebReport/Utility/PDF  -d --name  webreportback  webreportback'
                }
                echo 'Docker Running'
            }
        }
        stage('Docker push') {
            steps {
                script{
                    bat 'docker login -u patelom0910 -p 09102001Om'
                }
                echo 'Docker push done'
            }
        }
    }
}
