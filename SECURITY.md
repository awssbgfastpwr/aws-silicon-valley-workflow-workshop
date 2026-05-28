# Security Policy

This is a public university club repository. Security reports are taken seriously because the repo includes AWS workshop guidance and certificate generation tooling.

## Do Not Report Secrets Publicly

Do not open a public GitHub issue for:

- leaked AWS access keys or session tokens
- private certificate signing keys
- API keys
- `.env` files
- real attendee spreadsheets
- student personal data
- vulnerabilities that could expose private data

Use the official AWS Cloud Club FAST Peshawar maintainer or leadership channel instead.

## What To Report

Report security issues such as:

- committed secrets or private keys
- instructions that could expose student AWS accounts
- unsafe IAM guidance
- certificate signing or verification weaknesses
- accidental publication of attendee data
- dependency or deployment issues that create real risk

## If You Accidentally Commit a Secret

1. Revoke or rotate the secret immediately.
2. Remove the secret from the working branch.
3. Contact the maintainers through the official club leadership channel.
4. Do not rely on deleting the file from a later commit. Git history may still contain the secret.

## Public Repository Rules

Never commit:

- AWS access keys, secret keys, or session tokens
- `.env` files
- private keys under `.certificate_keys/`
- generated certificate outputs
- real attendee spreadsheets
- private student data

## Maintainer Response

Maintainers should:

- acknowledge reports as soon as practical
- assess whether credentials, attendee data, or certificate trust are affected
- rotate affected keys before discussing technical details publicly
- remove or invalidate exposed generated artifacts where possible
- document public remediation only after sensitive details are safe
