import qrcode 

import qrcode

# Solicitar al usuario que introduzca un dato
cosa = input("Introduce algo (URL, texto, etc.): ")

nombre = input("Introduce el nombre del archivo QR: ")

# Generar el código QR
img = qrcode.make(cosa)

# Guardar la imagen del QR en el archivo especificado
img.save(f'C:\\Users\\USUARIO\\Desktop\\VISUAL\\1\\{nombre}.png')

print("El código QR ha sido generado y guardado en el archivo qr.png")
    