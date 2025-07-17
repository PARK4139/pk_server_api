# FROM python:3.12.8-alpine
# FROM python:3.12-slim # Ubuntu-slim [fail]
FROM ubuntu:24.04
WORKDIR /container_workspace
ENV TZ=Asia/Seoul
RUN export LANG=en_US.UTF-8
RUN apt-get update && apt-get install -y \
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
    && rm -rf /var/lib/apt/lists/*  # 설치 후 패키지 목록 삭제하여 용량 최적화

RUN python3 -m venv /container_workspace/.venv
RUN /container_workspace/.venv/bin/pip install --upgrade pip setuptools wheel 

COPY requirements.txt .
# RUN apt-get install uvicorn
RUN /container_workspace/.venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["/container_workspace/.venv/bin/python", "-m", "uvicorn", "project_fastapi.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
