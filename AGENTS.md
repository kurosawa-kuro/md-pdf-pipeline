# AGENTS.md

AI コーディングエージェント共通の作業ガイド。
ツール固有の補足は各ファイルに分離し、ここではこのリポジトリで共通に守る方針のみを記す。

## プロジェクト概要

- 目的: WSL 上で Markdown 原本から日本語 PDF を生成するローカル CLI パイプラインを作る
- 対象: `Python + WeasyPrint` を本命とした Markdown → HTML → PDF 変換
- 現状: `doc/01` と `doc/02` で仕様は具体化済み、`src/` はこれから実装する段階

## 基本方針

- Markdown を唯一の原本とする
- 初期版は単一 Markdown 入力、単一 PDF 出力に絞る
- CLI を canonical とし、GUI 依存運用を作らない
- Google Drive 連携は後回しにする

## 権威順位

```text
doc/02_移行ロードマップ.md
> doc/01_仕様と設計.md
> README.md
```

補助的な運用ルールは [`doc/README.md`](doc/README.md) を参照する。

## 更新ルール

- スコープや採否の変更は `doc/02_移行ロードマップ.md` を先に直し、その後 `doc/01_仕様と設計.md` と `README.md` を合わせる
- 実装物や構成変更は `doc/03_実装カタログ.md` を更新する
- 実行手順や環境構築の変更は `doc/04_運用.md` と `Makefile` を更新する
- 関連ドキュメントは同一変更でそろえる

## 作業上の注意

- `Makefile` はまだひな形であり、存在だけでコマンド成立を前提にしない
- `Python + WeasyPrint` を初期本命とし、Pandoc などの代替案は勝手に主軸へ切り替えない
- 非機密は `env/config.yaml`、ローカル秘密情報は `env/secret.yaml`、共有・本番秘密情報は Doppler（`doppler.yaml`）で管理する
- 秘密情報はコミットしない
