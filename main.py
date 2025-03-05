import json
# El json que vamos leer parece ser una lista de Diccionarios
'''def leer_json(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

datos = leer_json("indicadores.json")
print(datos)'''

def leer_json(ruta): #Definimos la funcion y colocamos la ruta hasta la extencion del archivo
    archivo = open(ruta, "r", encoding="utf-8") #Usamos la funcion open para abrir el archivo y r para perisos de lectura en codificacion utf-8, almacenamos en variable archivo
    datos = json.load(archivo) # almacenamos en variable datos, leemos y convertir un archivo JSON en una estructura de datos de Python {} [].
    archivo.close()  # Cierra el archivo manualmente
    return datos #Si el JSON contiene {} → se convierte en un diccionario (dict). Si el JSON contiene [] → se convierte en una lista (list).

datos = leer_json("indicadores.json")
print(datos)

datos = leer_json("paises.json")
print(datos)

datos = leer_json("poblacion.json")
print(datos)