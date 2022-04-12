ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, ten))
ten_square = list(map(lambda x: x ** 2, evens))

print(evens)
print(ten_square)
def object_output(ten):
    while True:
            indx = input("Команда выход - 'q', Введите индекс: ")
            if indx == 'q':
                print('Программа завершена!')
                break
            try:
                print(ten[int(indx)])
            except:
                print(f"Только числа! или индекс с 0 по {len(ten) - 1}")
object_output(ten)
