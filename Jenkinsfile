pipeline {
    agent any
    stages {
        stage ('Initialize') {
            steps {
                sh '''
                    echo "PATH = ${PATH}"
                    echo "M2_HOME = ${M2_HOME}"
                ''' 
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'mvn -B -DskipTests clean package'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'mvn test'
            }
            post {
                always {
                    junit 'target/surefire-reports/*.xml'
                }
            }
        }
        stage('Packing') {
            steps {
                echo 'Pack the project....'
		sh 'mvn package'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying....'
		sh 'cd target/rpm/dealhub_calc/RPMS/noarch/ && for i in *.rpm; do echo $i; done'
            }
        }
    }
}
