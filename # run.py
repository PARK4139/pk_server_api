import subprocess
import os



print("Running main.py in the uv virtual environment...")
main_path = os.path.abspath("main.py")
subprocess.run(f"uv venv exec python3 {main_path}", shell=True)
