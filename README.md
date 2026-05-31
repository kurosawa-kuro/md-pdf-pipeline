# md-pdf-pipeline

WSL 上で Markdown 原本から日本語 PDF を生成するためのローカル CLI パイプライン。
初期方針は `Python + WeasyPrint` を本命とし、Markdown を HTML 化して CSS 付きで PDF にレンダリングする。

## 目的

- Markdown を原本として管理する
- 日本語文字化けを避けつつ A4 PDF を安定生成する
- GUI 依存ではなく、CLI ベースで再現可能な変換経路を作る

## 現在の前提

- 対象環境: `WSL2 + Ubuntu + Python 3`
- 本命実装: `Python + WeasyPrint`
- 入力: 単一 Markdown
- 出力: 単一 PDF
- Google Drive 連携: 後回し

## 現在の構成

```text
.
├── AGENTS.md
├── CLAUDE.md
├── Makefile
├── README.md
├── env/
│   ├── config.yaml
│   └── secret.yaml
├── doc/
│   ├── 01_仕様と設計.md
│   ├── 02_移行ロードマップ.md
│   ├── 03_実装カタログ.md
│   ├── 04_運用.md
│   └── README.md
├── src/
│   ├── cli.py
│   ├── markdown_loader.py
│   ├── html_renderer.py
│   ├── pdf_renderer.py
│   ├── templates/
│   ├── styles/
│   └── examples/
└── out/
```

## コマンド

現在の主なコマンドは以下。

```bash
make setup    # Python 依存を導入
make build    # src/ を compileall で確認
make run      # sample.md から sample.pdf を生成
make test     # compileall + PDF 生成のスモークテスト
make lint     # py_compile による構文確認
```

`make run` と `make test` は、サンプル確認のため `--allow-missing-font` を付けたスモーク実行にしている。
本番想定の厳格なフォントチェックつき実行は次を使う。

```bash
python3 src/cli.py src/examples/sample.md
```

## ドキュメント

詳細は [`doc/`](doc/) を参照。権威順位と更新規約は [`doc/README.md`](doc/README.md) に従う。

- [`doc/01_仕様と設計.md`](doc/01_仕様と設計.md) — WSL + Python + WeasyPrint 前提の仕様と設計
- [`doc/02_移行ロードマップ.md`](doc/02_移行ロードマップ.md) — 実装順とやらないことを固定した決定的仕様
- [`doc/03_実装カタログ.md`](doc/03_実装カタログ.md) — 実装物の所在記録
- [`doc/04_運用.md`](doc/04_運用.md) — 環境構築、実行、運用手順

## 設定管理

- 非機密: `env/config.yaml`
- ローカル秘密情報: `env/secret.yaml`
- 共有・本番秘密情報: `doppler.yaml`

このプロジェクトは初期版では秘密情報をほぼ必要としない想定だが、`env/secret.yaml` はコミットしない。
