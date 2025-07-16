import traceback


if __name__ == "__main__":
    from pk_colorful_cli_util import pk_print
    from pkg_py.pk_core_constants import UNDERLINE, D_PROJECT , D_PROJECT, D_DESKTOP
    from pk_core import pk_deprecated_get_d_current_n_like_person, get_f_current_n
    from datetime import datetime
    from datetime import datetime  # Lazy import 적용

    try:
        def copy_changed_files(src_dir, dest_dir, since_time):
            import os  # Lazy import 적용
            import shutil  # Lazy import 적용

            # Unix timestamp로 변환
            since_timestamp = since_time.timestamp()

            # 원본 디렉터리 순회
            for root, dirs, files in os.walk(src_dir):
                # 상대 경로 계산
                relative_path = os.path.relpath(root, src_dir)
                target_root = os.path.join(dest_dir, relative_path)

                # 대상 디렉터리 생성
                os.makedirs(target_root, exist_ok=True)

                for file_name in files:
                    src_file = os.path.join(root, file_name)
                    dest_file = os.path.join(target_root, file_name)

                    # 파일 수정 시간 확인
                    if os.path.getmtime(src_file) >= since_timestamp:
                        # 파일 복사
                        shutil.copy2(src_file, dest_file)
                        print(f"Copied: {src_file} -> {dest_file}")

        # 원본 및 대상 디렉터리 설정
        source_directory = rf"{D_PROJECT}"
        destination_directory = RF"{D_DESKTOP}"
        since = datetime(2025, 1, 1, 15, 30)  # 기준 시점 설정 (예: 2025년 1월 1일 15:30)
        copy_changed_files(src_dir=source_directory, dest_dir=destination_directory, since_time=since)


    except Exception as e:
        traceback.print_exc()
        # 예외 처리
        pk_print(working_str=f'{UNDERLINE}예외발생 s\n\n', print_color='red')
        pk_print(working_str=f'{traceback.format_exc()}\n', print_color='red')
        pk_print(working_str=f'{UNDERLINE}예외발생 e\n\n', print_color='red')

        # 디버깅 노트 출력
        f_current= get_f_current_n()
        d_current=pk_deprecated_get_d_current_n_like_person()
        pk_print(working_str=f'{UNDERLINE}[Debugging Note] s\n', print_color="yellow")
        pk_print(working_str=f'f_current={f_current}\nd_current={d_current}\n', print_color="yellow")
        pk_print(working_str=f'{UNDERLINE}[Debugging Note] e\n', print_color="yellow")
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        pk_print(script_to_run_python_program_in_venv)
