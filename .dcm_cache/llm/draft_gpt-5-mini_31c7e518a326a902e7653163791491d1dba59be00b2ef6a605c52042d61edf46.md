review_status: draft

id: md-pdf-pipeline-decision-catalog
domain: markdown-to-pdf pipeline (CLI / renderer)
confidence: medium
confidence_policy: capped_to_medium (freshness=fresh, catalog_items=9, distinct_evidence_artifacts=34)
evidence_freshness: high
coverage_confidence: high
meaning_quality: medium
high_end_ready: medium

# Decision Catalog (Draft)

fact_source: non_llm_scan
evidence_run_id: 20260705T043242Z_f0826d1bdc31
machine_provenance: docs/catalog/evidence/evidence_index.jsonl

## scan_summary

### overall_scan_and_metrics
- summary: スキャンは最新で、対象リポジトリにはテンプレート、CSS、Python スクリプト群、ドキュメントが含まれる。シンボル抽出は限定的でテスト検出は 0 件と報告されている（scan manifest の集計に基づく）。

### static_signals_summary
- summary: 静的サーチで job_lifecycle / auth_permission / env_secret に対応するヒットが観測されている（env_secret はパック内で redacted）。これらは静的シグナルであり、no-hit は不存在の証明ではない。

### extraction_coverage_notes
- summary: 公開 API・シンボル・エントリポイント・テストの自動抽出は限定的で、抽出器の制限（macro や動的生成の取りこぼし等）が収集結果の完全性に影響している。

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
- 事実: リポジトリに CLI/スクリプト実装 Python のエントリポイント風ファイル src/cli.py が存在する。
- 意味あい:
  - 役割: CLI / コマンド・エントリポイント候補
  - 含意: src/cli.py はコマンドライン操作を受け付ける実行可能スクリプトまたは CLI ラッパーの役割を持つ可能性が高い。
  - 含意: ユーザー入力（コマンド引数／フラグ）を介して Markdown→HTML→PDF などの処理フローをトリガする役割であることが想定される。
  - confidence: medium

### src/markdown_loader.py  {subject_kind: module}
- 事実: Markdown を読み込む処理を担うモジュール風のファイル src/markdown_loader.py が存在する。
- 意味あい:
  - 役割: 入力ロード（Markdown 読み込み）コンポーネント
  - 含意: src/markdown_loader.py は入力となる Markdown 文書の読み込み／前処理（ファイル IO、フロントマター解析等）を担う責務であることが示唆される。
  - 含意: パイプラインの入力段（ドキュメント取得）を提供するコンポーネントとして振る舞う。
  - confidence: high

### src/html_renderer.py  {subject_kind: module}
- 事実: HTML 出力を生成する役割のモジュール風ファイル src/html_renderer.py が存在する。
- 意味あい:
  - 役割: HTML レンダリング／変換コンポーネント
  - 含意: src/html_renderer.py は Markdown を HTML にレンダリングする段を担当する可能性が高い。
  - 含意: HTML を生成することで後続の PDF 変換コンポーネントにデータを渡す中間層として動くことが想定される。
  - confidence: high

### src/pdf_renderer.py  {subject_kind: module}
- 事実: PDF 生成を担当するモジュール風ファイル src/pdf_renderer.py が存在する。
- 意味あい:
  - 役割: PDF 出力（レンダラー）コンポーネント
  - 含意: src/pdf_renderer.py は HTML（または他の中間表現）から PDF を生成する最終出力段を担当すると見做せる。
  - 含意: PDF 生成時に CSS やテンプレートを参照する実装になっている可能性がある。
  - confidence: high

### src/templates/base.html  {subject_kind: file}
- 事実: HTML テンプレートファイル src/templates/base.html が存在する。
- 意味あい:
  - 役割: HTML テンプレート（表示レイアウト基盤）
  - 含意: base.html はレンダリング時のレイアウト／共通テンプレートとして使用され、HTML 出力の構造やスタイル適用の基盤となっている。
  - 含意: テンプレートの存在は HTML レンダラがテンプレート駆動であることを示す。
  - confidence: high

### src/styles/print.css  {subject_kind: file}
- 事実: プロジェクトにスタイルシート src/styles/print.css が含まれている。
- 意味あい:
  - 役割: レンダリング用スタイルシート
  - 含意: 印刷向けの CSS が含まれているため、HTML→PDF の変換過程で CSS を用いたレイアウト調整が行われる設計であることが示唆される。
  - 含意: PDF レンダリング結果の外観はこのスタイルシートに依存する部分がある。
  - confidence: high

### requirements.txt  {subject_kind: dependency}
- 事実: プロジェクトは依存関係リストとして requirements.txt を含む（Python パッケージ指定ファイル）。
- 意味あい:
  - 役割: 依存パッケージ宣言（runtime dependencies）
  - 含意: requirements.txt により、プロジェクトは Python 実行環境の依存ライブラリを明示している。
  - 含意: 依存関係はランタイムの振る舞いやセキュリティ特性（例: HTML→PDF 変換ライブラリの脆弱性）に影響する可能性がある。
  - confidence: high

### env/config.yaml  {subject_kind: file}
- 事実: env/config.yaml がリポジトリに含まれている（設定ファイルの配置）。
- 意味あい:
  - 役割: ランタイム設定ファイル
  - 含意: env/config.yaml は実行時の構成を格納する設定ファイルとして動作する可能性が高い。
  - 含意: 環境変数参照や秘密情報の代替手段として設定ファイルを利用する設計要素が存在することを示す。
  - confidence: medium

### README.md  {subject_kind: file}
- 事実: ドキュメントや README 等の Markdown ファイル（README.md, CLAUDE.md, AGENTS.md, doc/ 以下）が複数存在する。
- 意味あい:
  - 役割: ユーザー向けドキュメント（入力コンテンツの代表）
  - 含意: 複数のドキュメントがリポジトリに含まれており、ドキュメント自体がプロジェクトの変更対象となることがある（change signals が観測されている）。
  - 含意: この種のドキュメントは Markdown→PDF パイプラインの典型的な入力例である。
  - confidence: high

## evidence_appendix

### scan_manifest_and_file_tree
- summary: スキャンは最新で、ルートツリーに Python スクリプト、テンプレート、スタイル、ドキュメントが含まれている。スキャンメタ情報は main ブランチかつクリーンな状態で実行された。

### symbols_tests_entrypoints_summary
- summary: 静的シンボル抽出・テスト検出・エントリポイント抽出の結果は限定的で、明示的なシンボル一覧やテストケース、明確な Rust エントリポイントはこのスキャンで抽出されていない（ヒューリスティックな検出制限あり）。

### config_and_env_redaction
- summary: 環境変数参照は検出されておらず、env/config.yaml が存在する。一方で静的 grep による秘密情報シグナルはパック内で赤字化（redacted）されているため詳細は付与されていない。

### observed_change_signals
- summary: 複数のドキュメントファイルに対して変更シグナルが観測されており、ドキュメントがアクティブな変更面であることを示す記録が含まれる。

### dependency_inventory
- summary: 依存関係インベントリが提供されており、requirements.txt を起点とする Python 実行時依存の存在が示される（依存内容の詳細はこの要約に含めていない）。

### code_metrics_and_public_api
- summary: コードメトリクスや一部コード抜粋が収集されているが、公開 API 抽出は限定的であり、実装責務の完全把握には制限がある。

### decision_memory
- summary: 過去の Decision Catalog のメモリが含まれている。以前の判断痕跡が記録されている可能性がある。

### infra_evidence_summary
- summary: infra ドメインの明示的なリソース参照は限定的で、スキャンは infra を主要対象にしていない。infra 連携がある場合でもこのパックの範囲では限定的に観測されている。

### static_signal_inventory
- summary: 静的シグナルで job_lifecycle 1件、auth_permission 2件、env_secret 6件（赤字化）などが検出されているが、grep ベースのヒットは語彙依存であり no-hit は不存在の証明ではない。

### scan_limitations
- summary: 抽出器と探索には既知の制限があり（macro/動的生成/conditional compilation の取りこぼし等）、得られたインベントリは完全とは限らない点に留意する必要がある。
