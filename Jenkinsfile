pipeline{
        agent any
        stages{
            stage('Testing'){
                steps{
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
        }
}