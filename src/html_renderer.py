from __future__ import annotations

from pathlib import Path
from string import Template

import markdown

TEMPLATE_PATH = Path(__file__).resolve().parent / "templates" / "base.html"
MARKDOWN_EXTENSIONS = [
    "extra",
    "tables",
    "toc",
    "fenced_code",
]


def _load_template() -> Template:
    if not TEMPLATE_PATH.exists():
        raise FileNotFoundError(f"HTML template not found: {TEMPLATE_PATH}")
    return Template(TEMPLATE_PATH.read_text(encoding="utf-8"))


def render_document_html(markdown_text: str, document_title: str) -> str:
    body_html = markdown.markdown(markdown_text, extensions=MARKDOWN_EXTENSIONS)
    template = _load_template()
    return template.substitute(title=document_title, body=body_html)
