class operaciones:  # Clase para las distintas operaciones

    def ordenarData(data):  # Procedimiento para agregar los valores de cada línea de la lista original a una lista nueva de manera individual
        data2 = []
        for l in data:  # Se recorre los elementos de la lista original
            for k in l:  # Se recorre cada elemento de cada linea
                k = k.replace("\n", "")  # Se elimina los saltos de línea
                data2.append(int(k))  # Se añade el elemento convertido en entero a la lista nueva
        data2.sort()  # Se ordena la lista
        return data2  # Se devuelve la lista nueva ordenada

    def busquedaBinaria(numero, lista):  # Se recibe de parámetros el valor a buscar y la lista ya ordenada
        inferior = 0  # Variables auxiliares
        superior = len(lista)-1
        medio = (inferior+superior+1)//2
        ubicacion = -1  # Valor base, si no se encontró el elemento se devuelve -1
        aux = False  # Variable de control del While
        while(aux != True):  # Proceso para comparar y buscar de forma binaria
            if(numero == lista[medio]):
                ubicacion = medio
                aux = True
            elif(numero < lista[medio]):
                        superior = medio - 1
            else:
                        inferior = medio + 1
            medio = (inferior+superior+1)//2
            if(inferior <= superior) and (ubicacion == -1):
                aux = False
            else:
                aux = True
        return ubicacion  # Se devuelva la posición del elemento encontrado
