# -*- coding: utf-8 -*-
# encoding declaration
__author__ = 'pk == junghoon.park'

import os
import sys
import subprocess
import traceback
from pathlib import Path
from colorama import init as pk_colorama_init

pk_colorama_init(autoreset=True)


def ensure_os_path_added():
    """
    표준 라이브러리와 시스템 명령(setx, 쉘 프로파일 편집)을 사용해
    중복을 제거하고 지정한 경로를 PATH 환경 변수에
    현재 프로세스와 영구 등록(Windows Registry 또는 쉘 프로파일)합니다.
    또한 사용자가 입력했던 경로를 홈 디렉토리의 ힴ토리 파일에 기록합니다.
    """
    # 사용자 입력 받기
    os_path_to_add = input("추가할 경로를 입력하세요: ").strip()

    # 입력 경로 검증
    if not os.path.isdir(os_path_to_add):
        print(f"경로가 존재하지 않습니다: {os_path_to_add}")
        return

    # 히스토리 파일 설정
    hist_file = Path.home() / ".ensure_os_path_history.txt"
    history = []
    if hist_file.exists():
        history = [line.strip() for line in hist_file.read_text(encoding="utf-8").splitlines() if line.strip()]

    # 히스토리에 추가 (중복 제거)
    if os_path_to_add in history:
        history.remove(os_path_to_add)
    history.insert(0, os_path_to_add)
    hist_file.write_text("\n".join(history), encoding="utf-8")

    # 현재 PATH 가져와 항목별 분리
    current_paths = os.environ.get("PATH", "").split(os.pathsep)
    unique_paths = []
    for p in current_paths:
        if p and p not in unique_paths and os.path.isdir(p):
            unique_paths.append(p)

    # 새 경로 추가
    if os_path_to_add not in unique_paths:
        unique_paths.append(os_path_to_add)

    # 새로운 PATH 문자열 생성
    new_path_str = os.pathsep.join(unique_paths)

    # 현재 프로세스에 적용
    os.environ["PATH"] = new_path_str
    print("✅ PATH가 업데이트되었습니다.")
    print(f"새 PATH: {new_path_str}")

    # 영구 등록
    if os.name == "nt":
        try:
            # setx는 1024자 제한이 있으므로 주의
            subprocess.run(["setx", "PATH", new_path_str], check=True, shell=True)
            print("✅ Windows 레지스트리에 영구 등록되었습니다.")
            print("새로운 CMD 창을 열어 변경 사항을 확인하세요.")
        except subprocess.CalledProcessError as e:
            print(f"❌ setx 실행 중 오류 발생: {e}")
    else:
        shell = os.path.basename(os.environ.get("SHELL", ""))
        profile_map = {"bash": ".bashrc", "zsh": ".zshrc"}
        profile = Path.home() / profile_map.get(shell, ".profile")
        export_line = f'\n# ensure_os_path_added 추가\nexport PATH="{new_path_str}"\n'
        try:
            text = profile.read_text(encoding="utf-8")
            # 이미 추가된 export_line이 없을 때만 붙임
            if export_line.strip() not in text:
                profile.write_text(text + export_line, encoding="utf-8")
            print(f"✅ {profile.name}에 export 라인이 추가되었습니다.")
            print("새 터미널을 열어 변경 사항을 확인하세요.")
        except Exception as e:
            print(f"❌ 프로파일에 추가 중 오류 발생: {e}")


if __name__ == "__main__":
    try:
        ensure_os_path_added()
    except Exception:
        print(traceback.format_exc())
        sys.exit(1)