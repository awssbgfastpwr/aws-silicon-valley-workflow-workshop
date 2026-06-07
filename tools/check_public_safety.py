from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".certificate_keys",
    "outputs",
    "generated_certificates",
    "generated_certificates_check",
}
ALLOWED_FILENAMES = {".env.example"}
FORBIDDEN_FILENAMES = {
    ".env",
    "private_key.pem",
    "manifest.csv",
    "manifest.json",
    "all_certificates.pdf",
}
SECRET_PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"ASIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"aws_secret_access_key\s*=\s*[^\s]+", re.IGNORECASE),
    re.compile(r"aws_session_token\s*=\s*[^\s]+", re.IGNORECASE),
    re.compile(r"GROQ_API_KEY\s*=\s*[A-Za-z0-9_\-]{12,}"),
]
BINARY_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg", ".gif", ".ico", ".zip"}


def candidate_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        if path.is_file():
            files.append(path)
    return files


def main() -> int:
    failures: list[str] = []
    for path in candidate_files():
        rel = path.relative_to(ROOT)
        name = path.name

        if name in FORBIDDEN_FILENAMES and name not in ALLOWED_FILENAMES:
            failures.append(f"{rel}: forbidden public filename")

        if path.suffix.lower() in BINARY_EXTENSIONS:
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                failures.append(f"{rel}: matched secret pattern {pattern.pattern}")

    if failures:
        print("Public safety check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Public safety check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

