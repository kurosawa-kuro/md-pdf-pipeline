from __future__ import annotations

from pathlib import Path


def load_markdown(input_path: Path) -> tuple[str, Path]:
    if not input_path.exists():
        raise FileNotFoundError(f"Input Markdown file not found: {input_path}")
    if not input_path.is_file():
        raise ValueError(f"Input path is not a file: {input_path}")
    if input_path.suffix.lower() != ".md":
        raise ValueError(f"Input file must be a .md file: {input_path}")

    try:
        text = input_path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(
            f"Input Markdown must be UTF-8 encoded: {input_path}"
        ) from exc

    return text, input_path.parent
