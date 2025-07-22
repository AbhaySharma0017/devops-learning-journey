# 🚀 Terraform Assignment - AWS Infrastructure Provisioning

# Description:
## This project provisions a complete AWS infrastructure using Terraform,including VPC, EKS, ECS, EC2, RDS (MySQL), S3, and supporting resources.

# Structure:
## - Terraform Modules and Resources
## - Uses remote and local resources
## - Outputs EC2 public IPs for easy access

# 🛠️ Tools Required:
## - Terraform >= v1.3.0
## - AWS CLI (configured)
## - SSH Key Pair

# 📂 File Structure:
## ├── assign.tf           → Main infrastructure (VPC, EKS, ECS, RDS, S3)
## ├── ec2_created.tf      → EC2 instance creation with key pair and SG
## ├── providers.tf        → AWS provider and region
## ├── variables.tf        → Variables for EC2, VPC, etc.
## ├── main.tf             → Local resource for demonstration (local file)
## ├── output.tf           → Outputs for EC2 details
## ├── s3_create.tf        → Extra S3 bucket creation
## └── install_docker.sh   → Script to install Docker on EC2

# 📦 Resources Created:

## ✅ VPC
###   - Public and private subnets across two AZs
###   - NAT Gateway

## ✅ EKS Cluster
###   - Managed node group with t3.medium instances

## ✅ ECS Cluster
###   - Basic ECS cluster setup

## ✅ S3 Bucket
###   - Bucket: <project_name>-bucket-by-terraform

## ✅ RDS MySQL Instance
###   - Engine: MySQL 8.0
###   - Storage: 20 GB
###  - Subnet Group: Uses private subnets
###   - Security Group: Port 3306 open to 0.0.0.0/0

## ✅ EC2 Instance
###   - Ubuntu AMI with Docker installed via user_data
###   - Security group with SSH and HTTP access

## ✅ Local File
###   - automate.txt created using Terraform local_file resource


# 🔐 Key Pair:
## - Key: terra-key (you must have terra-key.pub in root directory)

# 🚀 Usage:
## 1. Clone the Repo
```git clone <your-repo-url>
   cd <project-folder>
```
## 2. Initialize Terraform
```
terraform init
```
## 3. Plan the Deployment
```
terraform plan
```
## 4. Apply and Provision Infrastructure
```
terraform apply
```

## 📤 Outputs:
### - EC2 Public IP
### - EC2 Public DNS
### - EC2 Private IP


## 🌐 Region:
### AWS Region Used: us-east-1


## 📄 Notes:
### - Make sure your AWS CLI is configured with proper IAM permissions
### - Ensure you have a valid public key (terra-key.pub) for EC2 access
### - RDS password is generated securely using random_password
### - Some outputs will be printed after `terraform apply` for quick reference
