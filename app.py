import random
restart = [1]
for e in restart:
    number = random.randint(1,100)
    for i in range(1,7):
        userinput = int(input("1 ile 100 arası bir sayı tahmin et "))
        if number != userinput :
            if i == 5:
                altLimit = random.randint(1,6)
                üstLimit = random.randint(1,6)
                print(f"Son hakkın Sayı {number-altLimit} ile {number+üstLimit} aralığındadır.")
            elif i < 5:
                if number < userinput:
                    print("Daha düşük bir sayı yaz")
                else:
                    print("Daha yüksek bir sayı yaz")
        else:
            print(f"Tebrikler doğru sayıyı buldun: Sayımız: {number}")
            break
    else:
        print(f"Malesef doğru sonuca bulamadın, Sayımız: {number}")
    Reset = input("Tekrar oynamak için (r) harfine, çıkış için (q) ya basın ")
    if Reset == "r":
        restart.append(1)
    elif Reset == "q":
        break
    
    
    
# ** Bilgisayar Bulmaya çalışsın..
 
import random
restart = [1]
for e in restart:
    userinput = int(input("1 ile 100 arası bir sayı belirle. "))
    low,high= 1, 100
    
    for i in range(1,9):
        pc = random.randint(low,high)
        print(f"Bilgisayarın Tahmini: {pc}")
        if pc != userinput :
            if i < 8:
                if pc < userinput:
                    print("Daha yüksek bir sayı tahmin et.")
                    low = pc + 1
                else:
                    print("Daha düşük bir sayı tahmin et.")
                    high = pc - 1
        else:
            print(f"Tebrikler doğru sayıyı buldun: Sayımız: {userinput}")
            break
    else:
        print(f"Malesef doğru sonuca bulamadın, Sayımız: {userinput}")
    Reset = input("Tekrar oynamak için (r) harfine, çıkış için (q) ya basın ")
    if Reset == "r":
        restart.append(1)
    elif Reset == "q":
        break
    


    
    

