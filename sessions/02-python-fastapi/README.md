# Session 02: Python and FastAPI

Backend foundations using Python and FastAPI.

## Focus

- Python project structure
- FastAPI route design
- Pydantic request models
- JSON persistence for workshop demos
- Local API testing

## Run Locally

```bash
uv sync
uv run fastapi dev main.py
```

The sample API reads and writes `students.json` for demo purposes only.

## Lab Task

- Start the API.
- Fetch an existing student with `GET /studentdata/{id}`.
- Add a student with `POST /studentdata`.
- Delete a student with `DELETE /studentdata/{id}`.
- Restore `students.json` from Git if you want to reset the demo data.

## Done When

- The local server starts without errors.
- `GET /studentdata/1` returns JSON.
- A new student can be added and then deleted.

## Troubleshooting

- [Python, uv, and FastAPI troubleshooting](../../docs/troubleshooting-python-uv-fastapi.md)

## Resources

- [Session 2 Task](resources/session-2-task.pdf)
- [The Silicon Valley Workshop](resources/the-silicon-valley-workshop.pdf)
