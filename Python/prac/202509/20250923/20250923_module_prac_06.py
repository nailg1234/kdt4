import random, time
words_list = ['moon', 'potato',
              'tomato', 'blue',
              'code', 'red',
              'phone', 'book',
              'garlic', 'sky']

input('[타자게임] 준비되면 엔터!')
start_time = time.time()
correct_cnt = 0
num = 1

while correct_cnt < 10:

    print(f'문제 {num}')
    ran_word = random.choice(words_list)
    print(ran_word)
    while (ran_word != input()):
        print('오타 다시 도전!')
    else:
        print('\033[32m', end='')
        print(ran_word, '\033[0m')
        print('통과!!')
        correct_cnt += 1
        num += 1
else:
    print(f'타자시간 :  {round(time.time() - start_time, 2)}초')

