#!/bin/bash

# ----------------------------------
# CONFIGURATION
# ----------------------------------
AWS_REGION="us-east-1"
ACCOUNT_ID="510001482086"
ECR_REPO_NAME="hello-app"
IMAGE_TAG="latest"
CONTAINER_NAME="weather-container"

# Full image URI
IMAGE_URI="${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO_NAME}:${IMAGE_TAG}"

echo "🚀 Starting Weather App CI/CD Deployment..."

# ----------------------------------
# Step 1: Authenticate with ECR
# ----------------------------------
echo "🔐 Logging in to Amazon ECR..."
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com

# ----------------------------------
# Step 2: Build Docker image
# ----------------------------------
echo "🐳 Building Docker image..."
docker build -t $ECR_REPO_NAME .

# ----------------------------------
# Step 3: Tag Docker image
# ----------------------------------
echo "🏷️ Tagging image as $IMAGE_URI"
docker tag $ECR_REPO_NAME:latest $IMAGE_URI

# ----------------------------------
# Step 4: Push image to ECR
# ----------------------------------
echo "📦 Pushing image to Amazon ECR..."
docker push $IMAGE_URI

# ----------------------------------
# Step 5: Create imagedefinitions.json
# ----------------------------------
echo "📝 Generating imagedefinitions.json for CodePipeline"
echo "[{\"name\":\"$CONTAINER_NAME\",\"imageUri\":\"$IMAGE_URI\"}]" > imagedefinitions.json

echo "✅ Done. Your image is pushed and imagedefinitions.json is ready."
echo "➡️ Now go run the pipeline or deploy via ECS/CodePipeline."

