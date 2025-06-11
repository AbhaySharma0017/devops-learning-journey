# HelloWorld Flask App with Jenkins CI/CD

This project demonstrates a basic **CI/CD pipeline using Jenkins** to automate the build and deployment of a simple **Flask "Hello, Abhay" app** on an **AWS EC2 instance** using **Docker**.

---

## 🔧 Tech Stack

- Python Flask (HelloWorld app)
- Docker
- Jenkins (Declarative Pipeline)
- AWS EC2 (Ubuntu)
- GitHub (for source control)

---

## 🚀 What This Pipeline Does

1. **Pulls code** from GitHub (main branch)
2. **Builds Docker image** from the `Dockerfile` located in the `ci-cd` directory
3. **Runs the Docker container** on port 5000
4. Accessible via: `http://<your-ec2-public-ip>:5000`

---

## 🛠️ Setup Instructions

### 1. Launch EC2 Instance

- Type: `t2.micro` (Ubuntu 22.04)
- Open ports in **Security Group**:
  - **8080** for Jenkins
  - **5000** for Flask app

### 2. Install Jenkins

```bash
sudo apt update
sudo apt install -y openjdk-17-jdk
curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update
sudo apt install -y jenkins
sudo systemctl enable jenkins
sudo systemctl start jenkins
```
### 3. Install Docker

```bash
sudo apt install -y ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg \
  --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo $VERSION_CODENAME) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### 4. Give Jenkins Docker Permissions
```bash
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
```

### 🔄 Jenkins CI/CD Pipeline
- Jenkins pulls the latest code from GitHub

- Builds Docker image from the ci-cd folder

- Runs the container on port 5000 with name flask-container

## Jenkinsfile Snippet:
```bash
pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app ./ci-cd'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker rm -f flask-container || true'
                sh 'docker run -d -p 5000:5000 --name flask-container flask-app'
            }
        }
    }
}
```
## 🌐 Access the App
### After the pipeline runs:
```bash
http://<your-ec2-public-ip>:5000
```
### We should see:
```bash
Hello, Abhay from Flask!
```

---

