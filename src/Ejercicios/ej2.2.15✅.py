'''

Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

'''

suma_positivos = 0
numero = int(input("Introduce un número entero (0 para terminar): "))

while numero != 0:
    if numero > 0:
        suma_positivos += numero
    
    numero = int(input("Introduce otro número entero (0 para terminar): "))

print("La suma de todos los números positivos introducidos es:", suma_positivos)

