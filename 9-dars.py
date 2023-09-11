import os
os.system ("cls")
class Car:
    def _init_(self, brand, color, speed, cost):
        self.nomi = brand
        self.rangi = color
        self.tezligi = speed
        self.narxi = cost
    def start(self):
        print("1.2 sec")
    def stop(self):
        print("5 sec")
    def distance(self):
        print("500 km")
    def tolerant(self):
        print("5 ton")
car1 = Car("Mercedes Benz", "Black", "320 km", "100 000 dollar")
car2 = Car("BMW", "White", "300 km", "60 000 dollar")
car3 = Car("Cadillac", "Blue", "320 km", "50 000 dollar")
car4 = Car("Porshe", "Red", "350 km", "100 000 dollar")
class Lalaku:
    pass
class Lakatum:
    def __init__(self) -> None:
        pass
class Car:
    def _init_(self, brand):
        self.brand = brand