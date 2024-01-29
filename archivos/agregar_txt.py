import os
# Verificar y crear carpetas si no existen
if not os.path.exists("python/archivos"):
    os.makedirs("python/archivos")

with open("python/archivos/texto_omar.txt", 'a', encoding="UTF-8") as archivo:
    # Resto del código...
    archivo.write("\n")
    for i in range(5):
        archivo.write(f"Linea {i+1} agregada hsahha\n")