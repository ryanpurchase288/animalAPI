pipeline{
        agent any
        stages{
            stage('Testing'){
                steps{
                    slackSend channel: '#jenkins', message: 'Starting services'
                    sh "./scripts/test.sh"
                }
            }
            stage('Build'){
                steps{
                    sh "./scripts/build.sh"
                }
            }
            stage('Deploy App'){
                steps{
                    sh "./scripts/deploy.sh"
                    
                }
            }
            stage('Slack send'){
                steps{
                    slackSend channel: '#jenkins', message: 'App running successfully'
                }
            }
        }
}