# CLAUDE.md

このファイルは Claude Code が `md-pdf-pipeline` リポジトリで作業する際の補助ガイドである。

## リポジトリの前提

- このリポジトリは、WSL 上で Markdown から日本語 PDF を生成するローカル CLI パイプラインを扱う
- 初期本命は `Python + WeasyPrint`
- Google Drive 連携は初期スコープ外
- `src/` はこれから実装される前提で、`doc/02_移行ロードマップ.md` が初期構成と Phase を定義している

## コマンド

現在の主なコマンドは以下。

```bash
make setup
make build
make run
make dev
make test
make fmt
make lint
```

補足:

- `make run` / `make dev` / `make test` はサンプル入力に対するスモーク実行
- これらは `--allow-missing-font` を付けており、フォント未導入環境でも変換確認できる
- 厳格な日本語フォントチェックを含む実行は `python3 src/cli.py <input.md>` を使う

## ドキュメント優先順位

矛盾した場合は以下の順で扱う。

```text
doc/02_移行ロードマップ.md
> doc/01_仕様と設計.md
> README.md
```

更新規約の詳細は [`doc/README.md`](doc/README.md) を参照する。

## 作業ルール

- 推測で仕様を書かない。決まっていないことは明示する
- 仕様変更は `doc/01`、`doc/02`、必要に応じて `README.md` を同一変更で更新する
- `Python + WeasyPrint` を初期本命とし、代替案を勝手に本命へ切り替えない
- Google Drive 連携、GUI、複数ファイル一括変換など、`doc/02` でスコープ外としたものを先に広げない
- `src/cli.py` のデフォルトはフォント厳格チェックありである点を崩さない
- 非機密は `env/config.yaml`、ローカル秘密情報は `env/secret.yaml`、共有・本番秘密情報は Doppler（`doppler.yaml`）で管理する
