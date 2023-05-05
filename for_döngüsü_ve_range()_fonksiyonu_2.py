while True:
    notunuz = input("notunuz: ")
    if not notunuz:
        print("Lutfen notunuzu girin!")
        quit()
    else:
        notunuz = int(notunuz)
    if notunuz not in range(101):
        print("Notunuz 1 ile 100 arasinda olmali!")
        quit()
    
    elif notunuz in range(90, 101):
        puan = "AA"
    elif notunuz in range(85, 89):
        puan = "BA"
    elif notunuz in range(80, 84):
        puan = "BB"
    elif notunuz in range(75, 79):
        puan = "CB"
    elif notunuz in range(70, 74):
        puan = "CC"
    elif notunuz in range(60, 69):
        puan =  "DC"
    elif notunuz in range(50, 59):
        puan =  "DD"
    elif notunuz in range(0, 49):
        puan =  "FF"
    
    print('puaniniz: ', puan)
    
    