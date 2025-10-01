class UserAccount:
    def __init__(self, username, password):
        self.username = username  # public
        self.__password = password

    def change_password(self, old_pw, new_pw):
        '''
            현재 비밀번호가 old_pw와 같을 떄만 변경 허용,
            틀리면 "비밀번호 불일치"
        '''
        if self.__password == old_pw:
            self.__password = new_pw
            print('비밀번호가 성공적으로 변경되었습니다.')
        else:
            print('비밀번호 불일치')

    def check_passwrd(self, password):
        '''
            비밀번호 일치 여부를 반환(True/False)
        '''
        return self.__password == password


user1 = UserAccount('김철수', '1234')

print(user1.check_passwrd('1234'))
print(user1.change_password('1234', '2345'))
print(user1.check_passwrd('1234'))
