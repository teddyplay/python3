from random import randint
import datetime

secret_num = randint(1, 100)
print(secret_num)
user_try = 0
start = datetime.datetime.now()
while True:
    try:
        user_enter = int(input('Enter the number: '))
        if 1 <= user_enter <= 100:
            if secret_num > user_enter:
                print('>')
                user_try += 1
            elif secret_num < user_enter:
                print('<')
                user_try += 1
            else:
                print('You won!')
                user_try += 1
                break
        else:
            print('Only number from 1 to 100')

    except:
        print('Only number from 1 to 100')
print(f'How many times you used: {user_try}')
print(f'Time needed: {datetime.datetime.now() - start}')