import subprocess
import os

main_path = os.path.abspath("main.py")
subprocess.run(f"uv venv exec python {main_path}", shell=True)
