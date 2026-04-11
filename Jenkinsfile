pipeline {
  agent {
    docker {
      image 'python:3.10'
    }
  }

  stages {
    stage('Checkout') {
      steps {
        git credentialsId: 'github-token',
            branch: 'develop',
            url: 'https://github.com/martinsangdo/python_flask_ecommerce.git'
      }
    }

    stage('Install') {
      steps {
        dir('python_flask_ecommerce') {
          sh 'pip install -r requirements.txt'
        }
      }
    }

    stage('Test') {
      steps {
        sh 'pytest || true'
      }
    }

    stage('SonarQube') {
      steps {
        sh '''
        sonar-scanner \
          -Dsonar.projectKey=fastapi \
          -Dsonar.sources=. \
          -Dsonar.host.url=http://host.docker.internal:9000 \
          -Dsonar.login=YOUR_TOKEN
        '''
      }
    }
  }
}