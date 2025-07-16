# -*- coding: utf-8 -*-
import os
import shutil
import subprocess
import webbrowser
from datetime import datetime
import http.server


class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        if self.path.endswith(".txt"):
            self.send_header('Content-Disposition', f'attachment; filename="{os.path.basename(self.path)}"')
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
        elif self.path.endswith(".xls") or self.path.endswith(".xlsx"):
            self.send_header('Content-Disposition', f'attachment; filename="{os.path.basename(self.path)}"')
            self.send_header('Content-Type', 'application/vnd.ms-excel')
        super().end_headers()


def _extract_latest_tracking(excel_path: str, save_path: str):
    import pandas as pd
    from datetime import datetime

    xls = pd.ExcelFile(excel_path)
    df = pd.read_excel(xls, sheet_name="업무현황")

    df.columns = df.iloc[0]
    df = df[1:]
    df = df[["장비식별자", "업무트래킹", "최신업무트래킹"]]

    df["최신업무트래킹"] = pd.to_numeric(df["최신업무트래킹"], errors="coerce")
    df = df.sort_values("최신업무트래킹", ascending=False)
    df = df.drop_duplicates(subset=["장비식별자"], keep="first").sort_values("장비식별자")

    today = datetime.now().strftime("%Y%m%d")
    df.to_excel(f"{save_path}/장비별_최신업무트래킹_{today}.xlsx", index=False)
    print("✅ 업무트래킹 최신화 완료")


if __name__ == "__main__":
    BASE = os.path.join(os.environ['USERPROFILE'], 'Downloads', '[]', 'pk_server_api', 'project_release_server')
    EXCEL_FILE = os.path.join(BASE, '영상처리제어기 업무현황.xlsx')
    EXCEL_FILE_WORK_TRACKING_LATEST = os.path.join(BASE, '영상처리제어기 업무현황 최신업무트래킹.xlsx')
    ARCHIVER = os.path.join(BASE, 'pk_archive_old_version.py')
    RELEASE_DIR = os.path.join(BASE, 'release')

    subprocess.Popen(['start', '', EXCEL_FILE], shell=True)
    subprocess.run(['python', ARCHIVER], check=True)

    now = datetime.now()
    FILENAME = f"영상처리제어기_업무현황_{now:%y%m%d_%H%M}.xlsx"
    DEST = os.path.join(RELEASE_DIR, FILENAME)

    os.makedirs(RELEASE_DIR, exist_ok=True)
    shutil.copy2(EXCEL_FILE, DEST)
    print(f"File copied: {FILENAME}")

    _extract_latest_tracking(EXCEL_FILE, EXCEL_FILE_WORK_TRACKING_LATEST)

    subprocess.Popen(['explorer', RELEASE_DIR], shell=True)
    webbrowser.open('http://192.168.2.76:8888')

    # ✅ 작업 디렉토리를 release 디렉토리로 설정
    os.chdir(RELEASE_DIR)

    # 서버 루프 실행
    while True:
        try:
            http.server.test(HandlerClass=MyHTTPRequestHandler, port=8888, bind="0.0.0.0")
        except Exception as e:
            print("서버가 종료되었습니다:", e)
        input("엔터를 누르면 서버를 재시작합니다...")
