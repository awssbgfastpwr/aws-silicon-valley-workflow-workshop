# Participant Quickstart

Use this page before Session 01. It gives you the minimum setup needed to follow the workshop.

## Accounts

- GitHub account
- AWS account or workshop-provided AWS access, only when the mentors ask for it
- Groq API key, only if you want the optional roast feature in Session 04

Do not paste access keys, API keys, `.env` files, or screenshots of credentials into GitHub issues, pull requests, Discord, WhatsApp, or public chat.

## Local Tools

Install these before the first live session:

- Git
- VS Code or another code editor
- Python
- `uv` for Python project setup
- Docker, needed for the final deployment session
- AWS CLI, needed for cloud sessions

On Windows, use WSL with Ubuntu unless the workshop mentor gives a different setup.

## Clone the Repository

```bash
git clone https://github.com/awssbgfastpwr/aws-silicon-valley-workflow-workshop.git
cd aws-silicon-valley-workflow-workshop
```

Confirm Git can see the repo:

```bash
git status
```

Expected result:

```text
On branch main
```

Git may show extra lines. That is fine if it does not show a command error.

## Start the FastAPI Session

```bash
cd sessions/02-python-fastapi
uv sync
uv run fastapi dev main.py
```

Open:

```text
http://127.0.0.1:8000
```

## Start the Final Deployment App Locally

```bash
cd sessions/04-final-production-launch
python -m venv .venv
source .venv/bin/activate
pip install -e .
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open:

```text
http://127.0.0.1:8000
```

## Ask for Help

When you ask a mentor for help, include:

- your operating system
- the session folder
- the command you ran
- the full error output
- what you expected to happen

Do not include secrets or real credentials in screenshots.

