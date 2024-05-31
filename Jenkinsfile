pipeline{
  agent any

  triggers {
    githubPush()
  }

  stages {
    stage('checkout') {
      steps {

        checkout scm
      }
    }
  }
}
