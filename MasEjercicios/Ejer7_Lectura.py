import csv

def leerCsv(archivo):
    lista_cotizaciones = []
    with open(archivo, newline='') as cotizaciones:
        cotizacionesLista = csv.reader(cotizaciones, delimiter=';') #Leo CSV con libreria csv, le asigno delimitador ';'
        
        for row in cotizacionesLista: # Itero los datos del CSV y se lo asigno al diccionario declarado.
                dict_cotizacion = {
                    'Nombre': row[0],
                    'final': row[1],
                    'Maximo': row[2],
                    'Minimo': row[3],
                    'Volumen': row[4],
                    'Efectivo': row[5]
                }
                lista_cotizaciones.append(dict_cotizacion) #Agrego a una lista cada diccionario

    return lista_cotizaciones

# MAIN
url = r'C:\Users\sofia\OneDrive\Documentos\Master\MasEjercicios\cotizacion.csv'
cotizacionEnDic = leerCsv(url)

with open('diccionario.txt','w+') as diccionario: # Genero un nuevo documento.txt
    for dict in cotizacionEnDic: # Lo itero y le escribo cada valor aqui debajo.
        diccionario.write('***************************************\n')
        for clave, valor in dict.items(): 
            diccionario.write(f'{clave}: {valor}\n')
        diccionario.write('***************************************\n')


#GENERO SEGUNDO .TXT#
cotizacionEnDic = leerCsv(url)

with open('diccionarioMinimoMax.csv','w+') as diccionario: # Genero un nuevo documento.txt
    for dict in cotizacionEnDic: # Lo itero y le escribo cada valor aqui debajo.
        diccionario.write('***************************************\n')
        for clave, valor in dict.items():
            if clave == 'Nombre' or 'Maximo' or clave == 'Minimo':
                diccionario.write(f'{clave}: {valor}\n')
        diccionario.write('***************************************\n')

