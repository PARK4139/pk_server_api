import os
import shutil

# 원본 디렉토리와 대상 디렉토리 설정
import os

d_release = rf"{os.environ['USERPROFILE']}\Downloads\pk_server_fastapi\project_release_server\release"
d_archived = rf"{d_release}\archived"


# 대상 디렉토리가 없으면 생성
if not os.path.exists(d_archived):
    os.makedirs(d_archived)

print("-----------------------------------")

# source_dir 디렉토리 내의 파일을 하나씩 확인
for root, dirs, files in os.walk(d_release):
    for filename in files:
        # 파일 이름에 '영상처리제어기 업무현황'이 포함된 파일인지 확인
        if '영상처리제어기 업무현황' in filename:
            file_path = os.path.join(root, filename)
            print(f"처리 중인 파일: {file_path}")

            # 파일을 target_dir로 이동
            target_file_path = os.path.join(d_archived, filename)
            try:
                shutil.move(file_path, target_file_path)
                print(f"파일을 이동 중: {filename}")
                # 이동된 파일 확인 출력
                if os.path.exists(target_file_path):
                    print(f"성공적으로 이동됨: {filename}")
                else:
                    print(f"파일 이동 실패: {filename}")
            except Exception as e:
                print(f"파일 이동 중 오류 발생: {filename}, 오류: {e}")

print("-----------------------------------")
print("작업이 완료되었습니다.")
