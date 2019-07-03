from libro import Libro


class hash_tabla:
    def __init__(self):
        self.tabla = [None] * 127

    # Función hash
    def funcion_hash(self, valor):
        llave = 0
        for i in range(0, len(valor)):
            llave += ord(valor[i])
        return llave % 127

    def insertar(self, valor):  # Metodo para ingresar elementos
        hash = self.funcion_hash(str(valor))
        if self.tabla[hash] is None:
            self.tabla[hash] = valor

    def buscar(self, valor):  # Metodo para buscar elementos
        hash = self.funcion_hash(valor)
        if self.tabla[hash] is None:
            return None
        else:
            return self.tabla[hash]

    def eliminar(self, valor):  # Metodo para eleminar elementos
        hash = self.funcion_hash(valor)
        if self.tabla[hash] is None:
            print("No hay elementos con ese valor", valor)
        else:
            print("Elemento con valor", valor, "eliminado")
            self.tabla[hash] = None

    def __iter__(self):
        i = 0
        while i != 127:
            yield (self.tabla[i])
            i += 1
