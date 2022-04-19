#name = 'ablai'
#age = 19
#color = 'white'
#print ('прикинь , его зовут {0} , ему целых {1} лет, и от того что он вообще не выходит на солнце он {2}'.format(name , age, color))









#i = 5
#print (i)
#i += 1 
#print(i)

#s = 'это многосторочный код тебе  его не понять но в принципе если хочешь его понять ьто ты модешь начать тзкучать пайтон'
#print (s)



#i = 5 ; print(i)



#ploshad  = 5
#shirina = 3
#area = ploshad * shirina
#print('площадь равнв ' , area)
#print('площадь равна', 2*(ploshad +shirina))


#while True:
#    number = 55
#    guess = int(input('введите пин - код ;'))
#    if guess == number:
#        print('поздравляю ,вы вошли в систему /n хотя ниснео не взломали')
 #       
 #   elif guess < number:
#        print ('число чуть выше')
#
 #   else:
 #       print('чувак ты нисего не угадал , лох')



#number = 555
#running = True
#while running :
#
 #   guess = int(input('введите пин код: , '))
#
#    if guess == number:
 #       print( 'Да ,вы угадали со значением ! ')
 #       print('если желаете выйти нажмите "q')
 #       break
 #   
  #  elif guess < number :
  #      print ('нет число выше , гадай дальше')
  #  
  #  elif guess >  number :
  #      print ('нет число ниже ,гадай дальше')
#
  #  else:
  #      print (' что ты вообще ввел?')



#for i in range(0 , 5):
#   print (i)


#while True:
#    a = input('введите что нибудь : , для выхода нажмите q : ')
#    if a == 'q' :
 #       print('программа завершена !')
 #       break
 #   print ('длина строки:' , len(a))



#while True:
#    a = input("введите слово из 5 букв , для выхода нажмите : exit :")
#    if a == 'exit':
#        break
#    if len(a) < 5 :
#        print('то что вы ввели слишком маленькое слово!')
#    if len(a) > 5 :
 #       print('то что вы ввели слишком длинное слово!')
 #       continue
 #   print('то что вы ввели достаточной длины!')




#def sayHello():
#    print('привет скажи !')
#
#sayHello()
#sayHello()




#def printMax( a , b ):
#    if a > b :
#        print( a , ' максимально')
 #   elif a == b :
#        print(a , ' равно ' , b )
#    else:
#        print ( b , ' максимально ')
#
#printMax( 3 , 4 )
#
#x = 4
#y = 4
#
#printMax( x , y )




#x = 50
#
#def func(x):
#    print('значение ' , x)
#    x = 2 
#    print ('замена локалного x на ' , x)
#
#func(x)
#print('x по прежнему ' , x)



#x = 50
#
#def func():
#    global x 
#    print ( 'x  равен:' , x )
#    x = 2 
#func()
#print('x уже равен ' , x)





#def func_outher():
#    x = 3
#     print(' локальный x ' , x )
#
 #   def func_inner():
 #       nonlocal x
 #       x = 5 
 #   func_inner()
 #   print ('локальное x сменилось на ' , x)
#
#func_outher()




#def say( message , time=1):
#    print( message * time)
#
#say('привет !')
#say(  'мир' , 5)
#
#
#
#
#def say(message , time = 1 ):
#    print ( message * time)
#
#say('привет')
#say('мир ' , 6)




#def primer( a , b = 5 , c = 12):
#    print ( 'a равно = ' , a , ' , b  равно = ' , b , ' ,  а c равно  = ' , c)
#
#primer( a = 3 )
#primer(a = 4  , c = 5)
#primer(a = 1 , b = 6 , )


#while True:
 #   ask = input('напишите что нибудь ))) , а для выхода нажмите q ')
#    if ask == 'q':
#        print('программа завершена!')
 #       break
 #   print ('длина строки = ' , (len(ask)))




#def total( a = 5 , *numbers , **phonebook):
 #   print('a = ' , a)
 #   
 #   for single_items in numbers:
 #       print('single items' , single_items)
#
 #   for first_part , second_part in phonebook.items():
#        print(first_part , second_part)
#
#print(total( 10 , 1 , 2 , 3 , "jack = 4567" , "Amber = 9746" , "johny = 8246"))



#def numbers( x , y ):
 #   if x < y :
#        return y 
#    elif x == y :
#        return 'числа равны бро '
#    else:
#       return 'y , больше бро'
#
#print(numbers( 3 , 3 ))



#from math import *
#n = int(input("Введите диапазон:- ")) 
#p = [2, 3]
#count = 2
#a=5
#while (count < n):
#    b=0
#    for i in range(2,a):
#        if ( i <= sqrt(a)): 
#            if (a % i == 0):
#                print(a,"непростое")
#                b=1 
#        else:
 #           pass
#        if (b != 1): 
 #           print(a,"простое") 
 #           p = p + [a]
 ##       count = count + 1
 #       a=a+2 
#print(p)


#if __name__ == "__main__":
#    print ('эта программа запущена самам по себе')
#else :
#    print('нет его запустили насилльно')




#shop = ['яблоки ' , 'банан ' , 'апельсины' , 'клубника' , 'малина ']
#jack = 'я посчитал все фрукты которые мне нужно было купить и их  ' , len(shop) , 'штук'
#print ( jack , end = '')
#
#for item in shop:
##  print(  item , end = '' )
#
#print( ' \n так же нужно купить риса ')
#shop.append('рис')
#print('теперь мой список выглядит так : ' , shop )
#
#print('отсорирую ка я свой список , ')
#shop.sort()
#print ('теперь мой отсартированный список выглядит так : ' , shop )

#print('для начала мне нужно купить : ' , shop[0])
#print('апельсины я купил , теперь мне нужно убрать их из списка ')
#olditem = shop
#del shop[0]
#print('мой список покупок теперь выглядит так ;' , shop )


#while True:
#  produkts = [ 'яблоки' , ' бананы ' , 'апельсины' , ' конфеты' , 'жвачки']
#  print('привет , меня зовут Аблай и я продавец товаров  \n вот писок товаров котрорые сейчас есть у меня :' , produkts)
#  a = input ('желаете что нибудь приобрести из вышеперечисленного ? если ничего не желаете то напечатайте , exit: ')
#  if a == exit:
#    print('тогда хорошего вам дня !')
#    break
#  if 




#zoo = 'пингвин' , ' лошадь' , ' змея ' 
#print('количество всех животных  :' , len(zoo))
#
#new_zoo = 'ястреб ' , ' лев' , 'тигр' , zoo
#print ('количество  клеток в новом зоопарке :' , len(new_zoo))
#print('все животные ы новом зоопарке : ' , (new_zoo))
#print('животные привезенные из сатрого зоопарка  :' , new_zoo[3])
#print('последнее животное привезенное из старого зоопарка :' , new_zoo[3][2])
#print( 'в общем и целом всех животных теперь :' , len(new_zoo)-1 + len(zoo))




#ab = { 'Swaroop' : 'swaroop@swaroopch.com',
#      'Larry' : 'larry@wall.org',
##      'Matsumoto' : 'matz@ruby-lang.org',
#      'Spammer' : 'spammer@hotmail.com' }
#print("Адрес Swaroop'а:", ab['Swaroop'])
#del ab['Spammer']
#print('\nВ адресной книге {0} контакта\n'.format(len(ab)))
#for name, address in ab.items():
#  print('Контакт {0} с адресом {1}'.format(name, address))
# Добавление пары ключ-значение
#ab['Guido'] = 'guido@python.org'
#if 'Guido' in ab:
#  print("\nАдрес Guido:", ab['Guido'])




#while True:
#  ask = input('Введите действие операции  : + , - , * , / . \nДля выхода нажмите q : ')
#
#  if ask ==  'q':
#    print ('программа завершена ')
 #   break
#
 # a = int(input('введите первое значение:'))
#  b = int(input('введите второе значение : '))
#
##  if a + b:
 #   c = a + b 
#    print('результат вычисления данной операции : ' , str( c))
#
 # if a - b :
#   print('результат вычисления даннной операции : ' , int(a - b))
 #   print(c = a - b)
#
 # if a * b:
##    print ('результат вычисления жанной операции : ' ,int( a * b ))
 #   print(c = a * b)
#
 # if a / b:
 ##   print('Бро ,  скажу сразу  , что на 0 делить нельзя )')
 #   print ('резултат вычисления данной операции :' ,int( a / b ))
 #   print(c = a / b)
#
 # else:
 #   print('Такой операции нет зедс чувак , но или её ещё не добавили в меня)))')

#product = ('apple' , 'banan' , 'potato' , 'cherry')
#print('i have:' , list('apple'))
#print( 'так же у меня есть :' , product)


#class Song (object):
##  def __init__(self , lyrics):
#    self.lyrics = lyrics
#
#  def sing_me_a_song(self):
#    for line in self.lyrics:
#      print(line)
#
#happy_birdhday = Song([
#  'с днем рождения тебя я хочу у поздравить' ,
#  'и пожелать тебе счастья'])
#
#bulls_on_parad = Song ([
#  'кто же сегодня потерял корову ?',
# 'а это он потерял оказывается '])
#
#happy_birdhday.sing_me_a_song()
#bulls_on_parad.sing_me_a_song()








#class Point :
#  color = 'red'
#  number = 2


 # def set_cords (self , x , y):
 #   self.x = x
#    self.y = y 

 # def get_corts(self):
 #   return(self.x , self.y)

#pt = Point()
#pt.set_cords( 1 , 2 )
#print(pt.get_corts())



#class Point:
##  def __init__(self, a , b):
#    self.q = a
#    self.z = b
#
#pt = Point( 5 , 6)
#print(pt.__dict__)



#class Car:
#
#  name = 'c200'
#  make = 'mercedec'
#  model = 2018
#
 # def start(self):
 #   print('заводим двигатель')
##
#  def stop(self):
#    print('выключаем двигатель')
#
#car_a = Car()
#car_b = Car()
#
#car_b.start()
#print(car_b.make)
#print(dir(car_b))



#class Car:
#
#  car_count = 0
#
#  def start(self , name , model , age ):
#    print('двигаетль запущен ')
#    self.name = name 
##    self.model= model
#    self.age = age
#    Car.car_count += 1 
#
#car_a = Car()
#car_a.start('Rang rover', 'sport' , 2022)
#print(car_a.age)
#print(car_a.car_count)



#class Square:
#  @staticmethod
#  def get_square( a , b ):
#    return (a*a , b*b)
#
#print(Square.get_square(2 , 3))



#class Car:
#  def start(self):
#3    print('двигатеь запущен ')
#
###car_a = Car
#print(car_a.start)




#class Car:
#  car_coun = 0
#  def __init__(self):
#    Car.car_coun += 1
#    print(Car.car_coun)
##
#car_a = Car()
#car_b = Car()
#car_c = Car()





#class Car:
#  def __init__(self):
#    print('двигатель запущен ')
#    self.model = 'm5'
##    self.name = 'bmw'
##    self.age = '2014'
#
#car_a = Car()
#print(car_a.name)




#class House:
#  def __init__(self):
#    print('дом построен на улице :')
##   self.chapaeva_street = 'Чапаеева'
#    self.kosmonavtov_street = 'Космонавтов'
#    self.abai = 'Абай'

#street_1 = House()
#print(street_1.chapaeva_street)




#class Mom():
#  def mom_method(self):
#    print('это родительский класс')
#
#class Son(Mom):
#  def son_method(self):
#    print('это дочерний класс')
#
#mother = Son()
#mother.mom_method()




#class Papa():
#  def papa_method(self):
#    print('это родителький класс')
#
#class Son(Papa):
#  def son_method(self):
#    print('это дочерний класс ')
#
#class Daghter(Son):
#  def doughter_methot(self):
#    print('это тоже дочерний класс )))')
#
#family = Son()
#family.papa_method()
#family = Son()
#family.papa_method()



#class Telephone():
#  def phone(self):
#    print('это родительский класс')
#
#class Camera():
#  def camera(self):
#    print('это камера , метод из родитеолького класса')
#
#class Microphone(Telephone , Camera ):
##  def microphone(self):
#    print('здесь объеденены сразу два класса')
#
#tech = Microphone()
##tech.phone()
#tech.camera()




#class Calculate ():
#  def start(self , a , b):
#      print(a + b)
#
#math = Calculate()
#math.start( 1 , 3)



class Mother ():
  def mother(self):
    print(' это родителткий класс ')

class Son(Mother):
  def son (self):
    print(' это дочерний класс , взят с класса Mother')

class Doughter(Son):
  def doughter (self):
    print(' это тоже дочерний класс , взятый с класса Son')

family = Mother()
family.mother()
family = Son()
family.son()
family = Doughter()
family.doughter()