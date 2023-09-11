import os
os.system ("cls")
class Telefon:
    def __init__(self,Model,Kamerasi,Xotirasi,Chiqarilgani,Rangi):
        self.name = Model
        self.camera = Kamerasi
        self.memory = Xotirasi
        self.data = Chiqarilgani
        self.color = Rangi
class Samsung(Telefon):
    def yaroqlilik(self):
        if self.Chiqarilgani > 3:
            return "Yaroqsiz"
    def narx(self):
        summa = (self.camera * 5) + (self.Xotirasi * 10)
        if self.color == "Oq":
            summa *= 1.5
        elif self.color == "Qora":
            summa *= 2
    def print(self):
        print(self.Model, self.Kamerasi, self.Xotirasi, self.Chiqarilgani, self.Rangi)
telefon1 = Telefon ("iPhone", "50", "1 TB", "2023", "Oq")
telefon2 = Telefon ("Huwawei", "48", "256 GB", "2020", "Qora")
telefon3 = Telefon ("Xiaomi", "56", "512 GB", "2016", "Ko`k")
telefon4 = Telefon ("Redmi", "32", "128 GB", "2010", "Sariq")
telefon5 = Telefon ("Siemens", "16", "512 MB", "2000", "Yashil")
telefon6 = Telefon ("Nokia", "8", "256 MB", "2005", "Oq")
telefon7 = Telefon ("Alcatel", "16", "1 GB", "2002", "Kulrang")
telefon8 = Telefon ("Motorola", "16", "256 MB", "2015", "Qizil")
telefon9 = Telefon ("Honor", "16", "32 GB", "2012", "Tillarang")
telefon10 = Telefon ("Vivo", "16", "64 GB", "2018", "Qora")