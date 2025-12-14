# ClimateDigest

This repository contains a Django project.

## Quick setup

1. Create a virtual environment (optional, recommended):

```bash
python -m venv .venv
```

2. Activate the environment:

- macOS / Linux / Git Bash:

```bash
source .venv/bin/activate
```

- Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

or use the helper script (creates a venv `.venv` by default):

```bash
bash install_deps.sh
```

If you encounter errors like "ModuleNotFoundError: No module named 'django'" or "ModuleNotFoundError: No module named 'PIL'", install the missing packages with:

```bash
pip install django pillow
```

4. Apply migrations and run the dev server (use the `manage.py` inside the `ClimateDigest` folder):

```bash
python ClimateDigest/manage.py makemigrations
python ClimateDigest/manage.py migrate
python ClimateDigest/manage.py runserver
```

## Notes

- `install_deps.sh` will attempt to generate `requirements.txt` from `myenv` if one is not present.
- If you prefer a different Python executable, set the `PYTHON_CMD` env var when running the script, e.g.:

```bash
PYTHON_CMD=python3.11 bash install_deps.sh
```
