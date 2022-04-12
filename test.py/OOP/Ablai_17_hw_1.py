"""

class -

"""
from tkinter import N
from turtle import title


d = {
    "key": "value"
}
""" dict """

class Bmw:
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max = max_speed
        self.color= color
      

    def start_engine(self):
        print (f"{self.title} {self.model}")

    def stop_engine(self):
        print (f"{self.title} {self.model}")
    def info(self):
        print(f"title:{self.title}\n"
                f"model:{self.model}\n"
                f"weight:{self.weight}\n"
                f"hp:{self.hp}\n"
                f"nm:{self.nm}\n"
                f"max speed:{self.max}\n"
                f"color:{self.color}\n")
bmw1 = Bmw('output CarTitle ' , 'Car Model engine stoped! m5', 1500, 560, 700, 1500, "green")
bmw1.start_engine()
bmw1.stop_engine()
bmw1.info()

class Mercedec:
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max = max_speed
        self.color= color
      

    def start_engine(self):
        print (f"{self.title} {self.model}")

    def stop_engine(self):
        print (f"{self.title} {self.model}")
    def info(self):
        print(f"title:{self.title}\n"
                f"model:{self.model}\n"
                f"weight:{self.weight}\n"
                f"hp:{self.hp}\n"
                f"nm:{self.nm}\n"
                f"max speed:{self.max}\n"
                f"color:{self.color}\n")
mercedec1 = Mercedec('output CarTitle ' , 'Car Model engine stoped! s class', 1600, 560, 650, 1750, "white")
mercedec1.start_engine()
mercedec1.stop_engine()
mercedec1.info()
