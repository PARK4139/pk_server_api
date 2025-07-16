# import os

# # 현재 PATH 환경 변수 가져오기
# current_path = os.environ.get("PATH", "")
# path_list = current_path.split(";")

# # 중복 제거 (순서 유지)
# cleaned_paths = []
# seen = set()
# for path in path_list:
#     path = path.strip()
#     if path and path not in seen:
#         seen.add(path)
#         cleaned_paths.append(path)

# # UV 경로 추가 (사용자 지정)
# uv_path = r"C:\Users\user\Downloads\pk_server_fastapi\pkg_exe"
# if uv_path not in seen:
#     cleaned_paths.append(uv_path)

# # 새로운 PATH 설정
# new_path = ";".join(cleaned_paths)
# os.system(f'setx PATH "{new_path}"')

# # 결과 출력
# print("✅ PATH 중복 제거 및 UV 경로 추가 완료.")
# print("📌 최신 PATH:")
# print(new_path)


print("해당 스크립트는 관리자 권한으로 실행이 되어야 합니다.{__file__}")

import os

# 현재 PATH 환경 변수 가져오기
current_path = os.environ.get("PATH", "")
path_list = current_path.split(";")

# 중복 제거 (순서 유지)
cleaned_paths = []
seen = set()
for path in path_list:
    path = path.strip()
    if path and path not in seen:
        seen.add(path)
        cleaned_paths.append(path)

# UV 경로 추가 (사용자 지정)
uv_path = r"C:\Users\user\Downloads\pk_server_fastapi\pkg_exe"
if uv_path not in seen:
    cleaned_paths.append(uv_path)

# 새로운 PATH 설정
new_path = ";".join(cleaned_paths)
os.system(f'setx PATH "{new_path}"')  # 시스템 환경 변수 적용
os.environ["PATH"] = new_path         # 현재 세션에 즉시 적용

# 결과 출력
print("✅ PATH 중복 제거 및 UV 경로 추가 완료.")
print("📌 최신 PATH:")
print(new_path)
