
if __name__ == "__main__":
    from pkg_py.pk_core import LTA, pk_debug_state_for_py_data_type, check_installed_wsl, assist_to_control_wsl
    from pkg_py.pk_colorful_cli_util import pk_print
    import sys

    state_wsl_installed, wsl_cmd_map_dict = check_installed_wsl()
    if not state_wsl_installed:
        pk_debug_state_for_py_data_type(pk_stamp='%%%FOO%%%-2', data_working=wsl_cmd_map_dict)
        pk_print("wsl installed", print_color='red')
        sys.exit(0)
    else:
        if LTA:
            pk_debug_state_for_py_data_type(pk_stamp='%%%FOO%%%-3', data_working=wsl_cmd_map_dict)
            pk_print("wsl installed", print_color='green')

    wsl_cmd_list = list(wsl_cmd_map_dict.keys())
    pk_config_dict = {
        'pk_wsl_controller_version': 'pk_wsl_version.2.0.0',
        'pk_wsl_cmd_exec_map_dict': wsl_cmd_map_dict,
        'pk_wsl_cmd_list': wsl_cmd_list,
        'pk_wsl_cmd_list_len': len(wsl_cmd_list),
        'pk_wsl_cmd_map_dict': {idx: cmd for idx, cmd in enumerate(wsl_cmd_list)}
    }
    assist_to_control_wsl(**pk_config_dict)
