import codecs  # Clase para la lectura de archivos, se importa codecs


class manejoArchivo:

    def __init__(self, archivo):
        self.archivoNombre = archivo  # Atributo que recibe la dirección del archivo
        self.archivo = codecs.open(self.archivoNombre, "r")  # Se abre el archivo

    def obtenerInformacion(self):
        return self.archivo.readlines()  # Lee las líneas del archivo

    def cerrarArchivo(self):  # Se cierra el archivo
        self.archivo.close()
