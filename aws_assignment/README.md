# AWS Infrastructure Provisioning Assignment

This assignment demonstrates how to provision key AWS resources using AWS CLI , including EC2, S3, and VPC. The stretch goal also includes deploying a simple HelloWorld application using AWS Lambda via CloudFormation.

---

## 🚀 Tools Used

- **AWS CLI v2**
- **CloudFormation (YAML)**
- **Amazon EC2, S3, VPC, Lambda**

---

## Setup Instructions

### 1. Install AWS CLI

Download and install the AWS CLI MSI installer for Windows (64-bit):
```
https://awscli.amazonaws.com/AWSCLIV2.msi
```

Verify installation by opening a command prompt and running:
```
aws --version
```
### 2. Configure AWS IAM User

1. Navigate to AWS Console and search for IAM
2. Click on "Users" and "Create user"
3. Configure the user:
   - Name: awsCliUser
   - Enable console access
4. Assign the admin permission
5. Create the user

### 3. User access through AWS CLI
1. We need to take credential of this user
2. Click on user
3. Go to Security credential
4. Click on create access key
   - Click on Command Line Interface(CLI)
   - check the last check button
   - click on next
5. Access key and Secret key is generated, we can download it also by clicking on Download.csv file.

## ✅ Tasks Completed

### 1. Provisioning EC2 using AWS CLI

- Created a key pair (`my_ec2_key`)
- Selected a valid AMI ID compatible with `t2.micro` (free-tier eligible)
- Launched an EC2 instance using the command:

```bash
aws ec2 run-instances \
  --image-id ami-0c02fb55956c7d316 \
  --count 1 \
  --instance-type t2.micro \
  --key-name my_ec2_key \
  --security-group-ids sg-xxxxxxxxxxxxxxxxx \
  --subnet-id subnet-xxxxxxxxxxxxxxxxx

```
### 2. Creating an S3 Bucket via AWS CLI
```bash
aws s3api create-bucket --bucket my-assignment-bucket-123 --region us-east-1
```
### 3. Creating a Custom VPC via AWS CLI
```bash
aws ec2 create-vpc --cidr-block 10.0.0.0/16
```



