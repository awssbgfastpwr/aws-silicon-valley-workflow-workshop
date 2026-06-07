# Workshop Roadmap

This roadmap shows how the AWS Silicon Valley Workflow workshop material fits together. Use it before a live cohort starts, and keep it updated when the workshop team changes the sequence.

## Audience

This workshop is for students who can use a computer but may be new to terminals, Git, Python APIs, Docker, or AWS.

## Public Safety Rule

This repository is public. Do not add real AWS credentials, `.env` files, real attendee sheets, private certificate keys, generated certificates, or generated manifests.

## Session Sequence

| Session | Folder | Outcome | Public Materials |
| --- | --- | --- | --- |
| 01 | `sessions/01-the-hacker-setup` | Students set up a terminal, Git, GitHub CLI, and a local repo workflow. | README and PDF references |
| 02 | `sessions/02-python-fastapi` | Students build and test a small FastAPI student API with local JSON persistence. | README, source code, task PDF, workshop PDF |
| 03 | `sessions/03-cloud-access` | Students learn AWS account access, IAM basics, billing awareness, and credential safety. | README and cloud access PDF |
| 04 | `sessions/04-final-production-launch` | Students package a FastAPI app into a Lambda container image and expose it with API Gateway. | README, Dockerfile, setup script, cleanup guide |
| Certificate workflow | `tools/certificate-generator` | Maintainers generate signed attendance certificates after the event. | Generator code, sample input, public docs |

The certificate generator defaults to `--sessions-total 5` because the event tracks five attendance slots. The public workshop repo currently contains four instructional session folders plus the post-event certificate workflow. If the team runs a fifth teaching session, add `sessions/05-...` and update this table.

## Recommended Live Flow

1. Start with `docs/participant-quickstart.md`.
2. Use the session README as the command sheet.
3. Use the PDF resources when students need the longer handout.
4. Use the troubleshooting docs during setup failures.
5. End AWS sessions with `sessions/04-final-production-launch/CLEANUP.md`.

## Maintainer Checklist Before Each Cohort

- Confirm all session links open from the root README.
- Run the FastAPI tests for sessions 02 and 04.
- Check that sample data contains fake names and fake emails only.
- Confirm `.gitignore` still excludes private keys, `.env` files, generated certificates, and generated manifests.
- Review AWS instructions for cost risk before publishing updated deployment commands.
- Keep old certificate public keys available in the verifier if certificates from earlier cohorts still need validation.

