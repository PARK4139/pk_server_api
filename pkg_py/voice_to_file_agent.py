# voice_to_file_agent.py

import os
import json
import tempfile
import openai
import pyttsx3
import whisper
from pathlib import Path

# Whisper 로드
model = whisper.load_model("base")  # or "small", "medium", etc.

# TTS 초기화
tts_engine = pyttsx3.init()

# OpenAI API 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

# MCP 도구: 파일 목록 출력 함수
def list_files(path=".", extension=None):
    path_obj = Path(path)
    if not path_obj.exists():
        return {"error": f"{path} 경로가 존재하지 않음."}
    
    files = [str(f.name) for f in path_obj.iterdir() if f.is_file()]
    if extension:
        files = [f for f in files if f.endswith(extension)]
    return {"files": files}

# MCP 라우터
def mcp_router(tool_name, params):
    if tool_name == "list_files":
        return list_files(**params)
    else:
        return {"error": f"알 수 없는 도구 '{tool_name}' 호출됨"}

# 음성 인식
def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result['text']

# GPT 프롬프트 생성 및 MCP 포맷 요청
def convert_to_mcp_command(prompt_text):
    system_prompt = """
너는 음성 명령어를 분석하여 MCP 호출 형식(JSON 형식)으로 변환하는 역할을 한다.
MCP 형식은 다음과 같다:
{
  "tool": "list_files",
  "params": {
    "path": "D_WORKING",
    "extension": ".py"
  }
}
다른 기능은 무시하고 항상 tool과 params만 포함된 JSON만 반환해.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt_text}
        ],
        temperature=0.0
    )
    
    # JSON 추출
    text = response.choices[0].message.content.strip()
    return json.loads(text)

# TTS
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# 실행 파이프라인
def run_voice_agent(audio_file_path):
    print("1. 🎧 음성 인식 중...")
    text = transcribe_audio(audio_file_path)
    print("▶ 인식된 명령어:", text)

    print("2. 💡 GPT 분석 중...")
    mcp_command = convert_to_mcp_command(text)
    print("▶ MCP 명령어:", mcp_command)

    print("3. ⚙️ MCP 실행 중...")
    result = mcp_router(mcp_command['tool'], mcp_command['params'])
    print("▶ 실행 결과:", result)

    print("4. 🗣️ 결과 음성 출력 중...")
    output = (
        "총 " + str(len(result['files'])) + "개의 파일이 있습니다. "
        + ", ".join(result['files']) if 'files' in result else str(result)
    )
    speak(output)

# 예시 실행
if __name__ == "__main__":
    # 테스트용 WAV 파일 경로 (예: "command.wav")
    audio_path = "sample_command.wav"
    run_voice_agent(audio_path)
