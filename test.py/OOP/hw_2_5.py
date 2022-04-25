import re 

valid_phone_number = input('введите номер машины  \nПример: 01KG777BMW:')

valid = re.search(r"[0-7]+(KG)+([0-9]{3})+(BMW|AUDI)",valid_phone_number)
print(valid)