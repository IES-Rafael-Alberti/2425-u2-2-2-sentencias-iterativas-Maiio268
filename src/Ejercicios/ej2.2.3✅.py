'''

Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
todos los números impares desde 1 hasta ese número separados por comas.

'''

positivo = int(input("Introduce un número entero positivo: "))
print("Los números impares desde 1 hasta el número introducido son:")
for positivo in range (1, positivo, 2):
    print(positivo)