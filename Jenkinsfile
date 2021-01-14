pipeline {
    agent any
    stages {
        stage('Packing') {
            steps {
                echo 'Pack the project....'
		sh 'mvn package'
            }
        }
    }
}
