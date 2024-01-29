archivo_permiso = open("python/archivos/texto_omar.txt", encoding="UTF-8")
# archivo = archivo_permiso.read() leer archivo completo
lineas = archivo_permiso.readlines()  # con readline(es para leer lo que  esta con una sola linea ) pero con readlines(['si te sirve este block de notas buena que te ayude \n', 'ayuda a otras personas el conocimiento es para enseñar a los demas que \n', 'te quieran a escuchar\n']) nos lo dara en un array
# y lo podemos poner sus rangos (100) etc
print(lineas)