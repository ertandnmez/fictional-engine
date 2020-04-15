import winsound
import random

def alarm():
    for i in range(0,1):
        winsound.Beep(1000 , 500 )

def alarm2():
    for i in range(0,3):
        winsound.Beep(1250, 250)

print("""
*************************************************
SAYI BULMA OYUNUNA HOŞGELDİNİZ...

3 HAKKINIZ VAR

İYİ EĞLENCELER...
*************************************************
""")

hak = 4
bul = random.randint(0,50)
while True:
    sayı = int(input("Tahmininizi Giriniz:\n "))

    if sayı == bul:
        print("Tebrikler Oyunu Kazandınız...")
        break
        
    elif sayı < bul:
        print("Daha yükseğe çık!")
        hak -= 1
        alarm()

    elif sayı > bul:
        print("Daha aşağı in!")
        hak -= 1
        alarm()

    

    if hak == 0:
        print("Tahmin Hakkınız Kalmadı...")
        print("Kaybettiniz!!!")
        alarm2()
        break
