# AWS Serverless Thumbnail Generator

This is an AWS Serverless DevOps project that automatically processes and copies images uploaded to an Amazon S3 bucket to a destination bucket using an AWS Lambda trigger.

## 🛠️ Architecture & Services Used
* **Amazon S3**: Used for storing original images (`original-photos-ks`) and destination images (`thumbnali-photos`).
* **AWS Lambda**: Backend serverless compute service running Python (Boto3) code.
* **AWS IAM**: Configured execution roles with S3 permissions (`AmazonS3FullAccess`) for secure access.
* **CloudWatch Logs**: Used for monitoring, debugging, and tracking lambda function executions.

## 🚀 How It Works
1. A user uploads an image to the source S3 bucket (`original-photos-ks`).
2. S3 triggers an `ObjectCreated` event, invoking the Lambda function.
3. The Lambda function extracts the bucket name and object key, then copies the file to the destination bucket (`thumbnali-photos`) with a `thumbnail-` prefix.
