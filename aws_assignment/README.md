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



