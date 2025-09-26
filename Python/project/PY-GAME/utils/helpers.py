import random

# 1 ~ 10 중에 8, 9, 10이 나오면 True (30% 확률로 특수 공격) 
def is_special_attack():
    return 7 < random.randint(1, 10)

# 1 ~ 10 중에 4, 5, 6, 7, 8, 9, 10이 나오면 True (70% 확률로 도적의 특수 공격시전) 
def is_special_attack_rogue():
    return 3 < random.randint(1, 10)