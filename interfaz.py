""" Importamos todas nuetra ventana y funciones útiles"""
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

# Clase principal de nuestra aplicación
class MainPage(QDialog):
    """ Clase principal de nuestra aplicación"""
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('mainPage.ui', self)
        # Se llama al evento del botón léxico
        self.btnLexic.clicked.connect(self.lexicTest)
        # Se llama al evento del botón sintáctico
        self.btnSintact.clicked.connect(self.sintacticTest)
        # Se llama al evento del botón analizar de nuevo
        self.btnAnalizerNewCode.clicked.connect(self.analizarDeNuevo)

    """Por ahora estas funciones solo muestran mensajes se deben definir"""
    # Función que realiza el analisis léxico del código ingresado
    def lexicTest(self):
        words = self.cajaCodigo.toPlainText().strip()
        self.textEdit.setText(words)

    # Función que realiza el análisis sintáctico del código ingresado
    def sintacticTest(self):
        words = self.cajaCodigo.toPlainText().strip()
        message = "ahora es sintactico" + words
        self.textEdit.setText(message)

    def analizarDeNuevo(self):
       self.cajaCodigo.setText('')
       self.textEdit.setText('')


def iniciar():
    # Se instancia nuestra aplicación por defecto esto no cambia
    app = QApplication(sys.argv)

    # Se instancia nuestra ventana
    ventana = MainPage()
    # Se muestra la ventana principal
    ventana.show()

    # Se controla el cierre de la aplicación
    sys.exit(app.exec_())

if __name__ == '__main__':
    iniciar()
