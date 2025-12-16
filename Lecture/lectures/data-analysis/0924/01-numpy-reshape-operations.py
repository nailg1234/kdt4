# 파이썬 파일 입출력(File I/O) 완전 가이드

"""
파일 입출력(File I/O)이란?
- 파일을 읽고(input) 쓰는(output) 작업
- 프로그램이 종료되어도 데이터를 영구적으로 보관할 수 있는 유일한 방법
- 프로그램의 데이터는 메모리(RAM)에 저장되는데, 프로그램이 종료되면 메모리의 데이터는 사라짐
- 파일로 저장하면 하드디스크(HDD/SSD)에 영구 보관됨
"""

import os
print("=" * 60)
print("파일 입출력이 필요한 상황들")
print("=" * 60)

"""
파일 입출력이 필요한 대표적인 상황들:

1. 설정 파일 저장: 게임 설정, 프로그램 옵션, 사용자 환경설정
2. 데이터 백업: 중요한 정보나 작업 결과 보관
3. 로그 기록: 프로그램 실행 기록, 에러 추적, 디버깅 정보
4. 데이터 교환: 엑셀, CSV 파일로 다른 프로그램과 데이터 공유
5. 대용량 처리: 메모리에 다 담을 수 없는 빅데이터 처리
"""

print("\n" + "=" * 60)
print("파일 열기/닫기 방법")
print("=" * 60)

print("\n[ 위험한 방법 - 수동으로 파일 닫기 ]")
print("문제점: 예외 발생 시 파일이 제대로 닫히지 않을 수 있음")

# 1단계: 파일 열기 (open) - 파일과 연결 통로 생성
# 'r': 읽기 모드, encoding='utf-8': 한글 깨짐 방지
try:
    file = open('data.txt', 'r', encoding='utf-8')

    # 2단계: 파일 작업 (Read/Write) - 데이터 읽기/쓰기
    content = file.read()
    print("파일 내용:", content)

    # 3단계: 파일 닫기 (Close) - 연결 종료 (중요!!!)
    # 파일을 닫지 않으면 메모리 누수, 파일 잠금 등 문제 발생 가능
    file.close()

except FileNotFoundError:
    print("data.txt 파일이 존재하지 않습니다.")
except Exception as e:
    print(f"파일 처리 중 오류 발생: {e}")

print("\n[ 안전한 방법 - with문 사용 (권장!) ]")
print("장점: 자동으로 파일이 닫히므로 안전하고 깔끔함")

try:
    # with문을 사용하면 블록을 벗어날 때 자동으로 close() 호출
    with open('data.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print("파일 내용:", content)
    # 여기서 자동으로 파일이 닫힘

except FileNotFoundError:
    print("data.txt 파일이 존재하지 않습니다.")

print("\n" + "=" * 60)
print("파일 쓰기 모드")
print("=" * 60)

print("\n[ 'w' 모드: 새 파일 생성 또는 덮어쓰기 ]")
print("주의: 기존 파일이 있으면 내용이 완전히 삭제되고 새로 씀")

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, World!\n')        # 첫 번째 줄 작성
    f.write('파이썬 파일 입출력\n')      # 두 번째 줄 작성
print("output.txt 파일이 생성되었습니다.")

print("\n[ 'a' 모드: 파일 끝에 추가 (append) ]")
print("기존 내용은 유지하고 파일 끝에 새 내용 추가")

with open('output.txt', 'a', encoding='utf-8') as f:
    f.write('추가된 내용\n')           # 기존 내용 뒤에 추가
print("output.txt 파일에 내용이 추가되었습니다.")

print("\n" + "=" * 60)
print("파일 읽기 방법들")
print("=" * 60)

# 테스트용 파일 생성
test_content = """첫 번째 줄입니다.
두 번째 줄입니다.
세 번째 줄입니다.
네 번째 줄입니다.
다섯 번째 줄입니다."""

with open('test_data.txt', 'w', encoding='utf-8') as f:
    f.write(test_content)

print("\n[ 1. read() - 파일 전체를 하나의 문자열로 읽기 ]")
print("장점: 간단함 | 단점: 대용량 파일은 메모리 부족 위험")

with open('test_data.txt', 'r', encoding='utf-8') as f:
    print(f'파일 포인터 처음 위치: {f.tell()}')  # tell(): 현재 파일 포인터 위치
    content = f.read()  # 전체 내용을 한 번에 읽음 (메모리 사용량 多)
    print("전체 내용:")
    print(content)
    print(f'전체 읽은 후 포인터 위치: {f.tell()}')  # 파일 끝 위치

print("\n[ read(크기) - 지정한 바이트 수만큼 읽기 ]")
print("메모리 사용량을 제한할 수 있음")

with open('test_data.txt', 'r', encoding='utf-8') as f:
    print(f'파일 포인터 처음 위치: {f.tell()}')
    content = f.read(10)  # 10바이트만 읽음
    print(f"처음 10바이트: '{content}'")
    print(f'10바이트 읽은 후 포인터 위치: {f.tell()}')

    # 나머지 내용 읽기
    remaining = f.read()
    print(f"나머지 내용: '{remaining}'")

print("\n[ 2. readline() - 한 줄씩 읽기 ]")
print("장점: 메모리 효율적, 대용량 파일 처리 가능")

with open('test_data.txt', 'r', encoding='utf-8') as f:
    print(f'파일 포인터 처음 위치: {f.tell()}')

    line1 = f.readline()  # 첫 번째 줄 읽기 (\n 포함)
    print(f"첫 번째 줄 (strip 전): '{line1}'")
    print(f"첫 번째 줄 (strip 후): '{line1.strip()}'")  # strip(): 앞뒤 공백/개행문자 제거
    print(f'첫 번째 줄 읽은 후 포인터 위치: {f.tell()}')

    line2 = f.readline()  # 두 번째 줄 읽기
    print(f"두 번째 줄: '{line2.strip()}'")
    print(f'두 번째 줄 읽은 후 포인터 위치: {f.tell()}')

    # seek(): 파일 포인터를 특정 위치로 이동
    f.seek(20)  # 20바이트 위치로 이동
    print(f'seek(20) 후 포인터 위치: {f.tell()}')

    line3 = f.readline()  # 현재 위치부터 한 줄 읽기
    print(f"seek 후 읽은 줄: '{line3.strip()}'")

print("\n[ readline()과 for문 조합 - 대용량 파일 처리 최적 ]")
print("메모리 효율적: 한 번에 한 줄씩만 메모리에 로드")

with open('test_data.txt', 'r', encoding='utf-8') as f:
    line_number = 1
    for line in f:  # 파일의 각 줄을 순차적으로 처리 (메모리 절약!)
        print(f"{line_number}번째 줄: {line.strip()}")
        line_number += 1

        # 대용량 파일 처리 예시: 조건에 따라 중단 가능
        # if line_number > 1000:  # 1000줄까지만 처리
        #     break

print("\n[ 3. readlines() - 모든 줄을 리스트로 읽기 ]")
print("반환값: ['첫줄\\n', '둘째줄\\n', '셋째줄\\n', ...] 형태의 리스트")
print("주의: 전체 파일을 메모리에 로드하므로 대용량 파일에는 부적합")

with open('test_data.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()  # 모든 줄을 리스트로 반환
    print(f"읽은 줄 수: {len(lines)}")
    print("각 줄의 원본 데이터:")
    for i, line in enumerate(lines):
        print(f"  {i+1}: {repr(line)}")  # repr(): 특수문자도 보여줌

    print("\n정리된 내용:")
    for i, line in enumerate(lines):
        print(f"  {i+1}: {line.strip()}")

print("\n" + "=" * 60)
print("바이너리 파일 처리 (이미지, 동영상 등)")
print("=" * 60)

print("\n[ 바이너리 파일 복사 예제 ]")
print("'rb': 바이너리 읽기 모드, 'wb': 바이너리 쓰기 모드")

# 실제 이미지 파일이 있다면 복사 가능
# 예제용으로 텍스트 파일을 바이너리로 처리
try:
    # 바이너리 모드로 읽기 (이미지, 동영상, 실행파일 등에 사용)
    with open('test_data.txt', 'rb') as f1:  # 'rb': 바이너리 읽기
        data = f1.read()  # 바이너리 데이터로 읽음
        print(f"바이너리 데이터 크기: {len(data)} 바이트")
        print(f"바이너리 데이터 일부: {data[:50]}")  # 처음 50바이트만 출력

    # 바이너리 모드로 쓰기
    with open('test_data_copy.txt', 'wb') as f2:  # 'wb': 바이너리 쓰기
        f2.write(data)  # 바이너리 데이터를 그대로 복사

    print("파일이 성공적으로 복사되었습니다!")

except FileNotFoundError:
    print("원본 파일을 찾을 수 없습니다.")

print("\n" + "=" * 60)
print("파일 모드 정리")
print("=" * 60)

file_modes = """
텍스트 모드:
  'r'  : 읽기 전용 (기본값)
  'w'  : 쓰기 전용 (파일이 있으면 덮어씀, 없으면 생성)
  'a'  : 추가 모드 (파일 끝에 내용 추가)
  'x'  : 배타적 생성 (파일이 이미 있으면 에러)
  'r+' : 읽기/쓰기 (파일이 반드시 존재해야 함)
  'w+' : 읽기/쓰기 (파일이 있으면 덮어씀, 없으면 생성)

바이너리 모드 (위 모드에 'b' 추가):
  'rb' : 바이너리 읽기
  'wb' : 바이너리 쓰기
  'ab' : 바이너리 추가
  
인코딩:
  encoding='utf-8'  : 한글 등 유니코드 문자 처리 (권장)
  encoding='cp949'  : 한국어 윈도우 기본 인코딩
  encoding='ascii'  : 영어만 지원
"""

print(file_modes)

print("\n" + "=" * 60)
print("실전 팁과 주의사항")
print("=" * 60)

tips = """
💡 실전 팁:

1. 항상 with문 사용하기
   - 파일이 자동으로 닫혀서 안전
   - 예외 발생 시에도 파일이 제대로 닫힘

2. 인코딩 명시하기
   - encoding='utf-8' 사용 권장
   - 한글 깨짐 현상 방지

3. 대용량 파일 처리
   - read() 대신 readline()이나 for문 사용
   - 메모리 효율성 고려

4. 예외 처리하기
   - FileNotFoundError: 파일이 없을 때
   - PermissionError: 권한이 없을 때
   - UnicodeDecodeError: 인코딩 문제

5. 파일 경로 주의
   - 절대경로 vs 상대경로
   - 운영체제별 경로 구분자 차이 (/, \\)

⚠️  주의사항:
- 'w' 모드는 기존 파일을 완전히 삭제함
- 바이너리 파일은 반드시 'b' 모드 사용
- 대용량 파일에서 read()는 메모리 부족 위험
- 파일 경로에 한글이 있으면 인코딩 문제 발생 가능
"""

print(tips)

# 정리용 파일들 삭제 (선택적)
try:
    os.remove('test_data.txt')
    os.remove('test_data_copy.txt')
    os.remove('output.txt')
    print("\n테스트 파일들이 정리되었습니다.")
except:
    pass

print("\n" + "=" * 60)
print("파일 입출력 학습 완료! 🎉")
print("=" * 60)
