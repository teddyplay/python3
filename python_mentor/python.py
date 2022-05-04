data = int(input('Введите день рождения '))
month = int(input('Введите месяц рождения '))

if (data>=21 and data<=18 and month==3) or( month==4 and data>=1 and data<=19):
    print('Овен')

elif (data>=20 and data<=30 and month==4) or( month==5 and data>=1 and data<=20):
    print('Телец')

elif (data>=21 and data<=31 and month==5) or( month==6 and data>=1 and data<=21):
    print('Близнецы')

elif (data>=22 and data<=30 and month==6) or( month==7 and data>=1 and data<=22):
    print('Рак')

elif (data>=23 and data<=31 and month==7) or( month==8 and data>=1 and data<=22):
    print('Лев')

elif (data>=23 and data<=31 and month==8) or( month==9 and data>=1 and data<=22):
    print('Дева')

elif (data>=23 and data<=30 and month==9) or( month==10 and data>=1 and data<=23):
    print('Весы')

elif (data>=24 and data<=31 and month==10) or( month==11 and data>=1 and data<=22):
    print('Скорпион')

elif (data>=23 and data<=30 and month==11) or( month==12 and data>=1 and data<=21):
    print('Стрелец')

elif (data>=22 and data<=31 and month==12) or( month==1 and data>=1 and data<=20):
    print('Козерог')

elif (data>=21 and data<=31 and month==1) or( month==2 and data>=1 and data<=18):
    print('Водолей')

elif (data>=19 and data<=29 and month==2) or( month==3 and data>=1 and data<=20):
    print('Рыбы')

else:
    print('Введите ваш запрос корректнее!')


#class Peerson ():
#    def __init__(self , fullname , age , is_married):
#        self.fullname = fullname 
#        self.age = age 
#        self.is_married = is_married 
#
#    def introduce_myself(self):
#        print(f'{self.fullname} , {self.age} , {self.is_married} ')
#
#class Student(Peerson):
#    def __init__(self, fullname, age, is_married):
#        super().__init__(fullname, age, is_married)







