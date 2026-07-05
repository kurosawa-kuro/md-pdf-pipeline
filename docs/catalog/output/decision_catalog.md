review_status: adopted
id: md-pdf-pipeline-decision-catalog
domain: markdown-to-pdf pipeline (CLI / renderer)
confidence: medium

# Decision Catalog

fact_source: non_llm_scan
evidence_run_id: 20260705T043242Z_f0826d1bdc31
machine_provenance: docs/catalog/evidence/evidence_index.jsonl

purpose: upper_model_input
catalog_id: md-pdf-pipeline-decision-catalog
domain: markdown-to-pdf pipeline (CLI / renderer)
high_end_ready: medium

## repo_topology

- kind: rust_cli_application
- core_files:
  - path: src/cli.py
    role: cli_parse_and_dispatch
    catalog_status: core
  - path: src/examples/sample.md
    role: low_signal_or_appendix
    catalog_status: low_signal_or_appendix
  - path: src/html_renderer.py
    role: HTML_レンダリング／変換コンポーネント
    catalog_status: core
  - path: src/markdown_loader.py
    role: 入力ロード（Markdown_読み込み）コンポーネント
    catalog_status: core
  - path: src/pdf_renderer.py
    role: PDF_出力（レンダラー）コンポーネント
    catalog_status: core
  - path: src/styles/print.css
    role: レンダリング用スタイルシート
    catalog_status: core
  - path: src/templates/base.html
    role: HTML_テンプレート（表示レイアウト基盤）
    catalog_status: core
- runtime_surfaces:
  - unknown_invocation_surface
- data_surfaces:
  - Store file read/write/remove/clear/flush

## coverage_map

- scan_included_files: 20
- topology_files: 7
- catalog_core_items: 9
- covered_as_core:
  - src/cli.py
  - src/markdown_loader.py
  - src/html_renderer.py
  - src/pdf_renderer.py
  - src/templates/base.html
  - src/styles/print.css
  - env/config.yaml
  - README.md
- covered_as_appendix:
  - requirements.txt
  - src/examples/sample.md
- omitted_or_low_signal:
  - reason: generated/vendor/test fixture/low-signal or scan metadata only

## scan_summary

- profile: rust
- profile_resolution: requested=rust detected=css,html,infra,python profiles_run=rust language=rust
- scan_included_files: 20
- symbols: 0
- entrypoints: 0
- tests_detected: 0
- no_hit_is_not_absence: true

## flow_items

### Observed Primary Flow Candidate: Markdown → HTML → PDF pipeline  {subject_kind: evidence_inferred_flow}
- id: primary_task_lifecycle_candidate
- flow_type: primary_candidate
- grounding_level: weak
- basis:
  - src/markdown_loader.py
  - src/html_renderer.py
  - src/pdf_renderer.py
  - src/templates/base.html
- steps:
  - order: 1
    user_intent: 処理対象となる Markdown ドキュメントをパイプラインへ投入する
    surface: candidate load operation
    components: src/markdown_loader.py, README.md, doc/01_仕様と設計.md
    data_effect: Markdown ファイルを読み込み、内部表現（プレーン HTML 等）へ変換する入力データを生成する
    confidence: weak
  - order: 2
    user_intent: 読み込んだ Markdown を印刷・配布可能な HTML に変換する
    surface: candidate render-to-html operation
    components: src/html_renderer.py, src/templates/base.html, src/styles/print.css
    data_effect: Markdown の内容をテンプレートとスタイルを使って HTML にレンダリングする中間出力を生成する
    confidence: weak
  - order: 3
    user_intent: HTML を PDF に変換し、配布・印刷可能な成果物を得る
    surface: candidate render-to-pdf operation
    components: src/pdf_renderer.py, src/styles/print.css, src/templates/base.html
    data_effect: 生成された HTML を元に PDF を出力する最終生成物を作成する（ファイル化）
    confidence: weak
- cannot_conclude:
  - このフローが実際に CLI を介してシーケンシャルに呼び出されることおよび具体的な関数／コマンド名は、静的シンボル抽出／コールグラフの証拠が不足しているため断定できない（call graph 非在／シンボル検出制限）。
  - コマンドラインのサブコマンド名や引数仕様はスキャンで明示的に抽出されていないため、表層的な 'candidate' 表現に留めている。

### Observed Flow Candidate: Configuration / runtime initialization  {subject_kind: evidence_inferred_flow}
- id: configuration_and_runtime_initialization_candidate
- flow_type: config
- grounding_level: medium
- basis:
  - src/cli.py
  - env/config.yaml
  - requirements.txt
- steps:
  - order: 1
    user_intent: 実行環境に応じた設定値を読み取りパイプラインのパラメータを確定する
    surface: candidate configuration load
    components: env/config.yaml, src/cli.py
    data_effect: 実行時設定を読み込み、処理挙動（出力ディレクトリ、テンプレート選択等）に影響を与える構成値を初期化する
    confidence: medium
- cannot_conclude:
  - 設定ファイルや環境変数からランタイム設定が注入されるか、CLI が直接それらを参照するかの細部は検出証拠では断定できない（env 抽出は限定的／赤字化のため内容不明）。

### Observed Destructive Surface Candidate: candidate clear operation (output cleanup)  {subject_kind: evidence_inferred_flow}
- id: clear_all_surface_candidate
- flow_type: destructive_surface_candidate
- grounding_level: weak
- basis:
  - src/pdf_renderer.py
  - src/styles/print.css
- steps:
  - order: 1
    user_intent: 出力フォルダや一時ファイルを消去して状態をリセットする（候補的操作）
    surface: candidate clear operation
    components: src/cli.py, src/pdf_renderer.py
    data_effect: 生成済み出力ファイルや一時ファイルを削除する可能性のあるクリーンアップ操作（候補）
    confidence: weak
- cannot_conclude:
  - 明示的な 'clear all' や削除を行う CLI サブコマンドの証拠は無く、このフローを削除系の主要面と結び付ける確証はない。
  - もし一括削除やクリーン操作の表層が存在する場合、その実名や引数仕様は不明である。

## catalog_items

### src/cli.py  {subject_kind: file}
- role: CLI / コマンド・エントリポイント候補
- implications:
  - src/cli.py はコマンドライン操作を受け付ける実行可能スクリプトまたは CLI ラッパーの役割を持つ可能性が高い。
  - ユーザー入力（コマンド引数／フラグ）を介して Markdown→HTML→PDF などの処理フローをトリガする役割であることが想定される。

### src/markdown_loader.py  {subject_kind: module}
- role: 入力ロード（Markdown 読み込み）コンポーネント
- implications:
  - src/markdown_loader.py は入力となる Markdown 文書の読み込み／前処理（ファイル IO、フロントマター解析等）を担う責務であることが示唆される。
  - パイプラインの入力段（ドキュメント取得）を提供するコンポーネントとして振る舞う。

### src/html_renderer.py  {subject_kind: module}
- role: HTML レンダリング／変換コンポーネント
- implications:
  - src/html_renderer.py は Markdown を HTML にレンダリングする段を担当する可能性が高い。
  - HTML を生成することで後続の PDF 変換コンポーネントにデータを渡す中間層として動くことが想定される。

### src/pdf_renderer.py  {subject_kind: module}
- role: PDF 出力（レンダラー）コンポーネント
- implications:
  - src/pdf_renderer.py は HTML（または他の中間表現）から PDF を生成する最終出力段を担当すると見做せる。
  - PDF 生成時に CSS やテンプレートを参照する実装になっている可能性がある。

### src/templates/base.html  {subject_kind: file}
- role: HTML テンプレート（表示レイアウト基盤）
- implications:
  - base.html はレンダリング時のレイアウト／共通テンプレートとして使用され、HTML 出力の構造やスタイル適用の基盤となっている。
  - テンプレートの存在は HTML レンダラがテンプレート駆動であることを示す。

### src/styles/print.css  {subject_kind: file}
- role: レンダリング用スタイルシート
- implications:
  - 印刷向けの CSS が含まれているため、HTML→PDF の変換過程で CSS を用いたレイアウト調整が行われる設計であることが示唆される。
  - PDF レンダリング結果の外観はこのスタイルシートに依存する部分がある。

### requirements.txt  {subject_kind: dependency}
- role: 依存パッケージ宣言（runtime dependencies）
- implications:
  - requirements.txt により、プロジェクトは Python 実行環境の依存ライブラリを明示している。
  - 依存関係はランタイムの振る舞いやセキュリティ特性（例: HTML→PDF 変換ライブラリの脆弱性）に影響する可能性がある。

### env/config.yaml  {subject_kind: file}
- role: ランタイム設定ファイル
- implications:
  - env/config.yaml は実行時の構成を格納する設定ファイルとして動作する可能性が高い。
  - 環境変数参照や秘密情報の代替手段として設定ファイルを利用する設計要素が存在することを示す。

### README.md  {subject_kind: file}
- role: ユーザー向けドキュメント（入力コンテンツの代表）
- implications:
  - 複数のドキュメントがリポジトリに含まれており、ドキュメント自体がプロジェクトの変更対象となることがある（change signals が観測されている）。
  - この種のドキュメントは Markdown→PDF パイプラインの典型的な入力例である。

## evidence_appendix

- pointer: docs/catalog/evidence/evidence_index.jsonl
- pointer: docs/catalog/evidence/current_run_id
