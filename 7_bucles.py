#bucle while
#while condicion:
#    bloque de codigo
#    bloque de codigo

#contador = 0
# contador = contador + 1 -> contador += 1
# contador = contador - 2 -> contador -= 2
# contador = contador * 3 -> contador *= 3
# contador = contador / 2 -> contador /= 2


# -----------------------------
# numero = int(input("ingrese un numero: "))
# while contador <= numero:
#     if(contador == 3):
#         contador += 1
#         continue
#     print(contador)
#     contador += 1
    

#quiero imprimir todos los numeros menos los multiplos de 3
numero = int(input("ingrese un numero: "))
acumulador = 0
while acumulador <= numero:
    if acumulador % 3 == 0:
        acumulador += 1
        continue #esto no ejecuta las lineas que esta depues pero el bucle continua
    print(acumulador)
    acumulador += 1







