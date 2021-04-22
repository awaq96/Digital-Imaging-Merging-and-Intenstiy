pipeline {
    agent { docker { image 'pmantini/assignment-cosc6380:latest' } }

    environment {
        PATH = "env/bin/:$PATH"
    }
    stages {
        stage('build') {
            steps {
                sh 'python dip_hw0.py -il grace_1.png -ir grace_2.png -c 155'
                sh 'python dip_hw0.py -il grace_1.png -ir grace_2.png -c 200'
                sh 'python dip_hw0.py -il grace_1.png -ir grace_2.png -c 155 -a 0.5 -b 0.5'
                sh 'python dip_hw0.py -il grace_1.png -ir grace_2.png -c 155 -a 0.75 -b 0.25'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'output/**/*.* ', onlyIfSuccessful: true
        }
    }
}