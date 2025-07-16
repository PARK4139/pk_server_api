if __name__ == "__main__":
    try:
        import os
        import traceback
        from datetime import datetime
        from pathlib import Path

        from pkg_py.pk_core import pk_copy
        from pkg_py.pk_core_constants import UNDERLINE, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED, D_DOWNLOADS
        from pkg_py.pk_colorful_cli_util import pk_print

        # todo : 불필요하다고 판단이 되기도함.

        # 경로 설정
        recuva_dir = Path(f"{D_DOWNLOADS}/working directory for pkg_py pnx restoration via recuva")
        original_dir = Path(f"{D_DOWNLOADS}/pk_server_fastapi/pkg_py")

        # 리네이밍 대상 저장 경로 (타임스탬프 포함)
        timestamp = datetime.now().strftime("%y%m%d_%H%M%S")
        renamed_dir = recuva_dir / f"renamed_{timestamp}"
        renamed_dir.mkdir(exist_ok=True)

        # 파일 목록과 크기 수집
        recuva_files = {f.name: f.stat().st_size for f in recuva_dir.glob("f*.py")}
        original_files = {f.name: f.stat().st_size for f in original_dir.glob("pk*.py")}

        # 유사한 크기 기준으로 매칭
        matches = []
        for r_name, r_size in recuva_files.items():
            candidates = sorted(
                original_files.items(),
                key=lambda x: abs(x[1] - r_size)
            )
            best_match_name, best_match_size = candidates[0]
            matches.append((r_name, r_size, best_match_name, best_match_size, abs(r_size - best_match_size)))

        # delta 기준 정렬 (작은 것부터 우선)
        matches.sort(key=lambda x: x[4])

        # 결과 출력
        print("\n복원 파일 → 추정 파일명 (크기차)")
        for r_name, r_size, o_name, o_size, delta in matches:
            print(f"{r_name:15} ({r_size}B)  ➔  {o_name:30} ({o_size}B)  Δ {delta}B")

        # 사용자 입력
        do_rename = input(f"\n❓ Δ ≤ 100B 항목만 rename할까요? (o 입력 시 실행): ").strip().lower() == "o"

        if do_rename:
            print(f"\n📁 Δ ≤ 100B 항목은 {renamed_dir} 디렉토리로 이동 및 이름 변경됩니다.\n")
            for r_name, r_size, o_name, o_size, delta in matches:
                if delta <= 100:
                    src = recuva_dir / r_name
                    dst = renamed_dir / o_name

                    # 이름 중복 시 넘버링 처리
                    counter = 1
                    base_stem = dst.stem
                    base_suffix = dst.suffix
                    while dst.exists():
                        dst = renamed_dir / f"{base_stem}_{counter}{base_suffix}"
                        counter += 1

                    os.rename(src, dst)
                    print(f"✅ RENAME: {r_name} ➔ {dst.name} (Δ {delta}B)")
                else:
                    print(f"🚫 IGNORE: {r_name} ➔ {o_name} (Δ {delta}B > 100)")
        else:
            print("\n🚫 리네이밍 취소됨.")

    except:
        traceback_format_exc_list = traceback.format_exc().split("\n")
        pk_print(working_str=f'{UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            pk_print(working_str=f'{STAMP_UNIT_TEST_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        pk_print(working_str=f'{UNDERLINE}', print_color='red')

    finally:
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        pk_print(working_str=f'{UNDERLINE}')
        pk_print(working_str=f'{STAMP_TRY_GUIDE} {script_to_run_python_program_in_venv}')
        pk_print(working_str=f'{UNDERLINE}')