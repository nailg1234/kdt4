# 파일 기반 회원 관리 시스템
"""
이 프로그램은 파일 입출력과 예외 처리를 활용하여
회원 정보 관리와 전화번호 저장 기능을 제공합니다.

주요 기능:
1. 회원 가입 (이름, 비밀번호를 파일에 저장)
2. 로그인 검증 (파일에서 회원 정보 확인)
3. 전화번호 저장/수정 (로그인 성공 시)
"""


def saved_phone(input_id):
    """
    로그인한 회원의 전화번호를 저장하거나 수정하는 함수

    매개변수:
        input_id (str): 로그인한 회원의 이름

    동작 과정:
        1. 사용자로부터 전화번호 입력받기
        2. 기존 전화번호 파일 읽기 (없으면 새로 생성)
        3. 딕셔너리에 모든 회원의 전화번호 저장
        4. 현재 사용자의 전화번호 추가/수정
        5. 업데이트된 정보를 파일에 다시 저장
    """
    print(f"\n=== {input_id}님의 전화번호 등록 ===")

    # 사용자로부터 전화번호 입력받기
    input_phone = input('전화번호를 입력하세요 (예: 010-1234-5678): ')

    # 전화번호를 저장할 딕셔너리 초기화
    members = {}  # {이름: 전화번호} 형태로 저장할 딕셔너리

    # 기존 전화번호 파일이 있는지 확인하고 읽어오기
    try:
        print("📁 기존 전화번호 파일을 확인하는 중...")

        # 'member_tel.txt' 파일을 읽기 모드로 열기
        with open('member_tel.txt', 'r', encoding='utf-8') as f2:
            # 파일의 각 줄을 순서대로 처리
            for line in f2:
                # line.strip(): 앞뒤 공백과 개행문자 제거
                # split(): 공백을 기준으로 문자열을 나누어 리스트로 변환
                # 예: "철수 010-1234-5678\n" → ["철수", "010-1234-5678"]
                saved_name, saved_phone = line.strip().split()

                # 딕셔너리에 기존 회원들의 전화번호 저장
                members[saved_name] = saved_phone

        print(f"✅ 기존 회원 {len(members)}명의 전화번호를 불러왔습니다.")

        # 현재 상태 출력 (디버깅 및 확인용)
        print("현재 저장된 전화번호:")
        for name, phone in members.items():
            print(f"  - {name}: {phone}")

    except FileNotFoundError:
        # 파일이 존재하지 않는 경우 (첫 번째 실행)
        print("📝 전화번호 파일이 없습니다. 새로 생성합니다.")

    except Exception as e:
        # 파일 읽기 중 다른 오류 발생 시
        print(f"⚠️ 파일 읽기 중 오류 발생: {e}")
        print("빈 상태로 시작합니다.")

    # 현재 로그인한 사용자의 전화번호 추가 또는 업데이트
    old_phone = members.get(input_id, None)  # 기존 전화번호 확인

    if old_phone:
        print(f"📞 기존 전화번호: {old_phone}")
        print(f"🔄 새 전화번호로 업데이트: {input_phone}")
    else:
        print(f"📞 새 전화번호 등록: {input_phone}")

    # 딕셔너리에 전화번호 추가/수정
    # 키가 이미 있으면 값이 수정되고, 없으면 새로 추가됨

    members[input_id] = input_phone

    # 업데이트된 전화번호 딕셔너리를 파일에 저장
    try:
        print("💾 전화번호 파일을 업데이트하는 중...")

        # 'member_tel.txt' 파일을 쓰기 모드로 열기 (기존 내용은 덮어씀)
        with open('member_tel.txt', 'w', encoding='utf-8') as f2:
            # 딕셔너리의 모든 항목을 파일에 저장
            for name, phone in members.items():
                # 각 줄에 "이름 전화번호" 형태로 저장
                f2.write(f'{name} {phone}\n')

        print("✅ 전화번호가 성공적으로 저장되었습니다!")

        # 최종 저장 상태 확인
        print("\n📋 최종 저장된 전화번호 목록:")
        for name, phone in members.items():
            status = "🆕" if name == input_id and not old_phone else "🔄" if name == input_id else "📞"
            print(f"  {status} {name}: {phone}")

    except Exception as e:
        print(f"❌ 파일 저장 중 오류 발생: {e}")
        print("전화번호 저장에 실패했습니다.")


def register_members():
    """
    실습 1: 회원 가입 기능
    3명의 회원 정보(이름, 비밀번호)를 입력받아 파일에 저장
    """
    print("=" * 50)
    print("📝 회원 가입")
    print("=" * 50)

    try:
        # 'member.txt' 파일을 쓰기 모드로 열어서 회원 정보 저장
        with open('member.txt', 'w', encoding='utf-8') as f:
            print("3명의 회원 정보를 입력해주세요.\n")

            # 3명의 회원 정보 입력받기
            for i in range(3):
                print(f"--- {i+1}번째 회원 ---")

                # 사용자 입력받기
                user_id = input('이름을 입력해주세요: ').strip()
                user_pw = input('비밀번호를 입력해주세요: ').strip()

                # 입력값 검증
                if not user_id or not user_pw:
                    print("⚠️ 이름과 비밀번호는 필수입니다!")
                    i -= 1  # 다시 입력받기
                    continue

                # 파일에 "이름 비밀번호" 형태로 저장
                f.write(f'{user_id} {user_pw}\n')
                print(f"✅ {user_id}님 가입 완료!\n")

        print("🎉 모든 회원 가입이 완료되었습니다!")

        # 저장된 회원 목록 확인
        print("\n📋 가입된 회원 목록:")
        with open('member.txt', 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                user_id = line.split()[0]  # 이름만 추출 (비밀번호는 보안상 숨김)
                print(f"  {i}. {user_id}")

    except Exception as e:
        print(f"❌ 회원 가입 중 오류 발생: {e}")


def login_and_save_phone():
    """
    실습 2: 로그인 검증 및 전화번호 저장 기능
    저장된 회원 정보로 로그인하고, 성공 시 전화번호 저장 기능 실행
    """
    print("\n" + "=" * 50)
    print("🔐 로그인")
    print("=" * 50)

    try:
        # 회원 파일이 존재하는지 확인
        with open('member.txt', 'r', encoding='utf-8') as f:
            # 사용자로부터 로그인 정보 입력받기
            print("로그인 정보를 입력해주세요.")
            input_id = input('이름을 입력해주세요: ').strip()
            input_pw = input('비밀번호를 입력해주세요: ').strip()

            print("\n🔍 회원 정보를 확인하는 중...")

            # 파일의 각 줄을 확인하여 로그인 정보 검증
            login_success = False

            for line_num, line in enumerate(f, 1):
                try:
                    # 각 줄에서 이름과 비밀번호 분리
                    # strip(): 개행문자 제거, split(): 공백으로 분리
                    user_id, user_pw = line.strip().split()

                    print(f"  📄 {line_num}번째 회원 정보 확인 중...")

                    # 입력받은 정보와 파일의 정보 비교
                    if user_id == input_id and user_pw == input_pw:
                        print(f"✅ 로그인 성공! {input_id}님 환영합니다!")
                        login_success = True

                        # 로그인 성공 시 전화번호 저장 함수 호출
                        saved_phone(input_id)
                        break  # 로그인 성공했으므로 반복문 종료

                except ValueError:
                    # 파일 형식이 올바르지 않은 경우 (이름 비밀번호가 아닌 다른 형태)
                    print(f"⚠️ {line_num}번째 줄 형식 오류: '{line.strip()}'")
                    continue

            # for-else: for문이 break 없이 정상 완료된 경우 실행
            else:
                if not login_success:
                    print("❌ 로그인 실패!")
                    print("이름 또는 비밀번호를 확인해주세요.")

                    # 등록된 회원 목록 힌트 제공
                    print("\n💡 등록된 회원 목록:")
                    f.seek(0)  # 파일 포인터를 처음으로 이동
                    for i, line in enumerate(f, 1):
                        try:
                            user_id = line.split()[0]
                            print(f"  {i}. {user_id}")
                        except:
                            continue

    except FileNotFoundError:
        print("❌ 회원 파일을 찾을 수 없습니다!")
        print("먼저 회원 가입을 진행해주세요.")

    except Exception as e:
        print(f"❌ 로그인 중 오류 발생: {e}")


def display_all_members():
    """
    저장된 모든 회원 정보를 표시하는 함수 (디버깅/확인용)
    """
    print("\n" + "=" * 50)
    print("👥 전체 회원 정보")
    print("=" * 50)

    try:
        # 회원 기본 정보 표시
        print("📋 회원 목록 (member.txt):")
        with open('member.txt', 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                try:
                    user_id, user_pw = line.strip().split()
                    # 보안을 위해 비밀번호는 * 로 마스킹
                    masked_pw = '*' * len(user_pw)
                    print(f"  {i}. {user_id} ({masked_pw})")
                except:
                    print(f"  {i}. 형식 오류: {line.strip()}")

    except FileNotFoundError:
        print("📂 member.txt 파일이 없습니다.")

    try:
        # 전화번호 정보 표시
        print("\n📞 전화번호 목록 (member_tel.txt):")
        with open('member_tel.txt', 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                try:
                    name, phone = line.strip().split()
                    print(f"  {i}. {name}: {phone}")
                except:
                    print(f"  {i}. 형식 오류: {line.strip()}")

    except FileNotFoundError:
        print("📂 member_tel.txt 파일이 없습니다.")


def main_menu():
    """
    메인 메뉴를 표시하고 사용자 선택을 처리하는 함수
    """
    while True:
        print("\n" + "=" * 60)
        print("🏠 파일 기반 회원 관리 시스템")
        print("=" * 60)
        print("1️⃣ 회원 가입 (3명 등록)")
        print("2️⃣ 로그인 및 전화번호 저장")
        print("3️⃣ 전체 회원 정보 보기")
        print("4️⃣ 프로그램 종료")
        print("=" * 60)

        try:
            choice = input("선택하세요 (1-4): ").strip()

            if choice == '1':
                register_members()

            elif choice == '2':
                login_and_save_phone()

            elif choice == '3':
                display_all_members()

            elif choice == '4':
                print("👋 프로그램을 종료합니다. 안녕히 가세요!")
                break

            else:
                print("❌ 잘못된 선택입니다. 1-4 중에서 선택해주세요.")

        except KeyboardInterrupt:
            print("\n\n⏹️ 사용자에 의해 프로그램이 중단되었습니다.")
            break

        except Exception as e:
            print(f"❌ 예상치 못한 오류 발생: {e}")


if __name__ == "__main__":
    """
    프로그램의 진입점
    직접 실행될 때만 메인 메뉴 실행
    """
    print("🚀 파일 기반 회원 관리 시스템을 시작합니다!")

    # 실제 실행 시에는 main_menu()를 호출하세요
    main_menu()

    # 코드 설명을 위한 시뮬레이션 실행
    print("\n" + "=" * 60)
    print("📚 코드 동작 시뮬레이션")
    print("=" * 60)

    # 실제 사용 예시 설명
    simulation_text = """
실제 프로그램 실행 순서:

1️⃣ 회원 가입 단계:
   - register_members() 함수 실행
   - 3명의 이름과 비밀번호 입력
   - member.txt 파일에 저장
   
2️⃣ 로그인 단계:
   - login_and_save_phone() 함수 실행  
   - 저장된 회원 정보로 로그인 시도
   - 성공 시 saved_phone() 함수 자동 호출
   
3️⃣ 전화번호 저장 단계:
   - 기존 member_tel.txt 파일 읽기 (없으면 생성)
   - 딕셔너리에 모든 전화번호 로드
   - 현재 사용자 전화번호 추가/수정
   - 업데이트된 정보를 파일에 저장

💡 핵심 개념:
   - 파일 입출력: 데이터 영구 저장
   - 예외 처리: 파일 없음, 형식 오류 등 처리  
   - 딕셔너리: 메모리에서 빠른 검색/수정
   - 문자열 처리: split(), strip() 활용
"""

    print(simulation_text)

    # 파일 형식 예시
    print("\n📁 파일 형식 예시:")
    print("member.txt:")
    print("철수 1234")
    print("영희 abcd")
    print("민수 5678")
    print()
    print("member_tel.txt:")
    print("철수 010-1111-2222")
    print("영희 010-3333-4444")

    print("\n✅ 코드 분석이 완료되었습니다!")
    print("실제 실행하려면 main_menu() 함수의 주석을 해제하세요.")
