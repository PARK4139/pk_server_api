# [independent]

import sys
import os

if "VIRTUAL_ENV" in os.environ:
    # 가상환경에서 실행 중입니다.
    some_condition = 1
    print(some_condition)
    sys.exit(0)  # %errorlevel%=0  # 성공
else:
    # 가상환경이 아닙니다.
    some_condition = 0
    print(some_condition)
    sys.exit(1)  # %errorlevel%=1  # 실패