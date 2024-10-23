'''

Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
la cuenta atrás desde ese número hasta cero separados por comas.

'''

positivo = int(input("Introduce un número entero positivo: "))
print("La cuenta atrás de ese número hasta el 0 es:")
for positivo in range (positivo, 0, -1):  #positivo: nº a partir del cual se recorre / 0: nº hasta el cual se recorre / -1: de cuanto en cuanto se recorre, +/- depende si es hacia adelante o atrás#
    print(positivo)