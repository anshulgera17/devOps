# Jenkins setup and learning 
- Q1. What is Jenkins ?
#### Answer
- An open source automation server which enables developers around the world to reliably build, test, and deploy their software.

- Q2. What is CI-CD ?

## LearningJenkins
- Blue ocean aggregator plugin in jenkins for generate pipeline code
- Scripted pipeline (preparation, build and results stages here) using groovy scripting language
- Declarative pipeline (it is having stages and steps in it with in pipeline)
- Declarative detective generator
- Groovy vs DSL 
- Jenkinsfile: if you wanna use source control outside jenkins server then use JenkinsFile to do
- Pipeline → Stages → stage → steps 
- You can have agent, tools, option, triggers - inside pipeline 

### Jenkins installation process
```
sudo apt-get update
sudo apt-get install default-jre
sudo apt-get install default-jdk
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer
sudo update-alternatives --config java
sudo vi /etc/environment
add this line JAVA_HOME="/usr/lib/jvm/java-8-oracle"
echo $JAVA_HOME
```

```
wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
echo deb https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list
sudo apt-get update
```
- For the versions in cache `apt-cache policy jenkins`
- `sudo apt-get install jenkins=2.176.3`  (for specific version)
- `sudo systemctl start jenkins`
- `sudo systemctl status jenkins`

#### Step 3 — Opening the Firewall
- By default, Jenkins runs on port 8080, so we'll open that port using ufw `sudo ufw allow 8080`
- We can see the new rules by checking UFW's status `sudo ufw status`

- If you use Ubuntu, you can find initialAdminPassword using `sudo cat /var/lib/jenkins/secrets/initialAdminPassword`
- then configure the username and password for jenkins login, then you can login http://----url----:8080/

```
pipeline {
    agent {
        docker{image 'python:alpine'
            args '-u root'
        }
    }
    stages{
        stage('prep'){
            steps{
                sh 'apk add git'
            }
        }
        stage('fetch'){
            steps{
                sh 'git clone https://github.com/linuxacademy/content-pipelines-cje-labs.git'
            }
        }
        stage('install'){
            steps{
                sh 'pip install -r content-pipelines-cje-labs/lab3_lab4/dog_pics_downloader/requirements.txt'
            }
        }
        stage('execute'){
            steps{
                sh 'python content-pipelines-cje-labs/lab3_lab4/dog_pics_downloader/dog_pic_get_class.py'
            }
        }
    }
    post{
        always{
            echo "job execution complete"
        }
        success{
            archiveArtifacts artifacts: '*.jpg'
        }
        cleanup{
            echo "cleaning up"
            sh 'rm -rf content-pipelines-cje-labs'
        }
    }
}
```

```
pipeline{
    agent{
            docker{image 'centos:7'
            args '-u root'
            label 'docker2'
    }
	}
    stages{
        stage ('dependencies'){
            steps{
                sh 'yum -y install python3 python3-pip zlib-devel gcc git'
            }
        }
        stage('coptart'){
            steps{
                copyArtifacts(projectName: 'pipeline1', flatten: true)
            }
        }
        stage('fetch'){
            steps{
                sh 'git clone https://github.com/linuxacademy/content-pipelines-cje-labs.git'
            }
        }
        stage('install'){
            steps{
                sh 'pip3 install -r content-pipelines-cje-labs/lab3_lab4/image_watermarker/requirements.txt'
            }   
        }
        stage('exec'){
            steps{
                sh 'python3 content-pipelines-cje-labs/lab3_lab4/image_watermarker/watermark.py'
            }
            
        }
    }
    post{
        always{
            echo "job execution complete"
        }
        success{
            archiveArtifacts artifacts: '*watermarked.jpg'
        }
        cleanup{
            echo "cleaning up"
            sh 'rm -rf content-pipelines-cje-labs'
        }
    }
}
```