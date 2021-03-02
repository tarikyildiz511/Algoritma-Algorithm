# bir sayının karesini bulma algoritması
n = int(input("Num:"))

def karesi():
    print(n*n)
karesi()
# sıcaklık algoritması
su = int(input("Degree:"))

if su >=100:
    print(f"Kaynar Su {su} derece")
elif su <0:
    print(f"Buzlu Su {su} derece")
else:
    print(f"Su {su} derece")


#su kaynatan ve donduran robot

en = int(input("Kaç Derece Olsun? : "))
while True:

    if en <0:
        print("Donduruyorum")
        break
    elif en>=100:
        print("Kaynatıyorum")
        break
    else:
        print("Ilık Servis ediyorum")
        break
# üçgenin alanını bulan algoritma
yuk = int(input("Yükseklik:"))
tab = int(input("Taban:"))
alan = tab*yuk/2
print(alan)

