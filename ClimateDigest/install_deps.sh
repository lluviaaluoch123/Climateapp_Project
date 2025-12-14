#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_ROOT"

# Default python command (can be overridden by env var PYTHON_CMD)
PYTHON_CMD="${PYTHON_CMD:-python3}"
REQ_FILE="$PROJECT_ROOT/requirements.txt"
VENV_DIR="${1:-.venv}"

echo "Project root: $PROJECT_ROOT"

if [ -f "$REQ_FILE" ]; then
  echo "Found requirements.txt"
else
  if [ -d "$PROJECT_ROOT/myenv" ]; then
    if [ -x "$PROJECT_ROOT/myenv/Scripts/pip" ] || [ -x "$PROJECT_ROOT/myenv/Scripts/pip.exe" ]; then
      PIP="$PROJECT_ROOT/myenv/Scripts/pip"
    elif [ -x "$PROJECT_ROOT/myenv/bin/pip" ]; then
      PIP="$PROJECT_ROOT/myenv/bin/pip"
    else
      PIP=""
    fi

    if [ -n "$PIP" ]; then
      echo "Generating requirements.txt from existing venv at myenv"
      "$PIP" freeze > "$REQ_FILE"
    fi
  fi

  if [ ! -f "$REQ_FILE" ]; then
    echo "No requirements.txt found; generating from current Python environment"
    "$PYTHON_CMD" -m pip freeze > "$REQ_FILE" || { echo "pip freeze failed; please create requirements.txt manually."; exit 1; }
  fi
fi

echo "Using requirements: $REQ_FILE"

if [ ! -d "$VENV_DIR" ]; then
  echo "Creating virtual environment at $VENV_DIR using $PYTHON_CMD"
  "$PYTHON_CMD" -m venv "$VENV_DIR"
fi

if [ -f "$VENV_DIR/bin/activate" ]; then
  # POSIX-style venv activation
  # shellcheck disable=SC1090
  source "$VENV_DIR/bin/activate"
elif [ -f "$VENV_DIR/Scripts/activate" ]; then
  # Git Bash / MSYS / Windows bash activation
  # shellcheck disable=SC1090
  source "$VENV_DIR/Scripts/activate"
else
  echo "Could not find activation script in $VENV_DIR" >&2
  exit 1
fi

python -m pip install --upgrade pip
pip install -r "$REQ_FILE"

echo "Dependencies installed into $VENV_DIR"
echo "To activate: source $VENV_DIR/bin/activate  (or $VENV_DIR/Scripts/activate on Windows bash)"

exit 0
