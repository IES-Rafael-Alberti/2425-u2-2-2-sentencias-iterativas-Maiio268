'''

Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

'''

eco = input("Introduce algo (escribe 'salir' para terminar): ")

while eco.lower() != "salir":
    print(eco)  
    eco = input("Introduce algo (escribe 'salir' para terminar): ") 

print("Programa terminado.")