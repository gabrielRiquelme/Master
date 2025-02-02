import csv

def procesa_archivos(url):

    try: 
        with open (url,'r',encoding='UTF-8') as notas:
            variableNotas = csv.reader (notas,delimiter=',')
            for fila in variableNotas:
                print(fila)
    except Exception:
        print('No se pudo abrir archivo')


# Main
url = r'C:\Users\sofia\OneDrive\Documentos\Master\MasEjercicios\calificaciones.csv'
procesa_archivos(url)