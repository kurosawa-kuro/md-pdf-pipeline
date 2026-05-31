#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from html_renderer import render_document_html
from markdown_loader import load_markdown
from pdf_renderer import DEFAULT_FONT_FAMILY, write_pdf


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert a Markdown file into a styled PDF."
    )
    parser.add_argument("input_md", help="Path to the input Markdown file.")
    parser.add_argument(
        "-o",
        "--output",
        help="Output PDF path. Defaults to out/<input_stem>.pdf",
    )
    parser.add_argument(
        "--title",
        help="Optional document title. Defaults to the input file stem.",
    )
    parser.add_argument(
        "--font-family",
        default=DEFAULT_FONT_FAMILY,
        help=f'Preferred font family for PDF output. Default: "{DEFAULT_FONT_FAMILY}"',
    )
    parser.add_argument(
        "--allow-missing-font",
        action="store_true",
        help="Skip strict font availability checks and rely on system fallback fonts.",
    )
    return parser


def resolve_output_path(input_path: Path, output_arg: str | None) -> Path:
    if output_arg:
        output_path = Path(output_arg).expanduser()
    else:
        output_path = Path("out") / f"{input_path.stem}.pdf"

    if not output_path.is_absolute():
        output_path = Path.cwd() / output_path

    return output_path


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    input_path = Path(args.input_md).expanduser()
    if not input_path.is_absolute():
        input_path = Path.cwd() / input_path

    output_path = resolve_output_path(input_path, args.output)

    try:
        markdown_text, base_path = load_markdown(input_path)
        html = render_document_html(
            markdown_text=markdown_text,
            document_title=args.title or input_path.stem,
        )
        write_pdf(
            html=html,
            output_path=output_path,
            base_path=base_path,
            font_family=args.font_family,
            strict_font=not args.allow_missing_font,
        )
    except Exception as exc:  # noqa: BLE001
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
