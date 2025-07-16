# -*- coding: utf-8 -*-



if __name__ == '__main__':
    import psutil
    import pynvml

    from pk_core import pk_deprecated_get_d_current_n_like_person, get_f_current_n, chcp_65001, get_os_n, cmd_to_os, print_iterable_as_vertical
    from pkg_py.pk_core_constants import UNDERLINE
    from pkg_py.pk_core import get_list_sorted, get_list_deduplicated, cmd_to_os_like_person
    from pkg_py.pk_colorful_cli_util import pk_print, print_yellow

    try:
        # ___________________________________________________________________________
        if get_os_n() == 'windows':
            chcp_65001()

        process_n_list = []
        process_pid_list = []
        for process in psutil.process_iter(attrs=["pid", "name"]):
            # process_pid_list.append(process.info['pid'])
            process_n_list.append(process.info['name'])

        process_n_list = get_list_deduplicated(working_list=process_n_list)
        process_n_list = get_list_sorted(working_list=process_n_list)
        # print_iterable_as_vertical(item_iterable=process_n_list, item_iterable_n='process_n_list')

        def get_cpu_usage(process_name):
            cpu_usage = 0.0
            for process in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']):
                if process.info['name'] == process_name:
                    cpu_usage += process.info['cpu_percent']
            return cpu_usage

        import psutil
        import pynvml


        def get_gpu_usage_percent(process_name):
            pynvml.nvmlInit()
            device_count = pynvml.nvmlDeviceGetCount()
            total_gpu_memory = 0  # 총 GPU 메모리
            process_gpu_usage = 0  # 특정 프로세스의 사용량

            for i in range(device_count):
                handle = pynvml.nvmlDeviceGetHandleByIndex(i)
                memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)  # 총 메모리 가져오기
                total_gpu_memory += memory_info.total  # 전체 GPU 메모리 (bytes 단위)

                processes = pynvml.nvmlDeviceGetComputeRunningProcesses(handle)  # exec  중인 프로세스 가져오기

                for proc in processes:
                    try:
                        process = psutil.Process(proc.pid)
                        if process.name() == process_name and proc.usedGpuMemory is not None:
                            process_gpu_usage += proc.usedGpuMemory  # 사용 중인 GPU 메모리 (bytes 단위)
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        continue

            pynvml.nvmlShutdown()  # NVML 종료

            if total_gpu_memory == 0:
                return "Error: Could not retrieve total GPU memory."

            gpu_usage_percent = (process_gpu_usage / total_gpu_memory) * 100  # 퍼센트 변환
            return round(gpu_usage_percent, 2)  # 소수점 2자리 반올림




        # process_n = "chrome.exe"
        # process_n = "python.exe"  # 원하는 프로세스 이름 입력
        process_nx = "Losslesscut.exe"
        # while 1:
        #     cpu_usage = get_cpu_usage(process_nx)
        #     if cpu_usage != 0.0:
        #         # print(f"Process '{process_nx}' CPU Usage: {cpu_usage}%")
        #         print(f"Process '{process_nx}' CPU Usage: {int(cpu_usage)}%")
        # while 1:
        #     # gpu_usage = get_gpu_usage(process_nx)
        #     gpu_usage_percent = get_gpu_usage_percent(process_nx)
        #     print(f"Process '{process_nx}' GPU Usage: {gpu_usage_percent}%")

        process_n = "Losslesscut"
        cmd =f'powershell "Get-Process | Where-Object {{ $_.ProcessName -eq \'{process_n}\' }} | Select-Object ProcessName, Id, CPU, WS"'
        std_list = cmd_to_os(cmd=cmd)
        print_iterable_as_vertical(item_iterable=std_list, item_iterable_n='std_list')

    except Exception as e:
        import traceback

        pk_print(working_str=f'{UNDERLINE}예외발생 s\n\n', print_color='red')
        pk_print(f'''{traceback.format_exc()} %%%FOO%%%''', print_color='red')
        pk_print(working_str=f'{UNDERLINE}예외발생 e\n\n', print_color='red')

        pk_print(working_str=f'{UNDERLINE}[Debugging Note] s\n', print_color="yellow")
        f_current= get_f_current_n()
        d_current=pk_deprecated_get_d_current_n_like_person()
        print_yellow(prompt=f'f_current={f_current}\nd_current={d_current}\n')
        pk_print(working_str=f'{UNDERLINE}[Debugging Note] e\n', print_color="yellow")
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        pk_print(script_to_run_python_program_in_venv)

        import ipdb
        ipdb.set_trace()
