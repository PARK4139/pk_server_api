# chcp 65001
# title %~nx0
# @echo off
# cls
 
# explorer.exe \\192.168.1.40\30_vision_dev\ACU_NO\20_flash
# explorer.exe \\192.168.1.40\30_vision_dev\ACU_NX\20_flash
# explorer.exe \\192.168.1.40\30_vision_dev\Xavier_custom_board



import os
import subprocess

# 파일 경로
paths = [
    r"\\192.168.1.40\30_vision_dev\ACU_NO\20_flash",
    r"\\192.168.1.40\30_vision_dev\ACU_NX\20_flash",
    r"\\192.168.1.40\30_vision_dev\Xavier_custom_board"
]

# 각 경로에 대해 Explorer.exe 열기
for path in paths:
    subprocess.run(["explorer.exe", path])

