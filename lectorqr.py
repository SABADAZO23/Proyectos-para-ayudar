import qrcode
import os


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