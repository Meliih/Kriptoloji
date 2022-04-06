import hashlib as hasher


while True:
    print("--------------------------------")
    print("1.Kullanıcı Ekle ")
    print("2.Kullanıcı Girişi")
    print("Çıkış için q'ya basınız")
    selected_button = input() 
    if selected_button == "q":
        break    
    userName = input("Kullanıcı Adınızı Giriniz:")
    password = input("Şifrenizi Giriniz:")
    encryption = hasher.sha256()
    encryption.update(password.encode("utf-8"))
    password = encryption.hexdigest()

    if int(selected_button) == 1:
        with open("users.txt", "a") as file:
            file.write(userName + ":" + password + "\n")
        
    elif int(selected_button) == 2:
        with open("users.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line[:-1]
                dbUserName = line.split(":")[0]
                dbPassword = line.split(":")[1]
                print(dbUserName)
                print(dbPassword)
                print(userName)
                print(password)
                if dbUserName == userName and dbPassword == password:
                    print("Giriş Başarılı")
                    break
                else:
                    print("Kullanıcı Adı veya Şifre Hatalı")
                    
   