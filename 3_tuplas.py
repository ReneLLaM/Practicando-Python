tupla_1 = (1, 2, 3, 4)
lista = [1, 2, 3, 4]

lista[0] = 5
print(lista)

#tupla_1[0] = 5
print(lista)

string_1 = "nuevo"
string_1 = "Nuevo"
print(string_1)

#sacar partes de una tupla
#[inicio= : fin< : salto -1reversa]
print(tupla_1[:2])
print(tupla_1[2:])
print(tupla_1[-1::-1])
print(tupla_1)

#metodos para tuplas
print(len(tupla_1))

#transformar la tupla en lista
tupla_1 = list(tupla_1)
print(tupla_1)
tupla_1.append(5)
tupla_1 = tuple(tupla_1) #transformando la lista en tupla
print(tupla_1)

#eliminar una tupla
del tupla_1
print(tupla_1)