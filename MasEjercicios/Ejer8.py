import csv

def leer_archivo_separado(url):
    datos = []
    with open(url, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter=';')  # Especificamos el punto y coma como separador
        for fila in lector_csv:
            datos.append(fila)
    return datos

def gendic(lista):
    cabecera = lista[0]
    info = lista[1:]
    lista_diccionario=[]

    for i in range(len(info)):
        diccionario[cabecera[i]]=info[i]
        lista_diccionario.append(diccionario)
        return lista_diccionario

url = r'C:\Users\Juan G. Riquelme\OneDrive - Grupo Hasar\Documentos\Personal\Master\MasEjercicios\calificaciones.csv'
diccionario={}
lista_diccionario=[]
lista = leer_archivo_separado(url)
procesado = gendic(lista)
print(procesado)

