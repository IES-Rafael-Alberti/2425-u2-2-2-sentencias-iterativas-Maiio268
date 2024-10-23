'''

Escribir un programa que pida al usuario una palabra y luego muestre por pantalla 
una a una las letras de la palabra introducida empezando por la última.

'''

palabra = input("Introduce una palabra: ")


for letra in palabra[::-1]: #Al dejar inicio y fin vacíos y poner el rango -1, automáticamente empieza desde atrás#
    print(letra)
