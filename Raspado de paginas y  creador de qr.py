import urllib.request
from bs4 import BeautifulSoup
from collections import Counter
import qrcode
import os

print("1. Generar un codigo QR")
print("2. Raspar paginas web")
print("3. Salir")
menu = input ("Digite el tipo de operacion que desea generar: ")
if menu == "1":
    cosa = input("Introduce algo (URL, texto, etc.): ").strip()
    if not cosa:
        print("Error: No se ha introducido ningún dato.")
        exit()
    nombre = input("Introduce el nombre del archivo QR (sin extensión): ").strip()
    if not nombre:
        print("Error: No se ha introducido un nombre para el archivo.")
        exit()
    directorio = input("Introduce la ruta donde deseas guardar el archivo (deja vacío para usar el escritorio): ").strip()
    if not directorio:
        directorio = os.path.join(os.path.expanduser("~"), "Desktop")
    ruta = os.path.join(directorio, f"{nombre}.png")
    if not os.path.exists(directorio):
        print(f"Error: La carpeta {directorio} no existe.")
        exit()
    try:
        img = qrcode.make(cosa)
        img.save(ruta)
        print(f"El código QR ha sido generado y guardado en: {ruta}")
    except Exception as e:
        print(f"Error al generar el código QR: {e}")
elif menu == "2":
    url = input('Enter - ')
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        print("Links:", tag.get('href', None))
    print("Cantidad de links: ", len(tags))
    print("Cantidad de links unicos: ", len(Counter(tags)))
    print("Cantidad de links repetidos: ", len(tags) - len(Counter(tags)))
    print("Deseas guardar los links en un archivo de texto?")
    print("1. Si")
    with open("links.txt", "w") as file:
        for tag in tags:
            file.write(f"Links: {tag.get('href', None)}\n")
    print("Archivo guardado")
    print("Deseas vizualizar el texto de los links?")
    print("1. Si")
    print("2. No")
    if input == "1":
        for tag in tags:
            print("Links:", tag.get('href', None))
    elif input == "2":
        exit()
elif menu == "3":
    exit()




