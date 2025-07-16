chcp 65001 >nul
@echo off
setlocal

set "BASE_DIR=%~dp0"
set "BASE_DIR=%BASE_DIR:~0,-1%"

echo [INFO] BASE_DIR is "%BASE_DIR%"

call "%BASE_DIR%\.venv\Scripts\activate.bat"
python "%BASE_DIR%\pk_push_project_to_github.py"
