'''

Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario 
por la contraseña hasta que introduzca la contraseña correcta.

'''

contraseña = "contraseña"
contraseña_introducida = input("Introduce la contraseña: ")

if contraseña == contraseña_introducida:
    contraseña_introducida = True
    print("Contraseña introducida correcta")
else:
    contraseña_introducida = False


while not contraseña_introducida == True:
    print("Contraseña introducida incorrecta, por favor introduce de nuevo la contraseña")
    contraseña_introducida = input("Introduce la contraseña: ")