from ManejoArchivos.manejoArchivos import manejoArchivo as mA
from Operaciones.operaciones import operaciones as op

numBuscar = 0  # Variable del elemento a buscar
posicion = 0  # Variable de la posición del elemento encontrado
data = []  # Lista con los elementos del archivo
data2 = []  # Lista con los elementos organizados y ordenados
archivo = mA("datos.txt")  # Lectura del archivo
data = archivo.obtenerInformacion()  # Obtención de los elementos del archivo
data = [l.split(",") for l in data]  # Se separa los elementos de cada líneas en "subcadenas"
operaciones = op()  # Se crea un objeto de la clase operaciones
data2 = op.ordenarData(data)  # Se procede a agregar los valores ordenados y organizados de la lista data a data2
print(data2)  # Se presenta en pantalla la lista ordenada
numBuscar = int(input("Ingrese el numero a buscar: "))  # Se ingresa por teclado el elemento a buscar
posicion = op.busquedaBinaria(numBuscar, data2)  # Se devuelve la posición del elemento
if(posicion == -1):  # Condicional, si es -1, significa que no hay dicho elemento, cso contrario se imprime la posición del elemento
    print("No existe elemento buscado")
else:
    print("El elemento de encontró en la posición: "+str(posicion))
archivo.cerrarArchivo()  # Se cierra el archivo
