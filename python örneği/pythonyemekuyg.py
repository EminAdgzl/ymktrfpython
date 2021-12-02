# Kullanıcıdan Yemek Adı ve Tariflerini Alan Kodlar

print(" Ben Mehmet Emin Adıgüzel. Yemek Tariflerine Hoşgeldiniz :)")

# Gerekirse Kullanılabilecek Kodlar
#yemek=input("Yemek Adı Giriniz =")
#ymktarifi=input("Yemek Tarifini Yazınız=")

# Alınan Bilgileri txt Dosyasına Yazdırma

kayıt = open("yemektarifleri.txt", "w") 
kayıt.write(input(  "Yemek Adı Giriniz = " )) 
kayıt.write(input( "Yemek Tarifi Giriniz = " ))
kayıt.close()

dosya = open("yemektarifleri.txt","r",encoding="utf-8")
oku = dosya.read()
print("Yemek Adı ve Tarifiniz = " ,oku)