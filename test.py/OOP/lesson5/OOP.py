#import re 
"""
re - regular expressions 
"""

"""title.test.com"""

"""
(gmail|mail|yandex)
"""

"""
[a-zA-Z0-9]
"""

"""
(com|ru)
"""



#email = input("email: ")
#is_valid = re.search(r"[a-zA-Z0-9]+@(gmail|mail|yandex)\.(com|ru)" , email)
#print(is_valid)

#phone = input('phone number:')
#is_valid = re.search(r"\+996-([0-9]{1,3})-([0-9]{2})",phone)
#print(is_valid)




"""lesson 6"""


#mass = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ,10]
#def algo(arr , target):
##    for i in range(len(arr)):
 ##       if arr[i] == target:
 #           print(i)
##
##algo(mass, 5)
#
#
#"""
#Big O(5)
#"""





#def sum_(arr):
#    total = 0
#    step = 0
#
#    for i in arr:
#        step += 1 
#        total += i
#        print(total , f"big o ({step})")
#sum_(mass)



#duplicatedMass = [ 1,2,4,5,6,7,8,9,10,10]
#
#def f1(mass):
#    for i in range(len(mass)):
#        for j in range(i +1 , len(mass)):
#            step += 1
#            if mass[i] == mass[j]:
#                print(i , j , f"Big O ({step})")
#
#f1(duplicatedMass)
#
#
#"""
#Big O ()
#"""




""" Lesson 7 """

#obj = {
#    'vadim' : 500,
#    'sasha' : 650,
##    'bados' : 750,
#    'bob': 879,
#    'harley': 900
#}
#
#name = input ('please enter thr name :')
#print(name  , obj[name])
#
#"""
#
#Big O(n)
#
#"""


dict_ = {
    "q": "й",
    "w": "ц",
    "e": "у",
    "r": "к",
    "t": "е",
    "y": "н",
    "u": "г",
    "i": "ш",
    "o": "щ",
    "p": "з",
    "[": "х",
    "]": "ъ",
    "a": "ф",
    "s": "ы",
    "d": "в",
    "f": "а",
    "g": "п",
    "h": "р",
    "j": "о",
    "k": "л",
    "l": "д",
    ";": "ж",
    "'": "э",
    "z": "я",
    "x": "ч",
    "c": "с",
    "v": "м",
    "b": "и",
    "n": "т",
    "m": "ь",
    ",": "б",
    ".": "ю",
    "`": "ё",
    "й": "q",
    "ц": "w",
    "у": "e",
    "к": "r",
    "е": "t",
    "н": "y",
    "г": "u",
    "ш": "i",
     "щ": "o",
     "з": "p",
     "х": "[",
     "ъ": "]",
     "ф": "d",
     "ы": "s",
     "в": "d",
     "а": "f",
     "п": "g",
     "р": "h",
     "о": "j",
     "л": "k",
     "д": "l",
     "ж": ";",
     "э": "'",
     "я": "z",
     "ч": "x",
     "с": "c",
     "м": "v",
     "и": "b",
     "т": "n",
     "ь": "m",
    "б": ",",
     "ю": ".",
     "ё": "`"
}

word = input('enter the name:')
print(dict_[word])



