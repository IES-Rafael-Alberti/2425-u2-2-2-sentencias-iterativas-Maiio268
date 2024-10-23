'''

Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.

'''

n = input("Introduce un número entero positivo: ")
suma_digitos = 0

for digito in n:
    suma_digitos += int(digito)  #Se convierte el carácter a entero#

print(f"La suma de los dígitos es: {suma_digitos}")