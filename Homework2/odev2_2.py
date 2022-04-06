import difflib
import random
import hashlib as hasher


alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z"]
folder = open("paragraph.txt", "w", encoding="utf-8")



#metin = input("Metin Giriniz: ")
metin = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus."

def change_text(metin,alphabet):
    for i in range(len(metin)):
        encryption = hasher.md5()
        encryption.update(metin.encode("utf-8"))
        encryption_metin = encryption.hexdigest()

        rastgele_sayi = random.randint(0,len(alphabet)-1)
        a = alphabet[rastgele_sayi]
        metin = metin.replace(metin[i],a)
       
        
        #dosya.write(metin + ":" + encryption_metin + "\n")
        folder.write(encryption_metin + "\n")
  
        #with open("paragraph.txt", "a") as file:
        #   file.write(metin + ":" + encryption_metin + "\n")
    
change_text(metin,alphabet)
folder.close()


