# Troubleshooting: WSL, Git, and GitHub

Use this guide during Session 01 when terminal, Git, or GitHub setup fails.

## `git` Is Not Found

Check:

```bash
git --version
```

If the command fails on Ubuntu or WSL:

```bash
sudo apt update
sudo apt install git
```

Run `git --version` again.

## Git Cannot Identify You

Set your public commit name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Use the email you want attached to public commits. Do not use a private email if you do not want it visible on GitHub.

## Clone Fails With Permission Denied

If you use HTTPS, clone with:

```bash
git clone https://github.com/awssbgfastpwr/aws-silicon-valley-workflow-workshop.git
```

If you use SSH, confirm your key is loaded and added to GitHub:

```bash
ssh -T git@github.com
```

Expected result includes your GitHub username. GitHub may say shell access is not provided. That is normal.

## WSL Cannot See Your Project

Keep workshop code inside the Linux filesystem when using WSL:

```bash
cd ~
mkdir -p code
cd code
```

Avoid running Python projects from `/mnt/c/...` during the workshop. File watching and permissions are less reliable there.

## Line Ending Warnings

If Git warns about LF or CRLF, continue unless the mentor asks you to change it. The repo is text-heavy, and Git can normalize line endings.

## Before You Push

Run:

```bash
git status
```

Do not push:

- `.env` files
- AWS credentials
- private keys
- generated certificates
- real attendee sheets

