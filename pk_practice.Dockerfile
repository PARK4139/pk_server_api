FROM ubuntu:24.04

# mysqlclient 는 C 기반 바이너리 확장 모듈이라 빌드할 때 아래가 필요해
# pkg-config for mysqlclient
# libmysqlclient-dev or default-libmysqlclient-dev (MySQL C 라이브러리 헤더) for mysqlclient
# portaudio19-dev for pyaudio
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    pkg-config \
    default-libmysqlclient-dev \
    portaudio19-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# rust installation  # uv 설치를 위해 필요
# curl https://sh.rustup.rs -sSf | sh
# source $HOME/.cargo/env


# uv installation as binary
# RUN pip3 install uv -> "외부 관리 환경(externally-managed-environment)"으로 설정되어 있기 때문에, 시스템 전역에 직접 pip install 하는 것이 막혀 발생한 것입니다. 이는 PEP 668에 따른 새로운 보안 정책
# Ubuntu 24.04 + Python 3.12는 PEP 668에 따라 전역 pip 설치를 제한해.
# 그래서 pip install uv가 실패하는데, 
# 이렇게 바이너리로 설치하면 그 문제를 우회할 수 있음.
RUN curl -Ls https://astral.sh/uv/install.sh | bash 


# (옵션) PATH 설정
# ENV PATH="/root/.cargo/bin:$PATH"
# ENV PATH="/usr/local/bin:$PATH"
ENV PATH="/root/.local/bin:$PATH"
# if in wsl
# echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
# source ~/.bashrc
# which uv
# uv --version

WORKDIR /app

# pyproject.toml만 먼저 복사 (Docker 캐시 활용)
COPY pyproject.toml ./

# 빨리 만들고 싶으면 이렇게 다 넣으면 되지만, 이렇게 하면 무거워지고 느려짐. 추후 최적화 필요
# COPY . .


# uv.lock 파일을 만들려면 pyproject.toml 이 필요함
# RUN uv pip install -r pyproject.toml && uv pip freeze > uv.lock
# RUN uv pip install --no-cache .
RUN uv venv && uv pip install -r pyproject.toml && uv pip freeze > uv.lock


# uv 가상환경 실행 in wsl
# source .venv/bin/activate


# 실행 명령
# which uv
# which pip3
# which python3
# uv run python3 pkg_py/pk_print_hello_world.py
# uv run python pkg_py/pk_print_hello_world.py
# CMD ["python3", "pkg_py/pk_print_hello_world.py"]
CMD ["uv", "run", "python3", "pkg_py/pk_print_hello_world.py"]
# CMD ["uv --version"]


uv run python pkg_py/pk_print_hello_world.py