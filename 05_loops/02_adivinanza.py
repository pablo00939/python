# Pablo Tapia 
# 26-04-2025

import random

numero_secreto = random.randint(1, 100)
intentos = 0
limite_intentos = 5

print("¡Bienvenido al juego de adivinanza!")
print(f"Tienes un máximo de {limite_intentos} intentos para adivinar el número.")

while intentos < limite_intentos:
    try:
        adivinanza = int(input("Adivina el número (entre 1 y 100): "))
        intentos += 1

        if adivinanza == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
        elif adivinanza < numero_secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")
    except ValueError:
        print("Por favor, introduce un número válido.")

if intentos == limite_intentos and adivinanza != numero_secreto:
    print(f"Lo siento, has alcanzado el límite de intentos. El número era {numero_secreto}.")