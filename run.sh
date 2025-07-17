#!/bin/bash

echo "Running main.py using uv-managed virtual environment..."

# Check and create venv if needed
if [ ! -x ".venv/bin/python" ]; then
  echo "📦 .venv not found. Creating..."
  uv venv || { echo "❌ uv venv 생성 실패"; exit 1; }
fi

PYTHON_PATH=".venv/bin/python"
MAIN_PATH="$(realpath main.py)"

"$PYTHON_PATH" "$MAIN_PATH"
