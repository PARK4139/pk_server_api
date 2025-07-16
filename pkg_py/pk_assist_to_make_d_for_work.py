if __name__ == "__main__":
    try:
        import traceback

        from pkg_py.pk_core import pk_copy, get_migrate_device_table_from_f_xlsx_to_local_db, get_pnx_os_style, pk_sleep, cmd_to_os, ensure_pnx_made, ensure_pnx_removed, LTA, is_year, is_minute, is_hour, is_day, is_month, assist_to_do_pk_schedule, copy_pnx, F_PK_CONFIG_TOML, pk_back_up_pnx, pk_decompress_f_via_zip, get_pn, get_pk_python_program_available_idx_list, get_pk_python_program_pnx_list, \
    get_available_pk_python_program_pnx, pk_run_process, get_time_as_, set_state_from_f_pk_config_toml, get_state_from_f_pk_config_toml, make_d_with_timestamp, assist_to_make_d_for_work
        from pkg_py.pk_colorful_cli_util import pk_print
        from pkg_py.pk_core_constants import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_EXCEPTION_DISCOVERED, D_PKG_DB, D_PKG_CMD, D_PK_RECYCLE_BIN, D_HOME

        assist_to_make_d_for_work()

    except:
        traceback_format_exc_list = traceback.format_exc().split("\n")
        pk_print(working_str=f'{UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            pk_print(working_str=f'{STAMP_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        pk_print(working_str=f'{UNDERLINE}', print_color='red')

    finally:
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        pk_print(working_str=f'{UNDERLINE}')
        pk_print(working_str=f'{STAMP_TRY_GUIDE} {script_to_run_python_program_in_venv}')
        pk_print(working_str=f'{UNDERLINE}')
