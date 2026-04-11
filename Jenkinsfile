pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout([
          $class: 'GitSCM',
          branches: [[name: '*/develop']],
          userRemoteConfigs: [[
            url: 'https://github.com/martinsangdo/python_flask_ecommerce.git',
            credentialsId: 'github-token'
          ]]
        ])
      }
    }

    stage('Debug Files') {
      steps {
        sh 'pwd'
        sh 'ls -la'
      }
    }

    stage('Install') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Build Docker') {
      steps {
        sh 'docker build -t fastapi-app .'
      }
    }

    stage('Deploy') {
      steps {
        sh 'kubectl rollout restart deployment fastapi-app'
      }
    }

    // stage('Test') {
    //   steps {
    //     sh 'pytest || true'
    //   }
    // }

    // stage('SonarQube') {
    //   steps {
    //     sh '''
    //     sonar-scanner \
    //       -Dsonar.projectKey=fastapi \
    //       -Dsonar.sources=. \
    //       -Dsonar.host.url=http://host.docker.internal:9000 \
    //       -Dsonar.login=YOUR_TOKEN
    //     '''
    //   }
    // }

  }
}