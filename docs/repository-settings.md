# Repository Settings

Use this when maintaining the GitHub repository profile for the AWS Cloud Club FAST Peshawar workshop repository.

## Canonical Repository

```text
Organization: awssbgfastpwr
Repository: aws-silicon-valley-workflow-workshop
URL: https://github.com/awssbgfastpwr/aws-silicon-valley-workflow-workshop
```

Primary repository owner: Rayyan Shaheer, Club Lead and Executive Maintainer.

## Description

Recommended GitHub description:

```text
Workshop assets and QR-verified certificate automation for AWS Silicon Valley Workflow at FAST Peshawar.
```

Longer option:

```text
Certificate automation and workshop assets for AWS Silicon Valley Workflow at FAST Peshawar, including signed QR-verified attendance certificates.
```

## Suggested Topics

```text
aws
aws-cloud-club
fast-peshawar
silicon-valley-workflow
workshop
fastapi
lambda
api-gateway
certificates
qr-code
ed25519
python
```

## Suggested Repository Features

Enable:

- Issues
- Pull requests
- Secret scanning
- Push protection
- Dependabot alerts
- Dependabot security updates

Optional:

- Discussions, if the club wants public Q&A outside issues
- Projects, if the team tracks workshop prep work on GitHub

Disable or avoid:

- Wiki, unless the club has a maintainer assigned to keep it current
- public uploads of attendee sheets, generated certificates, or private keys

## Branch Protection

Recommended protection for `main`:

- require pull requests before merging
- require conversation resolution before merging
- block force pushes
- block branch deletion
- limit direct pushes to active maintainers only
- require status checks once automated checks exist

The Club Lead should retain final approval over maintainer access, branch protection changes, and public repository settings.

## Public Safety Checklist

Before making the repository public or after major workshop updates, confirm that these are not present in Git:

- AWS access keys, secret keys, or session tokens
- `.env` files
- private signing keys
- real attendee spreadsheets
- generated certificates
- generated manifests containing private participant data
- local virtual environments or caches

## Historical Rename Note

If old event material points to a previous repository name, update official posters, slides, forms, and announcements to use the canonical URL above. GitHub usually redirects old repository URLs, but workshop material should use the current name.
