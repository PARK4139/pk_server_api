

if __name__ == '__main__':
    try:
        from pk_core import run_project_docker_base, pk_deprecated_get_d_current_n_like_person, get_f_current_n, get_driver_selenium
        from pkg_py.pk_colorful_cli_util import pk_print
        from pkg_py.pk_core_constants import UNDERLINE, D_PROJECT

        f_dockerfile_script_list = [
            f'# FROM python:3.12.8-alpine',
            f'# FROM python:3.12-slim # Ubuntu-slim [fail]',
            f'FROM ubuntu:24.04',
            f'WORKDIR /container_workspace',
            f'ENV TZ=Asia/Seoul',
            f'RUN export LANG=en_US.UTF-8',
            f'RUN apt-get update && apt-get install -y \
                        python3 \
                        python3-pip \
                        python3-venv \
                        bash \
                        bash-completion \
                        curl \
                        wget \
                        unzip \
                        nano \
                        ca-certificates \
                        software-properties-common \
                        locales \
                        tzdata \
                        build-essential \
                        pkg-config \
                        libmariadb-dev \
                        gcc \
                        portaudio19-dev \
                        && rm -rf /var/lib/apt/lists/*  # 설치 후 패키지 목록 삭제하여 용량 최적화',
            f'',
            f'RUN python3 -m venv /container_workspace/.venv',
            f'RUN /container_workspace/.venv/bin/pip install --upgrade pip setuptools wheel ',
            f'',
            f'COPY requirements.txt .',
            f'# RUN apt-get install uvicorn',
            f'RUN /container_workspace/.venv/bin/pip install --no-cache-dir -r requirements.txt',
            f'',
            f'COPY . .',
            f'',
            f'CMD ["/container_workspace/.venv/bin/python", "-m", "uvicorn", "project_fastapi.main_pk:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]',
            f'',
        ]
        # run_project_docker_base(f=rf'{D_PROJECT}/project_fastapi.Dockerfile',f_dockerfile_script_list=f_dockerfile_script_list)
        run_project_docker_base(f=rf'{D_PROJECT}/test.Dockerfile', dockerfile_script_list=f_dockerfile_script_list)

    except Exception as e:
        # red
        import traceback
        pk_print(working_str=f'{UNDERLINE}예외발생 s\n\n', print_color='red')
        pk_print(working_str=f'{traceback.format_exc()}\n', print_color='red')
        pk_print(working_str=f'{UNDERLINE}예외발생 e\n\n', print_color='red')

        # yellow
        f_current= get_f_current_n()
        d_current=pk_deprecated_get_d_current_n_like_person()
        pk_print(working_str=f'{UNDERLINE}[Debugging Note] s\n', print_color="yellow")
        pk_print(working_str=f'f_current={f_current}\nd_current={d_current}\n', print_color="yellow")
        pk_print(working_str=f'{UNDERLINE}[Debugging Note] e\n', print_color="yellow")
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        pk_print(script_to_run_python_program_in_venv)
