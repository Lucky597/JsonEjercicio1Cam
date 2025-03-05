import json

'''def leer_json(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

datos = leer_json("indicadores.json")
print(datos)'''

def leer_json(ruta):
    archivo = open(ruta, "r", encoding="utf-8")
    datos = json.load(archivo)
    archivo.close()  # Cierra el archivo manualmente
    return datos

datos = leer_json("indicadores.json")
print(datos)