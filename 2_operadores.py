
#operadores con numeros
print("------operadores con numeros------")
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)
print(2 % 3) #residuo o modulo
print(2 ** 3) #exponente
print(5 // 2) #division entera

print ("------strings-----------")
print("hola mi nombre es " + "rene")
nombre = "Rene"
apellido = "llanos"
edad = 26
print("hola mi nombre es: " + nombre + " " + apellido + " y tengo " + str(edad) + " años")
print("hola mi nombre es: {} {} y tengo {} años".format(nombre, apellido, edad))
print("hola mi nombre es: %s %s y tengo %s años"%(nombre, apellido, edad))
print(f"hola mi nombre es: {nombre} {apellido} y tengo {edad} años")

print(nombre*3)


#operadores de comparacion
print("operadores de comparacion")
print(3>2)
print(3<2)
#>= <= == !=

print("hola" == "hola")
print("aaa" < "aaaa") #se toma en cuenta el orden alfabetico y el tamaño del string



#operadores logicos
print("---------operadores logicos-----------------")
print(not(True and False) or (5 > 2 and False))
#numeros que estén en un rango diferente de 5 a 10 incluidos ambos
num = 7
print(not(num >= 5 and num <=10))




