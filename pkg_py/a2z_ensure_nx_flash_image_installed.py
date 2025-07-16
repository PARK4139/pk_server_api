#!/usr/bin/env python3
import os
import subprocess

def run_cmd_command(command_str):
    """cmd.exe /c 명령 실행"""
    result = subprocess.run(f'cmd.exe /c "{command_str}"', shell=True)
    if result.returncode != 0:
        raise RuntimeError(f"❌ CMD 명령 실패: {command_str}")

def main():
    filename = "Flash_Image_1.3.0.tar.bz2"
    nas_path = fr"\\192.168.1.40\30_vision_dev\ACU_NX\20_flash\Flash_Image_Release_1.3.0\{filename}"

    # Windows Downloads 경로
    win_userprofile = os.environ.get("USERPROFILE")
    if not win_userprofile:
        raise RuntimeError("❌ USERPROFILE 환경 변수를 찾을 수 없습니다.")

    dst_win_path = os.path.join(win_userprofile, "Downloads")
    full_win_file_path = os.path.join(dst_win_path, filename)

    # WSL 경로로 변환
    src_wsl_path = "/mnt/" + full_win_file_path.replace(":", "").replace("\\", "/").lower()
    dst_wsl_dir = os.path.expanduser("~/flash/nx_flash")
    dst_wsl_path = os.path.join(dst_wsl_dir, filename)

    # NAS → Downloads
    if os.path.exists(full_win_file_path):
        print(f"📁 이미 다운로드되어 있음: {full_win_file_path} → 복사 생략")
    else:
        print(f"📥 NAS에서 {filename} 복사 중...")
        copy_cmd = f'copy "{nas_path}" "{dst_win_path}"'
        run_cmd_command(copy_cmd)
        print("✅ 복사 완료")

    # Downloads → WSL
    print(f"📦 WSL로 이동 중: {src_wsl_path} → {dst_wsl_path}")
    subprocess.run(f'mkdir -p "{dst_wsl_dir}"', shell=True, check=True)
    subprocess.run(f'mv "{src_wsl_path}" "{dst_wsl_path}"', shell=True, check=True)

    print("✅ 완료!")

if __name__ == "__main__":
    main()
