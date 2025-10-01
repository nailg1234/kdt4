class Student:
    def __init__(self, score=0):
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    # def get_score(self):
    #     return self.__score

    # def set_score(self, score):
    #     if 0 <= score <= 100:
    #         self.__score = score
    #     else:
    #         raise ValueError('정수는 0이상 100이하만 허용됩니다.')


s1 = Student(90)

# print(s1.get_score())
# print(s1.set_score(80))
# print(s1.get_score())

print(s1.score)
s1.score = 80
print(s1.score)
