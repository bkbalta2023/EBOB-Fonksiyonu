def ebob (a,b):
    for i in range(a,0,-1):
        for y in range(b,0,-1):
            if a % i == 0 and b % y == 0 and i == y:
                return i


while True:
    a = int(input("EBOB'unu bulmak istediğiniz ilk sayıyı giriniz: "))
    b = int(input("EBOB'unu bulmak istediğiniz ikinci sayıyı giriniz: "))
    print("EBOB değeri = ",ebob(a,b))