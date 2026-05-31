.PHONY: setup build run dev test fmt lint clean

# Application
APP_NAME := md-pdf-pipeline
PYTHON ?= python3
SRC_DIR := src
EXAMPLE_MD := $(SRC_DIR)/examples/sample.md
EXAMPLE_PDF := out/sample.pdf
SMOKE_FLAGS := --allow-missing-font

# 初期セットアップ (依存取得・ビルド)
setup: deps build
	@echo "Setup complete."

deps:
	$(PYTHON) -m pip install -r requirements.txt

# ビルド
build:
	$(PYTHON) -m compileall $(SRC_DIR)

# 実行
run:
	$(PYTHON) $(SRC_DIR)/cli.py $(EXAMPLE_MD) -o $(EXAMPLE_PDF) $(SMOKE_FLAGS)

# 開発 (ホットリロード)
dev:
	$(PYTHON) $(SRC_DIR)/cli.py $(EXAMPLE_MD) -o $(EXAMPLE_PDF) $(SMOKE_FLAGS)

# テスト
test:
	$(PYTHON) -m compileall $(SRC_DIR)
	$(PYTHON) $(SRC_DIR)/cli.py $(EXAMPLE_MD) -o $(EXAMPLE_PDF) $(SMOKE_FLAGS)

# 整形
fmt:
	@echo "No formatter configured yet."

# 静的解析
lint:
	$(PYTHON) -m py_compile $(SRC_DIR)/*.py

# クリーンアップ
clean:
	rm -rf out __pycache__ $(SRC_DIR)/__pycache__
