'''

Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1

'''

n = int(input("Introduce un número entero: "))
for i in range (0, n):
    numero = list(range(2*i-1, 0, -2))
    print (" ".join(map(str, numero)))   #map() transforma los numeros enteros en cadenas#

                                        #.join() hace que cada numero convertido en cadena sea separado 
                                        #por un espacio ya que entre las comillas hay un espacio#