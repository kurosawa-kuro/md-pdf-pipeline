from __future__ import annotations

import subprocess
from pathlib import Path

DEFAULT_FONT_FAMILY = "Noto Sans CJK JP"
CSS_PATH = Path(__file__).resolve().parent / "styles" / "print.css"


def _ensure_weasyprint():
    try:
        from weasyprint import CSS, HTML  # type: ignore
    except ImportError as exc:
        raise RuntimeError(
            "weasyprint is not installed. Run `make setup` first."
        ) from exc
    return HTML, CSS


def _ensure_font_available(font_family: str) -> None:
    try:
        result = subprocess.run(
            ["fc-match", font_family],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError as exc:
        raise RuntimeError(
            "fc-match is not available. Install fontconfig to validate fonts."
        ) from exc

    if result.returncode != 0:
        raise RuntimeError(f"Failed to check font availability for: {font_family}")

    stdout = result.stdout.strip()
    if not stdout:
        raise RuntimeError(f"No font match found for: {font_family}")

    if "DejaVu Sans" in stdout and font_family not in stdout:
        raise RuntimeError(
            f'Required font "{font_family}" is not installed. '
            "Install fonts-noto-cjk or run with --allow-missing-font."
        )


def _load_css(font_family: str):
    _, CSS = _ensure_weasyprint()
    if not CSS_PATH.exists():
        raise FileNotFoundError(f"PDF stylesheet not found: {CSS_PATH}")

    css_text = CSS_PATH.read_text(encoding="utf-8").replace(
        "__FONT_FAMILY__", font_family
    )
    return CSS(string=css_text)


def write_pdf(
    html: str,
    output_path: Path,
    base_path: Path,
    font_family: str = DEFAULT_FONT_FAMILY,
    strict_font: bool = True,
) -> None:
    HTML, _ = _ensure_weasyprint()

    if strict_font:
        _ensure_font_available(font_family)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    stylesheet = _load_css(font_family)
    HTML(string=html, base_url=str(base_path)).write_pdf(
        output_path, stylesheets=[stylesheet]
    )
