from os import name, system
# asal mı kontrolü

def asal_mi(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


# e değerini belirle
def e_degeri(totient):
    for i in range(totient // 2, totient):
        if asal_mi(i) == True:
            return i

# d * e = 1 mod totient
def d_degeri(e, totient):
    for i in range(1, totient):
        temp = (1 + (i * totient))
        if temp % e == 0:

            return temp // e



# rsa
bulundu = False
while not bulundu:
    print("-----------------")
    p = int(input("p değerini girin: "))
    q = int(input("q değerini girin: "))
    e = int(input("e değerini girin: "))
    if (p > 9 and q > 9 and e > 9) :
        
        if  asal_mi(p) and asal_mi(q) and asal_mi(e):
            n = p * q
            print("(n = p * q) n değeri:", n)

            totient = (p-1) * (q-1)
            print("( totient = (p-1) * (q-1) )totient:", totient)

            if 1 < e < totient:
                print("(1 < e < totient) e değeri:", e)
            
                d = d_degeri(e, totient)
                print("(d * e = 1 mod totient) d değeri:", d)

                sayi = int(input("RSA ile şifrelemek istediğiniz sayıyı girin\n"))

                sifrele = (sayi ** e) % n
                bulundu = True
                print(sifrele ** d % n)
                
            else:
                print("e değeri 1 ile totient arasında olmalıdır")
        else:
            print("p, q veya e değerleri asal değil")
    else:
        print("p ,q ve e değerleri 10 dan büyük olmalıdır ")
        
    print()