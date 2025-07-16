import traceback

if __name__ == "__main__":
    from pk_colorful_cli_util import pk_print
    from pkg_py.pk_core_constants import UNDERLINE, D_PROJECT
    from pk_core import pk_deprecated_get_d_current_n_like_person, get_f_current_n, get_videos_urls_from_youtube_channel_main_page, download_youtube_list

    try:
        # todo
        while 1:
            youtube_channel_main_page_url = input('youtube_channel_main_page_url=')
            youtube_channel_main_page_url = youtube_channel_main_page_url.strip()
            # download_youtube_list(via_f_txt=True, debug_mode=True)
            video_url_list = get_videos_urls_from_youtube_channel_main_page(youtube_channel_main_page_url=youtube_channel_main_page_url)
            download_youtube_list(video_url_list=video_url_list)
    except Exception as e:
        # 예외 처리
        pk_print(f'{UNDERLINE}예외발생 s\n\n', print_color='red')
        pk_print(f'{traceback.format_exc()}\n', print_color='red')
        pk_print(f'{UNDERLINE}예외발생 e\n\n', print_color='red')

        # 디버깅 노트 출력
        f_current = get_f_current_n()
        d_current = pk_deprecated_get_d_current_n_like_person()
        pk_print(f'{UNDERLINE}[Debugging Note] s\n', print_color="yellow")
        pk_print(f'f_current={f_current}\nd_current={d_current}\n', print_color="yellow")
        pk_print(f'{UNDERLINE}[Debugging Note] e\n', print_color="yellow")
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        pk_print(script_to_run_python_program_in_venv)
