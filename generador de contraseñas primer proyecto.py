import random
import string
print("Generador de contraseñas: ")
print("_"*100)
print("Este programa generará una contraseña segura para ti, solo sigue las instrucciones.")
print("_"*100)
print("Instrucciones: ")
numcontraseñas = int(input("¿Cuántas contraseñas deseas generar? "))
print("_"*100)
print("Digite la longitud de la contraseña: ")
longitud = int(input())
print("_"*100)
print("Generando contraseñas...")
print("_"*100)
caracteres = string.ascii_letters + string.digits + string.punctuation
for i in range(numcontraseñas):
    contraseña = "".join(random.choice(caracteres) for l in range(longitud))
    print(f"Contraseña {i+1}: {contraseña}")
print("_"*100)
with open("contraseñas.txt", "w") as file:
    for i in range(numcontraseñas):
        contraseña = "".join(random.choice(caracteres) for k in range(longitud))
        file.write(f"Contraseña {i+1}: {contraseña}\n")
        print(f"Contraseña {i+1}: {contraseña}")
print("Contraseñas guardadas en el archivo contraseñas.txt")
print("_"*100)
print("¡Gracias por usar nuestro generador de contraseñas!")
print("_"*100)