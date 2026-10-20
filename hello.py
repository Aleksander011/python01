# import random

# print("Hello world") #komentarz

# zmienna = 10
# print(type(zmienna))

# rzeczywista = 10.5
# print(type(rzeczywista))

# tekst = "hello world" 
# print(type(tekst))

# suma = 1 + 2
# roznica = 5 - 4
# iloczyn = 3 * 2
# iloraz = 4 / 2
# reszta = 5 % 2
# potega = 5 ** 2
# dzielenie_calkowite = 5 // 2
# print(suma, roznica, iloczyn, iloraz, reszta, potega, dzielenie_calkowite)

# print("wartość sumy to:", suma, "a wartość róznicy to:", roznica)
# print(f"wartość sumy to {suma}, a wartość róznicy to {roznica}")
# print("wartość sumy to: %.10f" %suma)

# imie = input("Jak masz na imię?")
# print("Cześć", imie)
# wiek = int(input("ile masz lat"))
# print(type(wiek))

# los = random.randint(1, 100)
# print(los)

# liczba = -5
# if liczba > 0:
#     print("liczba jest większa od 0")
# elif liczba == 0:
#     print("liczba jest równa 0")
# else:
#     print("liczba jest mniejsza od 0")
# if "tekst" in "bardzo podobny tekst":
#     print("prawda")
# else:
#     print("fałsz")

# a = 5
# b = 5

# if a is b:
#     print("prawda")
# else:
#     print("fałsz")


# for i in range(5):
#     print(i)

# for i in range(1, 100):
#     if i%2==0:
#         print(i)

# for i in range (1, 102, 2):
#     print(i)

# for i in range(100, 0, -1):
#     print(i)


# for litera in "slowo":
#     if litera =="o":
#         break
#     print(litera)

# for litera in "slowo":
#     if litera =="o":
#         continue
#     print(litera)


liczba = int(input("podaj liczbę całkowitą: "))
# while liczba <=0:
#     liczba = int(input("podaj liczbę całkowitą: "))
# print("podałeś liczbę całkowitą")

l=0
while l < 10:
    print(f"liczba jest równa {l}")

def powitanie():
    print("Cześć", imie)

def powitanie_imienne(x):
        print("Cześć", x)

powitanie()
powitanie_imienne("Jacek")

def dzielenie(dzielna, dzielnik):
    if dzielnik == 0:
        return "Nie mozna dzielić przez 0"
    else:
        return dzielna/dzielnik

print(dzielenie(10, 5))
iloraz = dzielenie(4, 2)
print(iloraz)

print(dzielenie(4, 0))
