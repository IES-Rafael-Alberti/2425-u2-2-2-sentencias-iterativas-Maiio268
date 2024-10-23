'''

Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. 
Informar cuál fue el mayor número ingresado.

'''

mayor = None
n = int(input("Introduce un número entero positivo (Introduce el 0 para terminar): "))

while n != 0:
    if mayor is None or n > mayor:
        mayor = n
    n = int(input("Introduce otro número entero positivo (Introduce el 0 para terminar): "))

#Comprobar cuál es el mayor#
if mayor is None: 
    print("No se ingresaron números.")
else:
    print("El mayor número ingresado fue:", mayor)