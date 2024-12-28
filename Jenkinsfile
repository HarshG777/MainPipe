pipeline{
  agent any
  environment{
    PYTHON_PATH = 'C:\Users\lenovo\AppData\Local\Programs\Python\Python313;C:\Users\lenovo\AppData\Local\Programs\Python\Python313\Scripts'
  }

  stages{
    stage('CheckOut'){
      steps{
        checkout scm
      }
    }

    stage('Build'){
      steps{
        bat '''
        set PATH = %PYTHON_PATH%;%PATH%
        pip install -r requirements.txt
        '''
      }
    }

    stage('SonarAnalysis'){
      environment{
        SONAR_TOKEN = credentials('sonarQub-token')
      }
      steps{
        bat '''
        set PATH = %PYTHON_PATH%;%PATH%
        sonar-scanner -Dsonar.projectKey=MainPipeline^
        -Dsonar.sources=.^
        -Dsonar.host.url=http://localhost:9000^
        -Dsonar.token=%SONAR_TOKEN%
        '''
      }
    }
  }

  post{
    success{
      echo "All GOOD"
    }
    failure{
      echo "Fail Someting went Wrong"
    }
  }

  
}



