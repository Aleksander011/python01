# lista = [1, 2, 3]
# print(type(lista))
# print(lista)
# print(lista[0])
# print(*lista)
# print(*lista, sep=",")

# for i in lista:
#     print(i)

# lista.sort()
# print(lista)
# lista.reverse()
# print(lista)

# print(lista.count(3))
# lista.remove(3)
# print(lista)

# lista.append(3)
# print(lista)

# print(len(lista))

# kontakty = {
#     "Ewa":987654321,
#     "Edward":123456789,
#     "Leon":132547589
# }

# print(kontakty["Ewa"])
# kontakty["Iza"] = 102938485

# for imie, numer in kontakty.items():
#     print("%s ma numer telefonu %d" %(imie, numer))

# kontakty.pop("Iza")
# print(kontakty.keys())
# print(kontakty.values())

# zbior1 = {1,2,3,4}
# zbior2 = {3,4,5,6}

# suma_zbiorow = zbior1.union(zbior2)
# print(suma_zbiorow)

# roznica_zbiorow = zbior1.difference(zbior2)
# print(roznica_zbiorow)

# czesc_wspolna = zbior1.intersection(zbior2)
# print(czesc_wspolna)

krotka = (1, 2, 3)
print(krotka)

krotka1 = 1, 2, 3
print(len(krotka))
print(krotka.count(1))

print(krotka[0])

a, b, c = krotka
print(a)

lista2 = [10, 20, 30, 40, 50, 60]
print(lista2[1:4])
print(lista2[:3])
print(lista2[3:])
print(lista2[::2])
print(lista2[-1])
print(lista2[::-1])