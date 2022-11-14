import openpyxl

wb = openpyxl.load_workbook('estimador_precios.xlsx')

sheet = wb.active

# worksheet['B4']='We are writing to B4'
# Writing to a cell with sheet reference
sheet['C2'] = 'Writing with sheet reference'

# Writing with cell reference
# >>>mycell=worksheet['B4']
# >>>mycell.value='Writing with reference to cell'


cell = sheet['C3']
cell.value = 'Writing with reference to cell'

wb.save('estimador_precios.xlsx')