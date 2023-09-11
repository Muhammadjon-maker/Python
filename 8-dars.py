import os
import math
os.system("cls")


# a = ['sdfgh', 'kdfttt']
# for i in a:
#     if i[0] == "k":
#         print(i)

# 2 V 1 problem 
# sozlar = input("So'zlar kiritng: ").split()
# for soz in sozlar:
#         if soz.startswith('k'):
#             print(soz)

# def tartibla_satr(satr):
#     sozlar = satr.split()
#     if len(sozlar) <= 1:
#         return satr
    
#     birinchi = sozlar[0]
#     oxirgi = sozlar[-1]
#     qolgan = ' '.join(sozlar[1:-1])
    
#     teskari_tartib = birinchi[::-1] + ' ' + qolgan + ' ' + oxirgi[::-1]
#     return teskari_tartib

# satr = input("Istalgan uzunlikdagi satrni kiriting: ")
# natija = tartibla_satr(satr)
# print("Natija:", natija)

# i = 0
# numlist = []
# sum=0
# # print(sum(numlist))
# print("sonlar kiriting: (to'xtatish uchun 'c' ni kiriting:)")
# while True:
#     n = input(f"{i+1} --> ")
#     i+=1
#     if n == 'c':
#         break
#     else:
#         num = int(n)
#         numlist.append(num)
#         sum+=num
# print("siz kiritgan sonlar -->",numlist)
# print("sonlar yig'indisi -->",sum)

# # V 2 2 
# satr = input("Satrni kiriting: ")
# sozlar = satr.split()
# sozlar.sort()
# for soz in sozlar:
#     print(soz)a

# a = ['sdfgh', 'kdfttt', "df jhgfghjhghjhgf", "kfsdxtgdfhjjk"]
# for i in a:
#     if i[0] == "k":
#         print(i)

# # V2 4
# sozlar = input("So'zlarini kiriting: ").split(" ")

# with open("so'zlar.txt", 'w') as fayl:
#     for soz in sozlar:
#         fayl.write(soz + '\n')

# juftlar = []
# toqlar = []

# for soz in sozlar:
#     if len(soz) % 2 == 0 and soz != soz.capitalize():
#         juftlar.append(soz)
#     elif len(soz) % 2 != 0 and soz == soz.capitalize():
#         toqlar.append(soz)

# with open("juft.txt", 'w') as fayl:
#     for i in juftlar:
#         fayl.write(str(i) + '\n')

# with open("toq.txt", 'w') as fayl:
#     for i in toqlar:
#         fayl.write(str(i) + '\n')

# fayl.close()

# dct = {
#     "key1": "input1",
#     "key2": "input2",
#     "key3": "input3",
        
# }
# for i in dct.keys():
#     dct[i] = input("kiriting : ")

# print(dct)