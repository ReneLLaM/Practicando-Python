# declarar_diccionario 
mi_diccionario = {}
mi_diccionario_1 = dict()

#elementos de un diccionario {'clave': valor,}

mi_diccionario = {'nombre': "juan", 
                  'apellido': 'Perez', 
                  'edad': 30, 
                  'ubicacion': {'calle': 'calle 13', 
                                'ciudad': 'Bogota'}}

print(mi_diccionario)

#acceder a un elemento
mi_diccionario['nombre'] = 'Pedro'
print(mi_diccionario)

print(mi_diccionario['ubicacion']['ciudad'])

#agregar un elemento
mi_diccionario['telefono'] = '123456'
print(mi_diccionario)

#eliminar un elemento
del mi_diccionario['telefono']
print(mi_diccionario)

#eliminar el diccionario    
# del mi_diccionario

#metodos de los diccionarios
print(mi_diccionario.items())
print(mi_diccionario.keys())
print(mi_diccionario.values())


