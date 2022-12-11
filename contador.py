# importar las librerias necesarias
import sys

# modo de uso, escribir en la terminal:
# python3 contador.py inc
# python3 contador.py dec
# python3 contador.py

try:
    # intentar leer el archivo con permisos de escritura en caso de existir
    archivo = open('contador.txt', 'r+')
    contador =  int(archivo.read())
    # permute ubicar el puntero de la primera linea del archivo 
    archivo.seek(0)
    # eliminar el valor almacenado para ingresar un nuevo valor 
    # previamente este valor ya se almaceno en contador
    archivo.truncate()
except OSError:
    print('Archivo no existe! se creará con el valor de 0 visitas')
    # crear el archivo con permisos de escritura
    archivo = open('contador.txt', 'w+')
    contador = 0
    print('Archivo creado!!')
    
    