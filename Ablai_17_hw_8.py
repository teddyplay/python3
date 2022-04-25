from random import randint
import datetime

start = datetime.datetime.now()
name = input('Your name: ').title()
tries_user = int(input('How many tries? '))
finish = 0
while finish != tries_user:
    f_number = randint(1, 9)
    s_number = randint(1, 9)
    answer = int(input(f'{f_number} * {s_number} = '))
    correct_ans = f_number * s_number
    if answer == correct_ans:
        print(correct_ans)
        with open('data.txt', 'a') as file:
            file.write(f'{f_number} * {s_number} = {answer} ({correct_ans}) правильно\n')
    else:
        print(correct_ans)
        with open('data.txt', 'a') as file:
            file.write(f'{f_number} * {s_number} = {answer} ({correct_ans}) неправильно\n')
    finish += 1

with open('data.txt', 'a') as file:
    file.write(f'Было {tries_user} попыток.\n Потраченное время: {datetime.datetime.now() - start}ю \nИмя: {name}')