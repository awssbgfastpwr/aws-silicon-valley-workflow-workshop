# Contributing Guide

Thank you for helping improve the AWS Silicon Valley Workflow workshop repository.

This repo is maintained by AWS Cloud Club FAST Peshawar under the `awssbgfastpwr` GitHub organization. Contributions should help students learn, keep workshop material accurate, and protect participant privacy.

## Who Can Contribute

Contributions are welcome from:

- current AWS Cloud Club FAST Peshawar team members
- workshop mentors and volunteers
- FAST Peshawar students
- alumni helping maintain workshop material
- participants who find mistakes or want to improve explanations

## Good First Contributions

- fix typos or unclear instructions in session READMEs
- improve setup steps for Windows, WSL, Linux, or macOS
- add missing troubleshooting notes from workshop sessions
- improve FastAPI examples without making them harder for beginners
- improve AWS safety guidance
- update certificate generator docs or examples

## Contribution Rules

Before opening a pull request:

- do not commit secrets, tokens, `.env` files, AWS credentials, private keys, or attendee data
- do not commit generated certificates, manifests, or real participant spreadsheets
- keep examples beginner-friendly and workshop-focused
- prefer clear explanations over clever abstractions
- keep changes scoped to one topic per pull request
- follow the existing folder structure unless a maintainer agrees to a larger reorganization

## Branch and Pull Request Flow

1. Fork the repository or create a branch from `main`.
2. Use a short branch name, such as `docs/session-02-setup` or `fix/certificate-paths`.
3. Make the smallest useful change.
4. Run any relevant local checks.
5. Open a pull request using the provided template.
6. Wait for review from the technical team or club maintainers.

## Commit Style

Use clear commit messages:

```text
docs: add cloud access troubleshooting notes
fix: correct FastAPI run command
chore: update certificate example input
```

Common prefixes:

- `docs:` for documentation
- `fix:` for corrections
- `feat:` for new workshop material or examples
- `chore:` for maintenance
- `security:` for safety-related changes

## Local Checks

Run the repository checks before opening a pull request:

```bash
python3 tools/check_markdown_links.py
python3 tools/check_public_safety.py
```

For documentation-only changes, preview the Markdown and check links.

For `sessions/02-python-fastapi`:

```bash
cd sessions/02-python-fastapi
uv sync
uv run fastapi dev main.py
```

For `sessions/04-final-production-launch`:

```bash
cd sessions/04-final-production-launch
python -m venv .venv
source .venv/bin/activate
pip install -e .
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

For the certificate generator:

```bash
cd tools/certificate-generator
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/generate_certificates.py \
  --input examples/attendees-example.csv \
  --verify-base-url https://example.com/verify
```

Generated outputs should stay uncommitted.

## Documentation Style

Write for students who may be using a terminal, Git, Python, or AWS for the first time.

- use direct steps and copy-pasteable commands
- explain why a risky command is needed
- include expected output when it helps students confirm progress
- call out billing, credential, and privacy risks clearly
- avoid unexplained abbreviations

## Review Expectations

Maintainers may request changes for:

- inaccurate AWS guidance
- commands that create billing or security risk
- examples that expose secrets or real student data
- changes that make beginner sessions harder to follow
- docs that conflict with the workshop sequence

Two maintainer approvals are preferred for major session, AWS, security, or certificate workflow changes. Small typo fixes can be merged by one maintainer. For club-level direction, maintainer access, public releases, or disputed changes, the Club Lead has final approval.
