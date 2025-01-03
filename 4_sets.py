mi_set = set()
print(type(mi_set))

mi_set = {1, 2, 2, 3, 4, 4}
print(mi_set)   #no se añaden repetidos


mi_lista = [1, 2, 2, 3, 4, 4]
mi_lista = set(mi_lista)
mi_lista = list(mi_lista)
print(mi_lista)

#metodo para agregar elementos
mi_set.add(5)
print(mi_set)

# buscar un elemento en el set in
print(5 in mi_set)

#eliminar un elemento
mi_set.remove(1)
print(mi_set) #los sets no tienen orden

#eliminar todos los elementos
mi_set.clear()
print(mi_set)

#eliminar el set
del mi_set
#print(mi_set) #error porque el set ya no existe


#operaciones con sets
set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}

#union
print(set_1 | set_2) #union
print(set_1.union(set_2))
#interseccion
print(set_1 & set_2)
print(set_1.intersection(set_2))
#diferencia simetrica
print(set_1 ^ set_2) #{1, 2, 5, 6}
print(set_2 - set_1) #{5, 6}
print(set_1.difference(set_2))#{1, 2}