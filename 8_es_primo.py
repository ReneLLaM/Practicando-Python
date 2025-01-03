numero = int(input("ingrese un numero: "))
contador = 2
while(contador < numero):
    if(numero % contador == 0):
        print("no es un numero primo")
        break # esto finaliza el bucle
    contador += 1


    
    