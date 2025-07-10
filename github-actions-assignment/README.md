#  📦GitHub Actions CI/CD Assignment - Weather App
In this assignment, I replicated my Jenkins-based CI/CD pipeline using GitHub Actions with a self-hosted runner, using the same weather application built with Python, Flask, HTML, CSS, and JS.

- **Application Repository:** [Weather App](https://github.com/AbhaySharma0017/Weather-App/tree/main)
- **GitHub Actions Workflow File:** [deploy.yml](https://github.com/AbhaySharma0017/Weather-App/blob/main/.github/workflows/deploy.yaml)

## ✅ Assignment Objectives
- Build and run a Python Flask web app

- Create Docker image

- Push Docker image to DockerHub

- Deploy and run container using GitHub Actions self-hosted runner

  ## 🧠 Concepts Covered
- GitHub Actions workflow and syntax

- Self-hosted runners for custom environment control

- Docker build, tag, push to DockerHub

- GitHub Secrets for secure credential handling

# 🧭 Step-by-Step Setup

## 🔹 Step 1: Set Up Self-Hosted Runner
1. Go to GitHub repo → Settings > Actions > Runners

2. Click Add Runner → choose Linux x64

3. Follow instructions to register runner:

```
# Create a folder
$ mkdir actions-runner && cd actions-runner# Download the latest runner package
$ curl -o actions-runner-linux-x64-2.326.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.326.0/actions-runner-linux-x64-2.326.0.tar.gz# Optional: Validate the hash
$ echo "9c74af9b4352bbc99aecc7353b47bcdfcd1b2a0f6d15af54a99f54a0c14a1de8  actions-runner-linux-x64-2.326.0.tar.gz" | shasum -a 256 -c# Extract the installer
$ tar xzf ./actions-runner-linux-x64-2.326.0.tar.gz

# Create the runner and start the configuration experience
$ ./config.sh --url https://github.com/AbhaySharma0017/Weather-App --token BJYTHIEAMCTCVK2ZMVW7ZQDIN72SO# Last step, run it!
$ ./run.sh
```

## 🔹 Step 2: Add GitHub Secrets
Go to Settings > Secrets and variables > Actions:

- DOCKER_USERNAME: your DockerHub username
- DOCKER_PASSWORD: your DockerHub password or personal access token

## 🔹 Step 3: GitHub Actions Workflow
Create file: deploy.yml 

```
name: CI/CD Pipeline - Flask App

on: 
  workflow_dispatch:

jobs:
  build-and-push:
    runs-on: self-hosted

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Build Docker image
      run: |
        docker build -t ${{ secrets.DOCKER_USERNAME }}/weather-app:${{ github.run_number }} .

    - name: Run Docker container
      run: |
        docker stop weather-app-container || true
        docker rm weather-app-container || true
        docker run -d -p 8080:8080 --name weather-app-container ${{ secrets.DOCKER_USERNAME }}/weather-app:${{ github.run_number }}

    - name: Log in to DockerHub
      run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

   
    - name: Push Docker image to DockerHub
      run: |
        docker push ${{ secrets.DOCKER_USERNAME }}/weather-app:${{ github.run_number }}
```

## 🔹 Step 5: Access Deployed Flask App

Make sure port 8080 is open in your EC2 Security Group

Access the app at:
```
http://<EC2-PUBLIC-IP>:8080
```

## ✅ Successfully deployed Flask weather app using GitHub Actions, Docker, and EC2 self-hosted runner!
