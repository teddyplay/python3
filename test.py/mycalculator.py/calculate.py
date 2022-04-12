while True:

    what = (input(' Привет ^_^ , меня зовут "калькулятор" , и я умею считать некоторые операции )) \n Введите  действие пожалуйста : + , - , * , / :'))
    if what == "+":
        a = float(input())
        b = float(input())
        c = a + b 
        print('результат вычисления суммы двух чисел:' + str(c))
    elif what == "-":
        a = float(input()) 
        b = float(input())  
        c = a - b
        print('результат разности двух чисел:' + str(c))
    elif what == '*':
        a = float(input())
        b = float(input())
        c = a * b 
        print('результат умножения двух чисел:' + str(c))
    elif what == "/":
        print (' Извините но на ноль делить нельзя )))')
        a = float(input())
        b = float(input())
        c = a / b 
        print('резултат деления двух чисел:' + str(c))
    else:
        print(' извините , такого я ещё не умею ')
