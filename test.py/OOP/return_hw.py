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



#class Mother ():
#  def mother(self):
#    print(' это родителткий класс ')
#
#class Son(Mother):
#3  def son (self):
 #   print(' это дочерний класс , взят с класса Mother')
#
#class Doughter(Son):
#  def doughter (self):
 #   print(' это тоже дочерний класс , взятый с класса Son')

#family = Mother()
#family.mother()
#family = Son()
#family.son()
#family = Doughter()
#family.doughter()








#class Dog:
#  def __init__(self , name , age , type):
#    self.name = name
#    self.age = age
#    self.type = type
#
##  def voice(self):
#    print(f'{self.name} гав гав!')
#
#  def eat(self):
#    print(f"{self.name} i'm eaten ")
#  
#  def sleep(self):
#    print(f"{self.age} i be sleep ")
#
#  def info(self , weight , height ):
#    print(f"""
#    name: {self.name} 
#    Age : {self.age} 
#    Type: {self.type}
#    weight: {weight}
#    height: {height}
#    """)


#rex = Dog('rex', 12 , 'pitbul')
#rex.info(45 , 1.3)
#
#rex = Dog('Sharic' , 5  ,'pitbul')
#rex.voice()
##
#rex = Dog( 'jack'  , 12 , 'husky')
#rex.sleep()


#class Transport:
#  def __init__(self , title , model , age , color):
#    self.title = title 
#    self.model = model  
#    self.age = age 
#    self.color = color
# 
#  def start_engine(self):
#    print(f"{self.title} start engine!")
#
#car = Transport('Range_rover' , 'Sport' , 2016 , "black")
#.start_engine()




#class Дом ():
#
#  def __init__(self , фундамент , стены , крыша , окна ):
#    self.фундамент = фундамент
#    self.стены = стены 
#    self.крыша = крыша 
#    self.онка = окна
#
 # def plan(self):
 #   print( f'{self.фундамент} нужен для постройки дома')
#
#house = Дом( 'фундмаент' , 'стены' , 'крыша' , 'окна')
#house.plan()

  


#class Dog():
#  def __init__(self , name , age , VoiceText):
#    self.name = name
#    self.age = age 
#    self.VoiceText = VoiceText
#
#  def voice(self):
#    print (f' Rax {self.VoiceText} ')
#  
#dog = Dog( 'rax' , 12 ,  'gav- gav')
#dog.voice()
#
#
#class Cat():
#  def __init__(self , name , age , VoiceText):
#    self.name = name
#    self.age = age 
#    self.VoiceText = VoiceText
#
#  def voice(self):
#    print (f'cat {self.VoiceText} ')
#
##cat = Cat( 'hloe ' , 12 ,  'myu - myu ')
#cat.voice()
##
#
#
#class Cow():
#  def __init__(self , name , age , VoiceText):
#    self.name = name
#    self.age = age 
#    self.VoiceText = VoiceText
#
#  def voice(self):
#    print (f'cow {self.VoiceText} ')
#
#cat = Cow(  'jack' , 13 , 'muu - muu')
#cat.voice()
#
#
##class Bear():
#  def __init__(self , name , age , VoiceText):
#    self.name = name
#    self.age = age 
#    self.VoiceText = VoiceText
#
#  def voice(self):
#    print (f'bear {self.VoiceText} ')
#
#cat = Cow(  'greta' , 21 ,  'arr - arr')
#cat.voice()



#""" HOME WORK №1"""
#
#class Bmw ():
#  def __init__(self , title , model , weight , hp , nm , max_speed , color ):
#    self.title = title 
#    self.model = model 
#    self.weight = weight 
#    self.hp = hp 
#    self.nm = nm 
#    self.max_speed = max_speed 
#    self.color = color
#
#  def start_engine(self):
#    print (f'{self.title}  {self.model} engine started !')
#
#  def engine_stop(self):
#    print (f'{self.title} {self.model} engine stopped ! ')
#
#  def info (self):
#     print (f"""
#     {self.title} title
#     {self.model} model 
#     {self.weight} weight
#     {self.hp} hp 
#     {self.nm} nm
#     {self.max_speed} max_speed
#     {self.color} color
#     """)
#
#bmw = Bmw('Bmw' , 'm6' , 1.2  , 560 , 430 , 280 , 'black')
#bmw.start_engine()

#bmw = Bmw('Bmw' , 'm6' , 1.2  , 560 , 430 , 280 , 'black')
#bmw.engine_stop()
#bmw.info()
#
#"""
#Разделение классов :
#"""
#
#class Mercedec ():
#  def __init__(self , title , model , weight , hp , nm , max_speed , color ):
#    self.title = title 
#    self.model = model 
##    self.weight = weight 
#    self.hp = hp 
#    self.nm = nm 
#    self.max_speed = max_speed 
#    self.color = color
#
#  def start_engine(self):
#    print (f'{self.title}  {self.model} engine started !')
#
#  def engine_stop(self):
#    print (f'{self.title} {self.model} engine stopped ! ')
#
#  def info (self):
#     print (f"""
#     {self.title} title 
#     {self.model} model
#     {self.weight} weight
#     {self.hp} hp
#     {self.nm} nm
#     {self.max_speed} max_speed 
#     {self.color} color
#     """)
#
#
#merc = Mercedec( 'Mercedec' , 'cls' , 1.0  , 760 , 530 , 290 , 'monohrome')
#merc.start_engine()
#
#merc = Mercedec ('Mercedec' , 'cls' , 1.0  , 760 , 530 , 290 , 'monohrome')
#merc.engine_stop()
#merc.info()
 


#class Jack ():
#  def __init__(self , name , age ,  height):
#    self.name = name 
#    self.age = age 
#    self.height = height
#
#  def hello(self):
#    print(f'hello my name is {self.name} , my {self.age} age')
#
#name = Jack('jack' , 15 , 1.67 )
#name.hello()




#class Transport():
#  def __init__(self , title , model , color ):
#    self.title = title 
#    self.model = model 
#    self.color = color
#
#  def start_engine(self):
#    print(f'engine on  {self.title}  {self.model} started ')
#
#  def engine_stopped(self):
##    print(f'engine {self.model} {self.title} stopped ')
#
#
#class Car(Transport):
#  def __init__(self, title, model, color , speed):
#      super().__init__(title, model, color)
#      self.speed = speed 
#  def info(self):
#    print(f"{self.speed} 'speed' ")
#
#
#class Airplane(Transport):
 # def __init__(self, title, model, color , speed ,  weight):
#      super().__init__(title, model, color)
#      self.weight = weight
#      self.speed = speed 
#
#class DeliveryAirplane(Airplane):
#  def __init__(self, title , model , color , speed , weight , amount):
#    super().__init__( title , model , color , speed , weight)
#    self.amount = amount
#
#    
#
#merc = Car( 'Mercedec' , 'cls  6.3', 'white' , 320)
#merc.start_engine()
#merc.engine_stopped()
#
#boeyng = Airplane('Boeyng' , 'w235' , 'white' , 8000  , 900)
#boeyng.start_engine()






#class Transport():
#  def __init__(self , title , model , color ):
#    self.title = title 
#    self.model = model 
#    self.color = color
#
#  def start_engine(self):
#   print(f'engine on  {self.title}  {self.model} started ')
#
# def engine_stopped(self):
#    print(f'engine {self.model} {self.title} stopped ')
#
#
#class Car(Transport):
#
#  _curent_speed = 0
#  _is_started = False
#
#  def __init__(self, title, model, color , speed , max_speed):
#      super().__init__(title, model, color)
#      self.speed = speed 
#      self.max_speed = max_speed 
#  
#
#  def _get_curent_speed (self):
#    print(self._curent_speed)
#
#
#  def _get_is_started (self):
#    if not (self._is_started):
#      print('start engine')
#      return False
#    else:
#      return True
#
#
#  def start_engine(self):
#    self._is_started = True
#    print(f'{self.title} engine stardet {self.model}' )
#
#
#  def gas (self):
#    started = self._get_curent_speed()
#
#   if self._curent_speed + self.speed <= self.max_speed and started:
#      self._curent_speed += self.speed
#      self._get_curent_speed()
#    else:
#      print('sorry , CHECK!')
#
#
#  def break_ (self):
#    started = self._get_curent_speed()
#
#    if self._curent_speed >= self.speed and started:
#      self._curent_speed -= self.speed
#      self._get_curent_speed()
#    else:
#      print()
#
#
#bmw = Car ('Bmw' , 'm5 ' , 'black'  , 50 , 550)
#bmw.





#class Person():
#  def __init__(self , first_name , last_name):
#    self.first_name = first_name
#    self.last_name = last_name
#
#class Jack(Person):
#  def __init__(self, first_name, last_name , phone_number , balance):
#      super().__init__(first_name, last_name)
#      self.phone_number = phone_number
#      self.balance = balance
#
#name = Jack(' jack' , 'melly' , 6555656464 , 450)
#      
#
#
#class Vito(Jack):
#  _n_number = 22
#
# def __init__(self, first_name, last_name, phone_number, balance):
#      super().__init__(first_name, last_name, phone_number, balance)
#
# def minus (self):
#    a = self.balance - self._n_number 
#    m = self.balance + a
#    print(m)
#  = Vito( 'VIto' , 'shon' , 455298533 , 50)
# vito.minus(vito)





##class Num ():
#  def __init__(self , num ):
#    self.num = num
#
#  def _get_num(self):
#    print(self.num)
#
#  def __add__(self , other):
#    print('is dunder method __add__ ')
#    self.num += other
#    self._get_num()
#  
#  def __sub__ (self , other):
#    print("i's method __sub__ ")
##    self._get_num()
#
##    print("i's method dunder __mul__")
#    self.num *= other
#    self._get_num()
#
#  def __floordiv__(self , other):
#    print("i's dunder method __floordiv")
#    self.num //= other
#    self._get_num
#
#  def __truediv__(self  ,other):
#    print("i's dunder mr=ethod __truediv")
#    self.num /= other 
#    self._get_num
#
#
#num = Num(65)
#num + 5
#
#
#class Num2():
#  def __init__(self , num):
#    self.num =num
#
#  def __add__(self , other):
#    print("i's dunder method __add__")
#    self.num += other
#    
#num2 = Num2(10)
#num / 10
#
#class Num3(Num):
#  pass
#
#num3 = Num3(10)
#num3 + 5






#class Builder():
#  def build(self):
#    print('build')
#
#class Doctor ():
#  def help(self):
#    print('help')
#
#class Programmers ():
#  
#  def build (self):
#    print( 'build programm')
#
#  def programming(self):
#    print('programming')
#
#class People(Builder , Doctor , Programmers):
#  pass
#
#jack = People()
#jack.build()
#jack.help()
#jack.programming()






#class Name():
#  def __init__(self , name , age , color ):
#    self.name = name
#    self.age = age 
#   self.color = color 
#  
#  def my_name(self):
#    print(f"hello my name is {self.name} , me a {self.age} age , and I {self.color}")
#
#
#name =  Name( 'alex' , 17 , 'white')
#name.my_name()





#import sqlite3
#connection = sqlite3.connect('db.sqlite3')
#cursor = connection.cursor()

"""
create

"""

#cursor.execute("""
#CREATE TABLE  directions (id INT NOT NULL PRIMARY KEY , title CHAR )""")


#cursor.execute("""
#CREATE TABLE groups (
#id INT NOT NULL PRIMARY KEY , 
#number INT , 
#FOREIGN KEY (direction_id) REFERENCES direction (id )
#)
#""")


#cursor.execute("""
#CREATE TABLE peoples (
#  id INT NOT NULL PRIMARY KEY , 
#  first_name CHAR 
#  last_name CHAR 
#  group_id INT , 
 # FIREIGN KEY (group-id) REFERENCES group(id)
#)
#""")



#cursor.execute("""
#INSERT INTO directions VALUES (1 , 'Python')
#""")

#cursor.close()
#connection.commit()




from datetime import datetime
import bisect
tdays = [19,49,80,110,141,173,204,
          235,256,296,327,356,366]
zod =["Capricorn","Aquarius","Pisces","Aries",
    "Taurus","Gemini","Crayfish","Leo",
        "Virgo","Libra","Scorpio",
        "Sagittarius","Capricorn"]
d = (int(input( 'введите первое значение ')))
m = (int(input('введите значение ')))
print(zod[bisect.bisect_left
         (tdays,(datetime(2020, m, d) - 
                 datetime(2019,12,31)).days)])