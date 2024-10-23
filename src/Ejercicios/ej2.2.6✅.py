'''

Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****

'''

n = int(input("Introduce un número entero como altura: "))
for i in range (0, n):
    print("*"*i)