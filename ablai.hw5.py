contacts = [
    {'name': 'Geektech', 'phone': '0507052018'},
    {'name': 'Police', 'phone': '911'},
    {'name': 'Fire Department', 'phone': '101'},
]
def show_all_contact(lst):
    for i in lst:
        print(*i.values())

def search(name):
    for i in contacts:
        if name == i['name']:
            return i
    else:
        return False

def search2(phone):
    for i in contacts:
        if phone == i['phone']:
            return i
    else:
        return False

def create(lst):
    show_all_contact(contacts)
    for i in lst:
        name = input('введите имя: ')
        phone = input('введите номер: ')
        n = dict(name=name.title(), phone=phone)
        lst.append(n)
        if i['phone'] == phone:
            print("такой номер уже есть!\n")
        elif i['name'] == name:
            print("такое имя уже есть!\n")
        else:
            show_all_contact(contacts)
            break

def edit(name):
    if search(name):
        new_n = input('введите новое имя: ').title()
        new_p = input('введите новой номер: ')
        if search(new_n) or search2(new_p):
            print('такое имя или номер есть!')
        else:
            contacts[contacts.index(search(name))]['name'] = new_n
            contacts[1]['phone'] = new_p

def delete(lst):
    show_all_contact(contacts)
    name = input('Введите имя для удаления:')
    for i in lst:
        if i['name'] == name:
            lst.remove(i)
            show_all_contact(contacts)
            break

while True:
    show_all_contact(contacts)
    option = input('Команды: \n'
                   '1) создание\n'
                   '2) изменение\n'
                   '3) удаление\n'
                   '4) выход\n')
    if option == '1':
        create(contacts)
    elif option == '2':
        n = input('Enter name here: ').title()
        edit(n)
    elif option == '3':
        delete(contacts)
    elif option == "4":
        print('программа завешена!')
        break
    else:
        print('нет такой команды!')
        