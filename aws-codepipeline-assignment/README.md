# 📦 AWS CodePipeline Assignment - Weather App CI/CD 🚀
In this assignment, I reused the same Weather App (Flask-based) that I previously implemented using Jenkins and. This time, I deployed the app using AWS CodePipeline, along with ECR (Elastic Container Registry), CodeBuild, and ECS (Elastic Container Service).

Below is a detailed explanation of the steps I took, key configurations, and important screenshots to add.

## 🔹 Step 1: Create ECR Repository
- Go to AWS Console > ECR

- Click Create repository

- Name: simple-web-app

- URI generated: 510001482086.dkr.ecr.us-east-1.amazonaws.com/simple-web-app


## 🔹 Step 2: Create CodePipeline

- Go to AWS Console > CodePipeline

- Click Create pipeline

- Choose Build custom pipeline

- Pipeline name: weather-app-pipeline

- Execution mode: Queued

- Service role: Create new or use existing (AWSCodePipelineServiceRole-us-east-1-weather-app-publish)

## 🔹 Step 3: Configure Source Stage

- Source provider: GitHub

- Connected using OAuth token

- Repository: Your weather app repo

- Branch: main

- Output artifact: SourceArtifact

##  🔹 Step 4: Create CodeBuild Project

- Create a new CodeBuild project

- Name: weather-app-build

- Environment: Managed image

- OS: Amazon Linux 2

- Runtime: Standard 5.0

- Privileged: Enabled (for Docker build)

Role: codebuild-weather-app-service-role

Timeout: 1 hour

Buildspec location: Use a buildspec file in the repo

## 🔹 Step 5: Add Build Stage in Pipeline

- Provider: AWS CodeBuild

- Project: weather-app-build

- Input Artifact: SourceArtifact

- Output Artifact: BuildArtifact

buildspec.yml used:

```
version: 0.2

phases:
  pre_build:
    commands:
      - echo Logging in to Amazon ECR...
      - aws --version
      - $(aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 510001482086.dkr.ecr.us-east-1.amazonaws.com)
  build:
    commands:
      - echo Building Docker image...
      - docker build -t simple-web-app .
      - docker tag simple-web-app:latest 510001482086.dkr.ecr.us-east-1.amazonaws.com/simple-web-app:latest
  post_build:
    commands:
      - echo Pushing Docker image to ECR...
      - docker push 510001482086.dkr.ecr.us-east-1.amazonaws.com/simple-web-app:latest
      - echo Creating imagedefinitions.json for CodePipeline
      - printf '[{"name":"weather-container","imageUri":"%s"}]' 510001482086.dkr.ecr.us-east-1.amazonaws.com/simple-web-app:latest > imagedefinitions.json

artifacts:
  files:
    - imagedefinitions.json

```

## 🔹 Step 6: Create ECS Cluster

- Go to ECS > Clusters

- Click Create Cluster > Networking only

- Name: weather-app-cluster

## 🔹 Step 7: Create Task Definition

- Launch Type: Fargate

- Task name: weather-task

- Container name: weather-container

- Image: 510001482086.dkr.ecr.us-east-1.amazonaws.com/simple-web-app

- Port mapping: 8080

## 🔹 Step 8: Create ECS Service

- Cluster: weather-app-cluster

- Task Definition: weather-task

- Service Type: Fargate

- Desired tasks: 1

- Network: Public subnet + Auto-assign IP

- Security Group: Inbound TCP 8080 from 0.0.0.0/0

## 🔹 Step 9: Add Deploy Stage in Pipeline

- Provider: Amazon ECS

- Cluster: weather-app-cluster

- Service: weather-task-service

- Input artifact: BuildArtifact

- Image definition file: imagedefinitions.json

## 🛠️ Permissions Fixes

- Attached AmazonEC2ContainerRegistryPowerUser to CodeBuild role

- Attached AmazonECS_FullAccess to CodePipeline role

📌 Summary

- This assignment was a hands-on practical of end-to-end CI/CD using AWS native tools:

- CodePipeline for automation

- CodeBuild to build Docker images

- ECR for image storage

- ECS to host and serve the containerized app

- It involved IAM, Docker, ECS networking, and buildspec scripting. Learned a lot!

