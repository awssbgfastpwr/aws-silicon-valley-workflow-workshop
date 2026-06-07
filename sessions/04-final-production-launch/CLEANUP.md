# Cleanup Guide

Run this after Session 04 if you created AWS resources for the deployment lab. Cleanup prevents surprise charges and keeps the account tidy.

Use the same AWS account and region you used during deployment.

## Confirm Your Identity

```bash
aws sts get-caller-identity
```

Confirm the account is the one you used for the workshop.

Set the same names used during deployment:

```bash
AWS_REGION=eu-north-1
ECR_REPO=sentiment-api
LAMBDA_FUNCTION=sentiment-api-fn
IAM_ROLE_NAME=sentiment-api-lambda-role
API_NAME=sentiment-api-http
```

Change these values if you used different names.

## Delete API Gateway

Find the API ID:

```bash
API_ID=$(aws apigatewayv2 get-apis \
  --region "$AWS_REGION" \
  --query "Items[?Name=='$API_NAME'].ApiId | [0]" \
  --output text)
echo "$API_ID"
```

Delete it if the output is not `None`:

```bash
aws apigatewayv2 delete-api \
  --api-id "$API_ID" \
  --region "$AWS_REGION"
```

## Delete Lambda

```bash
aws lambda delete-function \
  --function-name "$LAMBDA_FUNCTION" \
  --region "$AWS_REGION"
```

## Delete ECR Images and Repository

This deletes the repository and all images inside it:

```bash
aws ecr delete-repository \
  --repository-name "$ECR_REPO" \
  --force \
  --region "$AWS_REGION"
```

## Delete IAM Role

Detach the basic Lambda policy:

```bash
aws iam detach-role-policy \
  --role-name "$IAM_ROLE_NAME" \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

Delete the role:

```bash
aws iam delete-role --role-name "$IAM_ROLE_NAME"
```

## Check CloudWatch Logs

Lambda log groups may remain after deleting the function.

```bash
aws logs describe-log-groups \
  --log-group-name-prefix "/aws/lambda/$LAMBDA_FUNCTION" \
  --region "$AWS_REGION"
```

Delete the log group if you no longer need it:

```bash
aws logs delete-log-group \
  --log-group-name "/aws/lambda/$LAMBDA_FUNCTION" \
  --region "$AWS_REGION"
```

## Final Billing Check

Open the AWS Billing dashboard and check:

- current month charges
- active budgets
- ECR storage
- Lambda usage
- CloudWatch log storage
- API Gateway usage

Ask a mentor before deleting resources from an account shared with other students.

