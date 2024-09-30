from elasticsearch import Elasticsearch
import time 
client = Elasticsearch(
    "http://localhost:9200",  # Elasticsearch endpoint
)

# print(client.info())
print(client.search())

#def convertir_a_mayusculas(resultados):
#    for hit in resultados['hits']['hits']:
#        for campo, valor in hit['_source'].items():
#            if isinstance(valor, str):
#                hit['_source'][campo] = valor.upper()
#    return resultados

# Obtener los resultados de la búsqueda en el índice "perros"
#resultados_perros = client.search(index="perros", size=1000)  # Ajusta el tamaño según tus necesidades

# Convertir los campos de texto a mayúsculas
#resultados_modificados = convertir_a_mayusculas(resultados_perros)

# Actualizar los documentos en Elasticsearch
#for hit in resultados_modificados['hits']['hits']:
#    client.index(index="perros", id=hit['_id'], body=hit['_source'])

#print("Documentos actualizados con éxito.")

#time.sleep(5)
# CONSULTAS DE INSERSION DE DOCUMENTOS

# Insersión index sin ID
client.index(index="perros", body={"nombre": "Roberto", "edad": 10, "raza": "Pastor Alemán"})
# Insersión index con ID
client.index(index="perros", id=1, body={"nombre": "Ricardo", "edad": 5, "raza": "Pastor Alemán"})
# Insersión create con ID (ID OBLIGATORIO)
client.create(index="perros", id=4, body={"nombre": "Juan", "edad": 3, "raza": "Pastor Alemán"})

# BUSQUEDA DE DOCUMENTOS EN ELASTICSEARCH
search = client.search()
search_perros = client.search(index="perros")
search_perros_query = client.search(index="perros", query={"match": {"nombre": "Roberto"}})
perro_id_1 = client.get(index="perros", id=1)

# CONSULTAS DE ACTUALIZACION DE DOCUMENTOS
time.sleep(1)
perro_update = client.update(index="perros", id=1, body={"doc": {"edad": 11}})


# CONSULTAS DE ELIMINACION DE DOCUMENTOS

delete_perros = client.delete(index="perros", id=1)

time.sleep(1)
# Eliminación de indice
client.indices.delete(index="perros")

bulk = client.bulk(index="perros", body=[
    {"delete":{"_index":"mi_indice","_id":"OIf9LpIByUEr8HZBYpog"}},
    {"update": {"_index": "mi_indice","_id":"OIf9LpIByUEr8HZBYpog"}},
    {"doc":{"nombre": "Luis", "apellido": "Rodríguez"}}
])