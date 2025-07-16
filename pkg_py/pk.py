if __name__ == '__main__':
    try:
        from pkg_py.pk_core import cmd_to_pk
        from colorama import init as pk_colorama_init
        pk_colorama_init(autoreset=True)
        cmd_to_pk()
    except:
        import traceback
        traceback.print_exc()
        # pk_sleep(milliseconds=90000)
