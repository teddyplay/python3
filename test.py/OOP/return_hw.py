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


if __name__ == "__main__":
    print ('эта программа запущена самам по себе')
else :
    print('нет его запустили насилльно')


