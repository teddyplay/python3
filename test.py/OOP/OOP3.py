# # # # реализовать операцию над дробью, то есть создать класс Fraction у него будет 
# # # # 2 атрибута (numertor, denumerator)
# # # # сделать add, sub, mul, floordiv (Dunder Methods)
# # # # по правилам математики!)

# # # # #ExtraTask:

# # # # Учитывая целое число x, вернуть, true если x это целое число палиндрома.

# # # # К сведению: Целое число является палиндромом , если оно читается так же, как в прямом, так и в обратном порядке.

# # # # Например, 121 есть палиндром, а 123 нет.


# """
# EXTRA TASK
# """

a = input('Enter the numbers: ')
a = str(a)
copy_a = a[::-1]

if a == copy_a:
    print(True)
else:
    print(False)





class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if type(other) == int:
            print(f'{other}({self.numerator}/{self.denominator})')
        elif type(other) == float:
            print(f'{self.numerator / self.denominator + other}')

    def __sub__(self, other):
        if type(other) == int:
            print(f'{other - self.numerator / self.denominator}')
        elif type(other) == float:
            print(f'{self.numerator / self.denominator - other}')

    def __mul__(self, other):
        if type(other) == int:
            print(f'{other * self.numerator}/{1 * self.denominator}')
        elif type(other) == float:
            print(f'{self.numerator / self.denominator * other}')

    def __floordiv__(self, other):
        if type(other) == int:
            self.denominator *= other
            print(f'{self.numerator // self.denominator}')
        elif type(other) == float:
            print(f'{(self.numerator / self.denominator) // other}')


F = Fraction(10, 5)
F.__add__(5)