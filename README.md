# AWS Silicon Valley Workflow Workshop

Official workshop repository for the AWS Silicon Valley Workflow series hosted by AWS Cloud Club FAST Peshawar.

This repository lives under the `awssbgfastpwr` university club organization. It is maintained as a public learning resource for students, club volunteers, technical leads, and workshop participants.

## What This Repository Contains

- session material for the AWS Silicon Valley Workflow workshop series
- PDF handouts, task sheets, and reference material linked from each session
- Python and FastAPI examples for backend development sessions
- AWS access and deployment guidance for hands-on cloud sessions
- a Lambda container deployment example for the final production launch
- certificate generation tooling for signed QR-verified attendance certificates
- club contribution, support, security, and governance documentation

## Repository Structure

```text
.
├── sessions/
│   ├── 01-the-hacker-setup/
│   ├── 02-python-fastapi/
│   ├── 03-cloud-access/
│   └── 04-final-production-launch/
├── tools/
│   └── certificate-generator/
├── docs/
├── .github/
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── GOVERNANCE.md
├── SECURITY.md
├── SUPPORT.md
└── README.md
```

## Sessions

| Folder | Focus |
| --- | --- |
| `sessions/01-the-hacker-setup` | Linux terminal, WSL, Git, and GitHub CLI setup |
| `sessions/02-python-fastapi` | Python backend foundations and FastAPI APIs |
| `sessions/03-cloud-access` | AWS access, IAM, billing safety, and cloud setup |
| `sessions/04-final-production-launch` | Docker, Lambda container deployment, API Gateway, and production launch |

Start with the session folder assigned by the workshop team. Each session has its own README with the setup steps and commands for that part of the workshop.

Session PDFs and handouts live in each session's `resources/` folder and are linked from that session README.

## Workshop Guides

- [Workshop roadmap](docs/workshop-roadmap.md) - session sequence, outcomes, and maintainer checks
- [Participant quickstart](docs/participant-quickstart.md) - setup steps before the first session
- [Instructor guide](docs/instructor-guide.md) - public-safe live session notes for mentors
- [WSL, Git, and GitHub troubleshooting](docs/troubleshooting-wsl-git.md)
- [Python, uv, and FastAPI troubleshooting](docs/troubleshooting-python-uv-fastapi.md)
- [AWS, Docker, Lambda, and API Gateway troubleshooting](docs/troubleshooting-aws-docker-lambda.md)
- [Certificate verification notes](docs/certificate-verification.md)

## Quick Start

Clone the repository:

```bash
git clone https://github.com/awssbgfastpwr/aws-silicon-valley-workflow-workshop.git
cd aws-silicon-valley-workflow-workshop
```

For the FastAPI session:

```bash
cd sessions/02-python-fastapi
uv sync
uv run fastapi dev main.py
```

For the final deployment session:

```bash
cd sessions/04-final-production-launch
python -m venv .venv
source .venv/bin/activate
pip install -e .
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

For certificate generation:

```bash
cd tools/certificate-generator
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

See [tools/certificate-generator/README.md](tools/certificate-generator/README.md) for the full certificate workflow.

## Community Docs

This repository includes the standard club docs needed for public collaboration:

- [CONTRIBUTING.md](CONTRIBUTING.md) - how students and volunteers should contribute
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - expected behavior for club spaces and repository work
- [GOVERNANCE.md](GOVERNANCE.md) - maintainer roles and decision process
- [SECURITY.md](SECURITY.md) - how to report leaked secrets or security issues
- [SUPPORT.md](SUPPORT.md) - where to ask for help
- [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md) - pull request checklist
- [.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE/) - issue templates for bugs and workshop content updates

## Public Repository Safety

This repository is intended to stay public. Never commit:

- AWS access keys, secret keys, session tokens, or downloaded credential files
- `.env` files or private API keys
- real attendee spreadsheets
- generated certificate outputs
- `.certificate_keys/`
- private signing keys
- local virtual environments and caches

Use [docs/participant-quickstart.md](docs/participant-quickstart.md) and [docs/workshop-roadmap.md](docs/workshop-roadmap.md) when onboarding new students. Use [sessions/04-final-production-launch/CLEANUP.md](sessions/04-final-production-launch/CLEANUP.md) after AWS deployment labs.

If a secret is committed, revoke or rotate it first, then report it using [SECURITY.md](SECURITY.md).

## Certificate Generator

The certificate workflow lives in:

```text
tools/certificate-generator/
```

It generates signed attendance certificates from CSV or XLSX input and exports PDFs, PNGs, manifests, and a public verifier key. Private signing keys and generated outputs are ignored by Git.

This certificate generator is specific to the AWS Silicon Valley Workflow event. For future events, the club should create a separate generic event certificate-maker repository instead of treating this folder as the long-term reusable certificate system.

The generator is not useful for producing official club certificates without the club's private signing key. Students and contributors can still study the workflow and generate learning certificates with their own private key.

## Leadership

- Club Lead and Executive Maintainer: Rayyan Shaheer
- Technical Lead: Raqeeb
- Technical Co-Leads: Abdul Kalam, Muhammad Taha, Hisam Mehboob

The Club Lead holds final authority for repository direction, maintainer access, public releases, and club-level decisions for this workshop.

## Repository

```text
awssbgfastpwr/aws-silicon-valley-workflow-workshop
```

## License

No license file is currently included. Do not reuse this repository outside the workshop or club context until the maintainers add an explicit license.
