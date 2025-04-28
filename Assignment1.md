# 🖥️ Jenkins Local Setup on Windows (Without Commands)
 
This guide helps you install and set up Jenkins **locally on a Windows machine** without using any terminal or command line. Perfect for beginners! ✅
 
---
 
## 📥 Step 1: Download Jenkins for Windows
 
1. Go to the official Jenkins download page:

   👉 [https://www.jenkins.io/download/](https://www.jenkins.io/download/)
 
2. Under **Windows**, click **"Download"**.
 
---
 
## 📦 Step 2: Install Jenkins
 
1. After downloading the `.msi` installer file, **double-click** to open it.

2. The Jenkins Setup Wizard will launch.

3. Follow the steps:

   - Accept license terms

   - Choose the installation path (or leave it as default)

   - Keep the default port `8080`

   - Proceed with the installation
 
4. Wait for the installation to complete.
 
---
 
## 🔐 Step 3: Unlock Jenkins
 
1. Once installed, Jenkins will open automatically in your browser:

   👉 [http://localhost:8080](http://localhost:8080)
 
2. It will ask you for an **initial admin password**.
 
3. Open **File Explorer** and navigate to:

 
4. Open the `initialAdminPassword` file and **copy** the password.
 
5. Paste it into the Jenkins setup screen to unlock.
 
---
 
## 🔌 Step 4: Install Suggested Plugins
 
1. Jenkins will ask what plugins to install.

2. Click **“Install suggested plugins”**.

3. Wait while the plugins are downloaded and installed.
 
---- Click **Save and Finish**.
 
---
 
## ✅ Jenkins is Ready!
 
Click **"Start using Jenkins"** and you’ll be taken to the Jenkins dashboard. 🎉
 
You're now ready to:
 
- Create pipelines

- Integrate with GitHub

- Automate your builds and deployments
 
## 👤 Step 5: Create Your First Admin User
 
Fill in the details:
 
- **Username**: Abhay

- **Password**: ------  

- **Full Name**: Abhay Sharma 

- **Email**: abhay.svce@gmail.com
 
Click **Save and Continue**.
 
---
 
## 🌐 Step 6: Configure Jenkins URL
 
- Jenkins will auto-fill the local URL:

### 🧪 Step 7: Jenkinsfile Created on GitHub & CI/CD Pipeline Setup
After successfully setting up Jenkins, I created a simple Jenkinsfile in my GitHub repository to test the CI/CD pipeline.

🔹 Jenkinsfile Content
Here’s the content of the Jenkinsfile I added to the root of my GitHub repository:


```
pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Build Code') {
            steps {
                bat 'javac HelloWorld.java'
            }
        }
        stage('Run Code') {
            steps {
                bat 'java HelloWorld'
            }
        }
    }
}

```
🔹 GitHub Repository
The Jenkinsfile is located in this GitHub repo:
🔗 https://github.com/AbhaySharma0017/devops-learning-journey.git

🔹 CI/CD Pipeline Setup in Jenkins
To connect Jenkins with the GitHub repo:

1.Opened Jenkins dashboard → Clicked "New Item"

2.Selected Pipeline → Named it hello-world-pipeline

3.Chose "Pipeline script from SCM"

4.Selected:

5.SCM: Git

6.Repository URL: https://github.com/AbhaySharma0017/devops-learning-journey.git

(If private repo: added GitHub credentials)
my repo is public so credentials do not required here

7.Set the branch to main (or whichever branch contains the Jenkinsfile)

8.Clicked Save and then "Build Now"

✅ Pipeline Output
The build was triggered, and in the Jenkins console log, I saw:

Started by user Abhay

Obtained Jenkinsfile from git https://github.com/AbhaySharma0017/devops-learning-journey.git

[Pipeline] Start of Pipeline

[Pipeline] node

Running on Jenkins in C:\ProgramData\Jenkins\.jenkins\workspace\HelloWorldPipeline

[Pipeline] {

[Pipeline] stage

[Pipeline] { (Declarative: Checkout SCM)

[Pipeline] checkout

The recommended git tool is: NONE

using credential 4d33095c-7137-4a6f-8e56-46fde1700e76

Cloning the remote Git repository
Cloning repository https://github.com/AbhaySharma0017/devops-learning-journey.git
 > C:\Users\abhay.s\AppData\Local\Programs\Git\cmd\git.exe init C:\ProgramData\Jenkins\.jenkins\workspace\HelloWorldPipeline # timeout=10

Fetching upstream changes from https://github.com/AbhaySharma0017/devops-learning-journey.git
 > C:\Users\abhay.s\AppData\Local\Programs\Git\cmd\git.exe --version # timeout=10

 > git --version # 'git version 2.48.1.windows.1'
using GIT_ASKPASS to set credentials GitHub PAT for Jenkins

 > C:\Users\abhay.s\AppData\Local\Programs\Git\cmd\git.exe fetch --tags --force --progress -- https://github.com/AbhaySharma0017/devops-learning-journey.git +refs/heads/*:refs/remotes/origin/* # timeout=10

 > C:\Users\abhay.s\AppData\Local\Programs\Git\cmd\git.exe config remote.origin.url https://github.com/AbhaySharma0017/devops-learning-journey.git # timeout=10

 > C:\Users\abhay.s\AppData\Local\Programs\Git\cmd\git.exe config --add remote.origin.fetch +refs/heads/*:refs/remotes/origin/* # timeout=10
Avoid second fetch

 > C:\Users\abhay.s\AppData\Local\Programs\Git\cmd\git.exe rev-parse "refs/remotes/origin/master^{commit}" # timeout=10
Checking out Revision 91e07a93fb2392ee02cc71e1a74d7aa846f56720 (refs/remotes/origin/master)

 > C:\Users\abhay.s\AppData\Local\Programs\Git\cmd\git.exe config core.sparsecheckout # timeout=10

 > C:\Users\abhay.s\AppData\Local\Programs\Git\cmd\git.exe checkout -f 91e07a93fb2392ee02cc71e1a74d7aa846f56720 # timeout=10

Commit message: "Create helloWorld.sh"

First time build. Skipping changelog.

[Pipeline] }

[Pipeline] // stage

[Pipeline] withEnv

[Pipeline] {

[Pipeline] stage

[Pipeline] { (Checkout Code)

[Pipeline] checkout

The recommended git tool is: NONE

using credential 4d33095c-7137-4a6f-8e56-46fde1700e76
 > C:\Users\abhay.s\AppData\Local\Programs\Git\cmd\git.exe rev-parse --resolve-git-dir C:\ProgramData\Jenkins\.jenkins\workspace\HelloWorldPipeline\.git # timeout=10

Fetching changes from the remote Git repository
 > C:\Users\abhay.s\AppData\Local\Programs\Git\cmd\git.exe config remote.origin.url https://github.com/AbhaySharma0017/devops-learning-journey.git # timeout=10

Fetching upstream changes from https://github.com/AbhaySharma0017/devops-learning-journey.git
 > C:\Users\abhay.s\AppData\Local\Programs\Git\cmd\git.exe --version # timeout=10

 > git --version # 'git version 2.48.1.windows.1'

using GIT_ASKPASS to set credentials GitHub PAT for Jenkins
 > C:\Users\abhay.s\AppData\Local\Programs\Git\cmd\git.exe fetch --tags --force --progress -- https://github.com/AbhaySharma0017/devops-learning-journey.git +refs/heads/*:refs/remotes/origin/* # timeout=10

 > C:\Users\abhay.s\AppData\Local\Programs\Git\cmd\git.exe rev-parse "refs/remotes/origin/master^{commit}" # timeout=10
Checking out Revision 91e07a93fb2392ee02cc71e1a74d7aa846f56720 (refs/remotes/origin/master)

 > C:\Users\abhay.s\AppData\Local\Programs\Git\cmd\git.exe config core.sparsecheckout # timeout=10

 > C:\Users\abhay.s\AppData\Local\Programs\Git\cmd\git.exe checkout -f 91e07a93fb2392ee02cc71e1a74d7aa846f56720 # timeout=10

Commit message: "Create helloWorld.sh"
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Build Code)
[Pipeline] bat

C:\ProgramData\Jenkins\.jenkins\workspace\HelloWorldPipeline>javac HelloWorld.java 
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Run Code)
[Pipeline] bat

C:\ProgramData\Jenkins\.jenkins\workspace\HelloWorldPipeline>java HelloWorld 
Hello World!
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS

🎉 Boom! Jenkins successfully cloned the repo, read the Jenkinsfile, and executed it.

> And I did my first Assignment.
> 
