# 📦 AWS CodePipeline Assignment - Weather App CI/CD 🚀
In this assignment, I reused the same Weather App (Flask-based) that I previously implemented using Jenkins and GitHub Actions. This time, I deployed the app using AWS CodePipeline, along with ECR (Elastic Container Registry), CodeBuild, and ECS (Elastic Container Service).

Below is a detailed explanation of the steps I took, key configurations, and important screenshots to add.

## 🔹 Step 1: Create ECR Repository
- Go to AWS Console > ECR

- Click Create repository

- Name: simple-web-app

- URI generated: 510001482086.dkr.ecr.us-east-1.amazonaws.com/simple-web-app
