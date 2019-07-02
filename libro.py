class Libro:
    def __init__(self, nombre, autor, editorial):
        self.nombre = nombre
        self.autor = autor
        self.editorial = editorial
    def __eq__(self,libro):
        if type(libro) == Libro:
            if self.nombre == libro.nombre:
                return True
        return False

    def __len__(self):
        return len(self.nombre)

    def __str__(self):
        return self.nombre
