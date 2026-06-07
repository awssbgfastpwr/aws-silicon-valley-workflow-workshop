# Troubleshooting: AWS, Docker, Lambda, and API Gateway

Use this guide during Session 04 when deployment fails.

## AWS CLI Is Not Configured

Check:

```bash
aws sts get-caller-identity
```

If it fails, configure the AWS CLI with the access method approved by the workshop team:

```bash
aws configure
```

Do not commit credentials or paste them into GitHub.

## Docker Is Not Running

Check:

```bash
docker info
```

If it fails on Linux:

```bash
sudo systemctl start docker
```

If Docker requires `sudo`, ask a mentor before changing groups on a lab machine.

## Docker Permission Error

Common error:

```text
permission denied while trying to connect to the Docker daemon socket
```

On your own Linux machine:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

Then run:

```bash
docker info
```

## ECR Login Fails

Confirm the region and identity:

```bash
aws sts get-caller-identity
aws configure get region
```

Use the same region for ECR, Lambda, and API Gateway during the session.

## Lambda Does Not Update

Wait for the previous update to finish:

```bash
aws lambda get-function-configuration \
  --function-name sentiment-api-fn \
  --query '[State,LastUpdateStatus]'
```

Deploy again after `LastUpdateStatus` is no longer `InProgress`.

## API Gateway Returns 403 or 500

Check that API Gateway can invoke Lambda:

```bash
aws lambda get-policy --function-name sentiment-api-fn
```

Check Lambda logs in CloudWatch if the API invokes Lambda but the app fails.

## Billing Safety

After the session, run the cleanup guide:

```text
sessions/04-final-production-launch/CLEANUP.md
```

Also check the AWS Billing dashboard before leaving the lab.

