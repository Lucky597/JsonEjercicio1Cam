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
print("=====================================================")

# HASTA AQUI """Lee un archivo JSON y devuelve su contenido como lista de diccionarios."""

def escribir_json(nombre_archivo, datos): # nombre_archivo:Es el nombre del archivo donde se guardarán los datos. datos: Es la información que queremos guardar en formato JSON.
    """Escribe datos en un archivo JSON."""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)

def escribirjson(ruta, datos): #el primero es el archivo json a escribir y el segundo es la estructura de datos de pyton {} []
    archivo = open(ruta, "w", encoding="utf-8") #w para perisos de escribir en codificacion utf-8
    json.dump(datos, archivo, indent=4) # almacenamos en variable datos, una estructura de datos de Python {} [] lo convertimos a JSON
    #Esta funcion no retorna si no que modifica el Json que le pasemos con lo datos en pyton que le pasemos

#vamos a crear una lista de diccionarios para pasarla a un Json 
tareas = [
    {"tarea": "Estudiar Python", "completado": False},
    {"tarea": "Hacer ejercicio", "completado": True},
    {"tarea": "hacer tonterias", "completed": True}
]

escribirjson("prueba.json", tareas) #si esxiste el archivo .josn lo crea, si existe lo sobre escribe

#Hasta aqui es el a) Módulo de gestión de archivos JSON (Funciones para leer y escribir en los archivos JSON).

#b) Módulo de gestión de países
def listar_paises():
    """Lista todos los países registrados en el sistema."""
    paises = leer_json("paises.json") #Reutilizo la funcion que use antes para leer json
    for pais in paises:
        print(f"Nombre: {pais['nombre']}, Código ISO: {pais['codigo_iso']}, Código ISO3: {pais['codigo_iso3']}") #f permite leeer los diccionarios
print("------------Módulo de gestión de países------------")
listar_paises()

#c) Módulo de gestión de población
def obtener_poblacion_por_pais(pais, ano_inicio, ano_fin): #Idico pais, año desde, años hasta. Rango en que quiero ver la poblacion de ese pais 
    """Devuelve los datos de población de un país en un rango de años con el formato deseado."""
    datos = leer_json("poblacion.json")  #Reutilizo la funcion que use antes para leer json
    
    poblacion_filtrada = [
        {"pais": p["pais"], "ano": p["ano"], "poblacion": p["valor"]} #esta creando un diccionario en la posicion p comotantos diccionarios existan enel json
        for p in datos
        if p["pais"] == pais and ano_inicio <= p["ano"] <= ano_fin #compara si es el pais en esa posicion p "amd" luego mira si ano variable o llave esta entre el rango
    ]
    
    return poblacion_filtrada #la lista de diccionarios creadda aaprtir laa informacion del json

print("------------Módulo de gestión de población------------")
resultado = obtener_poblacion_por_pais("India", 2000, 2023)
print(resultado)

#d) Módulo de reportes
print("------------Módulo de reportes------------")
def obtener_poblacion_total_india_2022():
    """Obtiene la población total de India en 2022."""
    datos = leer_json("poblacion.json")
    for d in datos:
        if d["pais"] == "India" and d["ano"] == 2022 and d["indicador_id"] == "SP.POP.TOTL":
            return d["valor"]
    return "No hay datos disponibles"


