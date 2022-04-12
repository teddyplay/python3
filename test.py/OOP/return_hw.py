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



number = 555
running = True
while running :

    guess = int(input('введите пин код: , '))

    if guess == number:
        print( 'Да ,вы угадали со значением ! ')
        print('если желаете выйти нажмите "q')
        break
    
    elif guess < number :
        print ('нет число выше , гадай дальше')
    
    elif guess >  number :
        print ('нет число ниже ,гадай дальше')

    else:
        print (' что ты вообще ввел?')
        
    guess  = input('если желаете выйти нажмите - q ')
    if guess == 'q':
        print('программа завершена!')
        break