# os 모듈
# 실습 8. 새폴더 생성, 파일목록 출력 따라하기

import os

# 1. 현재 작업 디렉터리 확인
print("현재 작업 디렉터리 확인 : ", os.getcwd)

folder_name = "sample_folder"

# 2. 새 폴더 생성 (이미 있으면 예외 발생 가능)
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f'{folder_name} 폴더를 생성했습니다.')
else:
    print(f'{folder_name} 폴더가 이미 존재합니다.')


# 3. 현재 디렉터리 내 파일/폴더 목록 출력
print("현재 디렉터리 내 파일 및 폴더 목록:")
print(os.listdir())