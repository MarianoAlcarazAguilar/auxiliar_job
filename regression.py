import pandas as pd
import sys
import numpy as np
import openpyxl

running_from_terminal = False
if running_from_terminal:
    producto = sys.argv[1].upper()
    region = sys.argv[2].lower()
    mes = sys.argv[3].lower()
    tipo_cliente = sys.argv[4].upper()

else: 
    wb = openpyxl.load_workbook('estimador_precios.xlsx')
    sheet = wb.active
    producto = sheet['B2'].value.upper()
    region = sheet['B3'].value.lower()
    mes = sheet['B4'].value.lower()
    tipo_cliente = sheet['B5'].value.upper()

regression = pd.read_csv('data_prods/regression.csv')
productos = pd.read_csv('data_prods/products_encoding.csv', index_col='sku')
regiones = pd.read_csv('data_prods/regions_encoding.csv', index_col='region')
meses = pd.read_csv('data_prods/months_encoding.csv', index_col='mes')
clientes = pd.read_csv('data_prods/clients_encoding.csv', index_col='tipo_cliente')


def get_price_of(producto=None, region=None, mes=None, tipo_cliente=None, piezas=0):
    reg = regression.loc[0].values
    encoding_producto = productos.loc[producto].values
    encoding_cliente = clientes.loc[tipo_cliente].values
    encoding_region = regiones.loc[region].values
    encoding_mes = meses.loc[mes].values
    encoding_piezas = np.array([piezas])
    full_encoding = np.hstack(
        ([1], encoding_piezas, encoding_cliente, encoding_region, encoding_mes, encoding_producto))
    return np.sqrt((reg * full_encoding).sum())


precio = get_price_of(producto, region, mes, tipo_cliente)*11/10
if running_from_terminal:
    print(f'Precio estimado: ${np.round(precio,2)}')
else:
    sheet['B6'].value = np.round(precio, 2)
    wb.save('estimador_precios.xlsx')