# if (condicion):
#     Bloque de código
#     Bloque de código
# else:
#     Bloque de código

edad = 11
#solo se ejecuta una condicion si 2 son verdaderas se ejecuta la primera
if edad >= 18:
    print("Es mayor de edad")
    if edad > 60:
        print("Es un adulto mayor")
elif edad >= 13 and edad < 18:
    print("Es menor de edad")
    print("Es un adolescente")
else:
    print("Es menor de edad")
    if (edad < 13):
        print("Es un niño")
    

    
 