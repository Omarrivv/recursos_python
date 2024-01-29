
# abriendo el archivo con witch open 
with open("python/archivos/texto_omar.txt",encoding="UTF-8") as archivo:
    #leemos el archivo
    contenido = archivo.read()
    print(contenido)