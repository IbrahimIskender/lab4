import random 

#entry
print('''Merhaba, hos geldiniz. Bu program ile herhangi iki sayi araligindan
 rastgele bir sayi urete bilirsiniz. (ilk sayi sifirdan buyuk olmali)''')
print("Programdan cikmak icin Q tusuna basin.")

#conditions
while True:
    first_number = int(input("ilk sayiyi yazin: "))
    
    if first_number < 1:
        print("ilk sayi sifirdan buyuk olmali")
        continue
    elif first_number == "":
        quit()
    last_number = int(input("son sayiyi girin: "))
    
    if last_number < first_number:
        print("Lutfen ilk sayiyi buyuk, son sayiyi kucuk yaziniz. ")
        continue
    
#result
    print("rastgele sayi uretiliyor... ")
    print(first_number, "ile", last_number, "arasindan",
    random.randint(first_number, last_number), "sayisi uretildi" )
