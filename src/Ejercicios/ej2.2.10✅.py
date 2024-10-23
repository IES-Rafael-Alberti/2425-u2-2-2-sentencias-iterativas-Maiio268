'''

Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

'''

n = int(input("Introduce un número entero: "))

# Verificar si el número es primo (sin usar funciones puras)
if n < 2:
    primo = False  # Los números menores que 2 no son primos
else:
    primo = True  # Suponemos que es primo hasta que se demuestre lo contrario
    for i in range(2, int(n ** 0.5) + 1):  # Probar divisores desde 2 hasta la raíz cuadrada del número
        if n % i == 0:
            primo = False  # Si es divisible por algún número, no es primo
            
if primo:
    print(f"{n} es un número primo.")
else:
    print(f"{n} no es un número primo.")