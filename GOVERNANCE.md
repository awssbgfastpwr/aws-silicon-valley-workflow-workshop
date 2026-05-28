# Governance

This repository is maintained by AWS Cloud Club FAST Peshawar under the `awssbgfastpwr` GitHub organization.

The goal of governance is simple: keep the workshop accurate, safe for students, and maintainable by future club teams.

## Roles

### Club Lead and Executive Maintainer

Current Club Lead and Executive Maintainer: Rayyan Shaheer.

The Club Lead and Executive Maintainer role owns the public direction of this repository and coordinates with university or AWS Cloud Club stakeholders when needed.

Responsibilities:

- approve major repository direction changes
- make the final decision when maintainers disagree
- coordinate official workshop release timing
- handle private escalation paths for conduct, privacy, and event operations
- decide when maintainership should transfer to the next club team

### Technical Lead

The Technical Lead owns the technical quality of the workshop material.

Responsibilities:

- review major session changes
- approve AWS deployment and security guidance
- keep examples beginner-friendly and technically correct
- coordinate technical reviewers

### Technical Co-Leads

Technical Co-Leads help maintain session content and review pull requests.

Responsibilities:

- review docs and code changes
- test session instructions before workshops
- add troubleshooting notes from live sessions
- help contributors prepare safe pull requests

### Contributors

Contributors may be students, mentors, alumni, or workshop participants.

Responsibilities:

- follow [CONTRIBUTING.md](CONTRIBUTING.md)
- keep changes scoped
- protect secrets and student data
- respond to review feedback respectfully

## Decision Process

Small documentation fixes can be merged after one maintainer review.

Changes should get broader review when they affect:

- AWS account setup, IAM, billing, or deployment
- certificate signing or verification
- student data handling
- workshop sequence or learning outcomes
- repository governance or conduct rules

For major changes, the Technical Lead and Club Lead should both agree before merge. If there is a disagreement or an urgent club-level decision is needed, the Club Lead has final decision authority.

## Maintainer Access

Repository access should be limited to active club maintainers who need it.

The Club Lead is the primary owner for maintainer access decisions.

When club leadership changes:

- remove maintainers who no longer need write access
- add the incoming technical maintainers
- review branch protection and repository settings
- confirm secret scanning and Dependabot settings remain enabled

## Repository Safety

Maintainers should keep the repository public-safe by checking for:

- committed secrets
- real attendee files
- generated certificates
- private signing keys
- commands that may create unexpected AWS costs

Security-sensitive fixes should follow [SECURITY.md](SECURITY.md).
