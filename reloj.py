# importar las librerias necesarias
import os
import time
import datetime

# modo de uso, escribir en la terminal
# python3 reloj.py


# ejecutar un bucle while en True de manera indefinida 
while True:
    # obtener la fecha completa
    fecha_completa_actual = datetime.datetime.now()
    # convertir la fecha al formato deseado 
    print('Fecha y hora actual:')
    print(fecha_completa_actual.strftime("%Y/%m/%d, %H:%M:%S"))
    # pausa la ejecución un segundo
    time.sleep(1)
    # eliminar el valor anterior para poner la siguiente nueva hora
    os.system('clear')
