# Troubleshooting: Python, uv, and FastAPI

Use this guide during Session 02 when the local API does not run.

## `uv` Is Not Found

Check:

```bash
uv --version
```

If it fails, install `uv` from the official Astral instructions, then open a new terminal and run the version command again.

## Wrong Folder

Run FastAPI commands from the session folder:

```bash
cd sessions/02-python-fastapi
```

Confirm the files exist:

```bash
ls
```

You should see `main.py`, `pyproject.toml`, `students.json`, and `README.md`.

## Dependencies Are Missing

Run:

```bash
uv sync
```

Then start the app:

```bash
uv run fastapi dev main.py
```

## Port 8000 Is Already in Use

Use another port:

```bash
uv run uvicorn main:app --reload --port 8001
```

Open:

```text
http://127.0.0.1:8001
```

## `students.json` Errors

The demo API reads `students.json`. If the file is missing or broken, restore it from Git:

```bash
git checkout -- sessions/02-python-fastapi/students.json
```

Only run that command if you do not need local changes in the file.

## Quick API Test

With the app running, open another terminal:

```bash
curl http://127.0.0.1:8000/studentdata/1
```

You should receive one student record as JSON.

