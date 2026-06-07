# Instructor Guide

Use this guide to prepare a live cohort. It is safe for the public repo and does not contain private attendance data, credentials, or internal account details.

## Before the Workshop

- Review `docs/workshop-roadmap.md`.
- Confirm every mentor can clone the repository.
- Run the tests for sessions 02 and 04.
- Confirm the AWS account plan, region, and cleanup owner.
- Prepare a fallback demo if Docker, AWS, or classroom internet fails.
- Keep real attendee data outside this repository.

## During Session 01

Goal: students leave with a working terminal and Git workflow.

Watch for:

- students working inside the wrong WSL path
- missing Git identity
- SSH setup delays
- students pasting private tokens into chat

Use `docs/troubleshooting-wsl-git.md` for common fixes.

## During Session 02

Goal: students run and modify a FastAPI app.

Watch for:

- wrong working directory
- missing `uv`
- port conflicts
- broken `students.json`

Use `docs/troubleshooting-python-uv-fastapi.md` for common fixes.

## During Session 03

Goal: students understand access, IAM, billing awareness, and credential safety before deployment.

Watch for:

- screenshots that expose account IDs or credentials
- confusion between IAM users, roles, and policies
- students skipping budget checks

Treat credential safety as part of the lab, not an optional warning.

## During Session 04

Goal: students deploy the sentiment API with Lambda container images and API Gateway.

Watch for:

- Docker not running
- AWS CLI using the wrong account or region
- Lambda updates still in progress
- API Gateway invoke permissions missing

End the session with `sessions/04-final-production-launch/CLEANUP.md`.

## After the Workshop

- Remove cloud resources created for demos.
- Generate certificates from verified attendance data only.
- Keep private signing keys off GitHub.
- Add new troubleshooting notes while the problems are still fresh.
- Review open issues and assign follow-up owners.

