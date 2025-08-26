# GenAI Project

CLI calculator + an agent that can auto-fix bugs.

## Run
```bash
uv run calculator/main.py "3 + 7 * 2"
uv run main.py "fix the bug: 3 + 7 * 2 shouldn't be 20"

uv venv
uv pip install -r requirements.txt

