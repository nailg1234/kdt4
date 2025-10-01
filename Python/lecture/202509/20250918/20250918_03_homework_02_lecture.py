# **kwargs 사용 연습
# 문제 3. 사용자 정보 출력 함수
# 사용자의 이름, 나이, 이메일 등의 정보를 받아 출력하는 함수를 **kwargs로 구현하세요.
# 정보가 몇 개가 들어오든 모두 출력해야 합니다.
def print_info(**info):
    for key, value in info.items():
        print(f'{key} : {value}')


print_info(name="김구연", age="35", email="abc@def.ghi")


# 문제 4. 할인 계산기
# 상품 가격 목록을 **kwargs로 받아, 각각 10%씩 할인된 가격을 출력하는 함수를 작성하세요.
def p_sale(**p_list):
    for key, value in p_list.items():
        print(f'{key} : {value * 0.9}')


p_sale(냉장고=1000000, 전화기=50000, 컴퓨터=2000000, 책상=300000)
