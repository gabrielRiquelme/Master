import openpyxl

# Crear un nuevo libro de trabajo

libro = openpyxl.load_workbook('datos_meses.xlsx')

sheet=libro.active

for row in sheet.iter_rows(values_only=True):
    print(row)

sheet['A4'] = '=SUM(A2:A3)'
sheet['B4'] = '=SUM(B2:B3)'
sheet['C4'] = '=SUM(A4:B4)'

sheet['C2'] = ''
sheet['C3'] = ''

libro.save("datos_meses.xlsx")