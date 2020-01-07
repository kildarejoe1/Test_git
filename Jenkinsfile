pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'apt-get install pip'
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python test.py'
      }
    }
  }
}
