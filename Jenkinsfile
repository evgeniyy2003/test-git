pipeline {
    agent any
    stages {
        stage('Packing') {
            steps {
                echo 'Pack the project....'
		sh 'mvn package'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
		sh 'cd target/rpm/dealhub_test/RPMS/noarch/ && for i in *.rpm; do rpm -Uvh $i; done'
            }
        }
    }
}
