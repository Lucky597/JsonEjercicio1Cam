import json #la librería json
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
print("*****************************************************")
datos = leer_json("paises.json")
print(datos)
print("=====================================================")
datos = leer_json("poblacion.json")
print(datos)

# HASTA AQUI """Lee un archivo JSON y devuelve su contenido como lista de diccionarios."""

def escribir_json(nombre_archivo, datos): # nombre_archivo:Es el nombre del archivo donde se guardarán los datos. datos: Es la información que queremos guardar en formato JSON.
    """Escribe datos en un archivo JSON."""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)

def escribirjson(ruta, datos): #el primero es el archivo json a escribir y el segundo es la estructura de datos de pyton {} []
    archivo = open(ruta, "w", encoding="utf-8") #w para perisos de escribir en codificacion utf-8
    json.dump(datos, archivo, indent=4) # almacenamos en variable datos, una estructura de datos de Python {} [] lo convertimos a JSON
    #Esta funcion no retorna si no que modifica el Json que le pasemos con lo datos en pyton que le pasemos

#vamos a crear una lista de diccionarios para pasarcela a un Json 
tareas = [
    {"tarea": "Estudiar Python", "completado": False},
    {"tarea": "Hacer ejercicio", "completado": True},
    {"tarea": "hacer tonterias", "completed": True}
]

escribirjson("prueba.json", tareas) #si esxiste el archivo .josn lo crea, si existe lo sobre escribe
