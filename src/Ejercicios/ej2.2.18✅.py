'''

Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de 
los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, 
mostrar cuántos de los números ingresados por el usuario fueron números pares.

'''

contador_pares = 0
continuar = True

while continuar:
    numero = int(input("Introduce un número entero positivo (-1 para terminar): "))
    
    # Verificar la condición de corte
    if numero == -1:
        continuar = False  # Cambiar la variable de control para terminar el bucle
    else:
        # Verificar si el número es positivo
        if numero < 0:
            print("Por favor, ingresa un número entero positivo o -1 para terminar.")
        else:
            # Calcular la suma de los dígitos
            suma_digitos = sum(int(digito) for digito in str(numero))
            print(f"La suma de los dígitos de {numero} es: {suma_digitos}")
            
            # Verificar si el número es par
            if numero % 2 == 0:
                contador_pares += 1

# Mostrar el resultado final
print(f"Se ingresaron {contador_pares} números pares.")