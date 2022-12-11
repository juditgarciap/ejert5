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
    
    # leer el argumento ingresado por medio del script
try:
    comando = sys.argv[1]    
    # incrementar el contador que hay en el txt en caso de ser 'inc'
    if comando == 'inc':
	    # incrementar en uno
	    contador = contador + 1
	print('Incrementando el número de visitas debido al argumento inc')
	print('Nuevo valor: {}'.format(contador))
	    
    elif comando == 'dec':
	    # decrementar en uno
	print('Decrementando el número de visitas debido al argumento dec')
	contador = contador - 1
	print('Nuevo valor: {}'.format(contador))
	    
    else:
	    # caso para cuando se envia otra cosa diferente a inc y dec
	print('Número de visitas leído del archivo contador: {}'.format(contador))
	    
    print('Almacenando nuevo valor')
    archivo.write(str(contador)) 
    # tambien almacena el valor que previamente fue leído en el caso que
    # se ingrese otro argumento diferente a inc o dec

except:
    # caso para cuando no se envia argumento
    print('Número de visitas leído del archivo contador: {}'.format(contador))
    
    # cuando se crea un archivo nuevo y no se aplica ninguna acción entonces 
    # alamcenar el 0
    if contador == 0:
        archivo.write(str(contador))

# cerrar el archivo 
archivo.close()
