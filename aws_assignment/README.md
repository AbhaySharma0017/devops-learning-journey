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

### 4. Configure AWS CLI

Run the following command and enter your access key details:

```powershell
aws configure
```
```
Input:
-PS C:\Users\abhay.s> aws configure
-AWS Access Key ID [****************5SG4]: AKI*************Y4C
-AWS Secret Access Key [****************po9N]: C3P2d**********************la4YU
-Default region name [us-east-1]:
-Default output format [None]:
```

After running these command AWS CLI is successfully configure into my local machine.
## ✅ Tasks Completed

### 1. Provisioning EC2 using AWS CLI
```
PS C:\Users\abhay.s> aws ec2 run-instances --image-id=ami-084568db4383264d4 --instance-type=t2.micro --region=us-east-1
```

Describe all the instance which are available in your aws account.
```
aws ec2 describe-instances
```

### 2. Creating an S3 Bucket via AWS CLI
```bash
aws s3api create-bucket --bucket a4admin123 --region us-east-1
```
Command for list all the buckets
```
aws s3 ls
```
Command for delete the bucket
```
aws s3api delete-bucket --bucket "bucket_name"
```
### 3. Creating a Custom VPC via AWS CLI

```bash
 aws ec2 create-vpc --cidr-block 10.0.0.0/16 --tag-specifications "ResourceType=vpc,Tags=[{Key=Name,Value=MySimpleVPC}]"
```
## 🧩 Command Breakdown

| Part                                                     | Meaning                                                                                                                                    |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `aws ec2 create-vpc`                                     | Tells AWS CLI to create a VPC using the EC2 service.                                                                                       |
| `--cidr-block 10.0.0.0/16`                               | Specifies the IP address range of the VPC. This allows up to **65,536 IP addresses** (16-bit subnet mask).                                 |
| `--tag-specifications`                                   | Adds metadata tags to your VPC.                                                                                                            |
| `"ResourceType=vpc,Tags=[{Key=Name,Value=MySimpleVPC}]"` | Adds a tag to the VPC with:<br>**Key:** `Name`<br>**Value:** `MySimpleVPC`<br>This makes it easier to identify the VPC in the AWS Console. |

Command for describe all the vpc
```
 aws ec2 describe-vpcs
```

# 🚀 Deploy HelloWorld Lambda Using AWS CloudFormation (Console-Based)

This project demonstrates how to deploy a simple AWS Lambda function using **AWS CloudFormation via the AWS Console**. The Lambda function is packaged in a ZIP file, stored in an S3 bucket, and deployed using a CloudFormation YAML template.

---

## 📌 Objective

- Deploy a **HelloWorld Lambda function** using AWS CloudFormation.
- Package the Lambda function code in a `.zip` file.
- Upload the ZIP file to an **S3 bucket**.
- Create an **IAM role** for Lambda.
- Deploy everything using the **AWS Management Console** (no CLI used).

---

## 📁 Project Files

├── hello_world.py # Lambda function code
├── hello_world.zip # Zipped function code for deployment
├── aws_lambda.yaml # CloudFormation template

## 🪄 Steps Followed

### 1. Create Lambda Function Code

Created a Python file named `hello_world.py` with the following content:

```python
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
```
### 2. Zip the Code
Zipped the Python file as hello_world.zip:
 - Right-click on hello_world.py > Send to > Compressed (zipped) folder
 - Verified that the ZIP file is not empty and contains only hello_world.py

### 3. Upload ZIP to S3
-Open AWS Console > S3
-Created a new bucket  e.g., my-lambda-bucket
-Uploaded the hello_world.zip file into the bucket

### 4. Prepare CloudFormation Template
```AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyLambdaRole:
    Type: 'AWS::IAM::Role'
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - lambda.amazonaws.com
            Action:
              - 'sts:AssumeRole'
      Path: /
      Policies:
        - PolicyName: root
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action: 's3:*'
                Resource: '*'

  MyLambdaFunction:
    Type: 'AWS::Lambda::Function'
    Properties:
      Role: !GetAtt MyLambdaRole.Arn
      Runtime: python3.9
      Handler: hello_world.lambda_handler
      Code:
        S3Bucket: my-bucket-for-hello-world
        S3Key: hello_world.zip
      Tags:
        - Key: Name
          Value: MyLambdaFunction
```
### 5. Deploy via AWS Console
1. Go to AWS Console > CloudFormation
2. Click on Create Stack
3. Choose With new resources (standard)
4. Upload the aws_lambda.yaml file
5. Provide a stack name, e.g., MyStackForLambda
6. Acknowledge creation of IAM roles
7. Click Create Stack
8. Wait until stack status is CREATE_COMPLETE

### 6. Test the Lambda Function
1. Go to AWS Console > Lambda
2. Locate function: HelloWorldLambda
3. Click on Test
4. Create a simple test event and run it
5. Expected output:
   - {
  "statusCode": 200,
  "body": "Hello from Lambda!"
}
