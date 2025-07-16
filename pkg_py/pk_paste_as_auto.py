import sys

def pk_paste():
    import clipboard
    return clipboard.paste()

def pk_copy(working_str):
    import clipboard
    # Set-Clipboard -Value "텍스트"  # 클립보드에 텍스트 저장
    clipboard.copy(working_str)

def get_clipboard_text():
    try:
        import subprocess
        result = subprocess.run(
            ["powershell", "-command", "Get-Clipboard"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"[ERROR] 클립보드 읽기 실패: {e}"

venv_arg = sys.argv[1] if len(sys.argv) > 1 else None
if venv_arg:
    pk_copy(venv_arg)
    pk_paste()