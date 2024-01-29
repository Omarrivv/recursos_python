with open("python\\archivos\\texto_omar.txt",'w',encoding="UTF-8", ) as archivo:
    # sobreescribiendo el archivo
    #archivo.write("noigfubudfpbufdsbupbfgbofkndjminedsils  ifds")
    # agregando 2 lineas gracias a \n que lo que hace es darnos un espaciado de lineas
    archivo.writelines(["hello men como esta svery good\n", " omar es y va aser uno de los mejores programadores . "])
    