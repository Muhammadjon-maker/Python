import os
os.system ("cls")

MORSE = {"-----" : "0", ".----" : "1", "..---" : "2", "...--" : "3", "....-" : "4", "....." : "5",
         "-...." : "6", "--..." : "7", "---.." : "8", "----." : "9"}
find = input("Morse kiriting!")
try:
    if find == "-----":
        print(0)
except:
    print("Qaytadan kiriting!")