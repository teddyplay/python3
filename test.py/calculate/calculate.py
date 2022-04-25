while True:

    what = (input('Введите  действие : + , - , * , / :'))
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
        print ('На ноль делить нельзя!')
        a = float(input())
        b = float(input())
        c = a / b 
        print('резултат деления двух чисел:' + str(c))
    else:
        print('такой команды нет в списке ! ')
