'''

Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
Finalmente, mostrar la sumatoria de todos los números ingresados.

'''

suma_total = 0
numero = int(input("Introduce un número entero (0 para terminar): "))

while numero != 0:
    suma_total += numero  
    numero = int(input("Introduce otro número entero (0 para terminar): "))

print(f"La sumatoria de todos los números ingresados es: {suma_total}")