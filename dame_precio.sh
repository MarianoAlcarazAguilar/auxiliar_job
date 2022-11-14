#! /bin/bash

echo -e '¿Qué producto es?'
read PRODUCTO
echo -e '¿En qué región es la venta?'
read REGION
echo -e '¿En qué mes es la venta?'
read MES
echo -e '¿Qué tipo de cliente hará la compra?'
read TIPO_CLIENTE

python ./regression.py $PRODUCTO $REGION $MES $TIPO_CLIENTE