import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.QtWidgets import QListWidgetItem

from libro import Libro
from hash import hash_tabla
from Archivos import *

qtCreatorFile = "Inicio.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Inicio(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.hash = hash_tabla()
        for libro in leer('libros.lib'):
            self.hash.insertar(libro)

        self.anadirboton.clicked.connect(self.agregarlibro)
        self.buscarboton.clicked.connect(self.buscarlibro)

    def buscarlibro(self):
        buscar = BuscarLibro(self.hash)
        buscar.exec()

    def agregarlibro(self):
        agregar = AgregarLibro(self.hash)
        agregar.exec()

qtCreatorFile = "Agregar.ui"
Ui_Dialog, QtBaseClass = uic.loadUiType(qtCreatorFile)


class AgregarLibro(QDialog, Ui_Dialog):
    def __init__(self, hash):
        QDialog.__init__(self)
        Ui_Dialog.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.hash = hash

        for libro in self.hash:
            if libro is not None:
                nuevo_libro = QListWidgetItem(
                    libro.nombre + "/" + libro.autor + "/" + libro.editorial
                )
                self.listWidget.addItem(nuevo_libro)

        self.Agregarlibro.clicked.connect(self.ingresarlibro)
        self.Mostrar.clicked.connect(self.mostrar)
        self.eliminarlibro.clicked.connect(self.eliminarLibro)

    def ingresarlibro(self):
        ingresar = IngresarLibro()
        ingresar.exec()

        if ingresar.libro is not None:
            libro = ingresar.libro
            self.hash.insertar(libro)

            nuevo_libro = QListWidgetItem(
                libro.nombre + "/" + libro.autor + "/" + libro.editorial
            )
            self.listWidget.addItem(nuevo_libro)

    def mostrar(self):
        for i in self.hash:
            print(i)

    def eliminarLibro(self):
        libro = self.listWidget.currentItem()
        if libro is not None:
            self.hash.eliminar(libro.text())
            libro = Libro(*libro.text().split('/'))
            eliminar("libros.lib", libro)
            self.listWidget.takeItem(self.listWidget.currentRow())

qtCreatorFile = "IngresarLibro.ui"
Ui_Dialog, QtBaseClass = uic.loadUiType(qtCreatorFile)

class IngresarLibro(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        Ui_Dialog.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.libro = None
        self.buttonBox.accepted.connect(self.ingresar)

    def ingresar(self):
        nombre = self.lineEdit_1.text()
        autor = self.lineEdit_2.text()
        editorial = self.lineEdit_3.text()
        self.libro = Libro(nombre, autor, editorial)
        añadir("libros.lib",self.libro)


qtCreatorFile = "Buscar.ui"
Ui_Dialog, QtBaseClass = uic.loadUiType(qtCreatorFile)


class BuscarLibro(QDialog, Ui_Dialog):
    def __init__(self, hash):
        QDialog.__init__(self)
        Ui_Dialog.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.hash = hash
        self.buttonBox.accepted.connect(self.buscar)

    def buscar(self):
        texto = self.lineEdit.text()
        libro = self.hash.buscar(texto)

        if libro is not None:
            mensaje = Mensaje('Nombre = ' + libro.nombre + "\n"
                + 'Autor = ' + libro.autor+"\n"
                + 'Editorial = ' + libro.editorial
            )
            mensaje.exec()
        else:
            mensaje = Mensaje('No se encontro el libro')
            mensaje.exec()


qtCreatorFile = "mensaje.ui"
Ui_Dialog, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Mensaje(QDialog, Ui_Dialog):
    def __init__(self, texto):
        QDialog.__init__(self)
        Ui_Dialog.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.librobuscado.setText(texto)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Inicio()
    window.show()
    sys.exit(app.exec_())
