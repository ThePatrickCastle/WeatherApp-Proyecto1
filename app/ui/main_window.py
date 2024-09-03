'''
Interacción entre el usuario y la aplicación, así como las acciones que la app puede ejecutar
@Author Salgado González Edgar
@Author
@Author
'''
import sys, os
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton,
    QLabel, QStackedLayout, QGridLayout, QLineEdit, QComboBox, QGridLayout,
    QListWidget, QMessageBox, QCompleter
)
basedir = os.path.dirname(__file__)
''' @class MainWindow. La ventana principal con la que interactua el uusario con el programa '''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tipodebusqueda = 0
        self.cadenabuscar = ""
        self.numerotabs = 0
        self.tabPrincipal = QStackedLayout()
        tabinicial = QGridLayout()
        barrasuperior = QHBoxLayout()
        barrabuscadora = QHBoxLayout()
        self.setWindowTitle(" OpenWeatherApp ")
        logo = QLabel(" Logo ")
        logo.setFont(QFont('Times', 50))
        logo.setAlignment(Qt.AlignLeft | Qt. AlignVCenter)
        imagenlogo = QLabel(" Imagen logo")
        imagenlogoeditable = QPixmap(os.path.join(basedir + "/resources/Logo.png"))
        imagenlogoeditable.scaled(50, 50, Qt.KeepAspectRatio)
        imagenlogo.setPixmap(imagenlogoeditable)
        imagenlogo.setAlignment(Qt.AlignRight)
        barrasuperior.addWidget(imagenlogo)
        barrasuperior.addWidget(logo)
        tabinicial.addLayout(barrasuperior, 0, 0)
        tabinicial.addLayout(barrabuscadora, 1, 0)
        listacoincidentes = QListWidget()
        tabinicial.addWidget(listacoincidentes, 2, 0)
        self.barraescritura = QLineEdit()
        self.barraescritura.setPlaceholderText(" Por favor, elige una opción ")
        barrabuscadora.addWidget(self.barraescritura)
        self.barraescritura.textEdited.connect(self.guardar_busqueda)
        self.barraescritura.returnPressed.connect(self.realizar_busqueda)
        self.listadebusqueda = QComboBox()
        self.listadebusqueda.addItems(["Opciones", "Vuelo", "Ciudad"])
        self.listadebusqueda.currentIndexChanged.connect(self.cambiar_tipo_busqueda)
        barrabuscadora.addWidget(self.listadebusqueda)
        botonbuscar = QPushButton("Buscar")
        botonbuscar.pressed.connect(self.realizar_busqueda)
        barrabuscadora.addWidget(botonbuscar)
        capainicial = QWidget()
        capainicial.setLayout(tabinicial)
        self.tabPrincipal.addWidget(capainicial)
        capafinal = QWidget()
        capafinal.setLayout(self.tabPrincipal)
        self.setCentralWidget(capafinal)
        # Bloqueamos el tamaño de la ventana para no tener errores indeseados en los formatos, por ahora.
        self.setMinimumSize(1000, 700)
        self.setMaximumSize(1000, 700)
    '''
    @func cambiar_tipo_busqueda hace que al seleccionar uno de los dos tipos de busqueda desde la QComboBox listadebusqueda
    determinemos que tipo de busqueda se realizará
    @param self, indice. self siendo la ventana principal en sí. indice siendo el índice de la QComboBox elegida
    '''
    def cambiar_tipo_busqueda(self, indice):
        if indice == 2:
            self.tipodebusqueda = 2
            self.barraescritura.setPlaceholderText(" Escribe tu ciudad ")
            ciudades = ["Valencia", "Madrid", "Tokyo", "Monterrey"]
            completarbusqueda = QCompleter(ciudades)
            self.barraescritura.setCompleter(completarbusqueda)
        if indice == 1:
            self.tipodebusqueda = 1
            vuelos = ["00000", "11111", "22222", "33333"]
            completarbusqueda = QCompleter(vuelos)
            self.barraescritura.setPlaceholderText(" Escribe tu ticket ")
            self.barraescritura.setCompleter(completarbusqueda)
        if indice == 0:
            self.barraescritura.setPlaceholderText(" Por favor, elige una opción")
    '''
    @func guardar_busqueda guarda en cadenabuscar lo escrito en la QLineEdit barraescritora en tiempo real, o sea, que
    guarda en la variable al mismo tiempo que se escribe
    @param self, cadenarecibida. self siendo el programa en sí. cadenarecibida siendo la cadena escrita en barraescritora
    '''
    def guardar_busqueda(self, cadenarecibida): self.cadenabuscar = cadenarecibida
    '''
    Tanto venta vuelo como ventana ciudad ya tienen su estructura hecha de una forma abstracta, a su discreción, todo aquí
    se puede eliminar sin problema, es más, es lo esperado, pues cosas como las listas, imágenes y una distribución de la
    información son más que una idea conceptual, por esa misma razón no tienen comentarios, pues en sí no es nada '''
    ''' @func ventana_vuelo crea a partir de la cadena recibida un nuevo tab con todo lo que se necesita desplegar
        para la ventana del vuelo '''
    def ventana_vuelo(self):
        ventanadevuelo = QGridLayout()
        ticketvuelo = QLabel(self.cadenabuscar)
        ticketvuelo.setFont(QFont('Times', 10))
        ticketvuelo.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        cdcomienza = QLabel(" Ciudad de despegue ")
        cdcomienza.setFont(QFont('Times', 30))
        cdcomienza.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        hrllegada = QLabel(" Hora de llegada: ")
        hrllegada.setFont(QFont('Times', 30))
        hrllegada.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        ventanadevuelo.addWidget(ticketvuelo, 0, 1)
        ventanadevuelo.addWidget(cdcomienza, 1, 0)
        ventanadevuelo.addWidget(hrllegada, 1, 2)
        ''' Aquí se puede agregar la lista de recomendaciones (en 1,1), está el hueco para poner cualquier
        cosa '''
        avion = QLabel(" Avion ")
        avion.setPixmap(QPixmap(os.path.join(basedir + "/resources/Avion.png")))
        avion.setScaledContents(True)
        ventanadevuelo.addWidget(avion, 1, 1)
        listaclimaida = QListWidget()
        ventanadevuelo.addWidget(listaclimaida, 2, 0)
        listarecomendar = QListWidget()
        listaclimallegada = QListWidget()
        juntalistas = QVBoxLayout()
        juntalistas.addWidget(listaclimallegada)
        juntalistas.addWidget(listarecomendar)
        ventanadevuelo.addLayout(juntalistas, 2, 2)
        botonAtras = QPushButton("Atras")
        botonAtras.resize(150, 50)
        botonAtras.clicked.connect(self.regresar_pantalla_principal)
        ventanadevuelo.addWidget(botonAtras, 0, 0)
        return ventanadevuelo
    ''' @func ventana_ciudad crea a partir de la cadena recibida un nuevo tab con todo lo que se necesita desplegar
        para la ventana de la ciudad '''
    def ventana_ciudad(self):
        ventanadeciudad = QGridLayout()
        nombreciudad = QLabel(self.cadenabuscar)
        nombreciudad.setFont(QFont('Times', 20))
        nombreciudad.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        ventanadeciudad.addWidget(nombreciudad, 0, 1)
        textoclimas = QLabel(" Clima: ")
        textoclimas.setFont(QFont('Times', 20))
        textoclimas.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        ventanadeciudad.addWidget(textoclimas, 1, 0)
        textorecomendaciones = QLabel(" Recomendaciones: ")
        textorecomendaciones.setFont(QFont('Times', 20))
        textorecomendaciones.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        ventanadeciudad.addWidget(textorecomendaciones, 1, 1)
        listaclimas = QListWidget()
        ventanadeciudad.addWidget(listaclimas, 2, 0)
        listarecomendar = QListWidget()
        ventanadeciudad.addWidget(listarecomendar, 2, 1)
        botonAtras = QPushButton("Atras")
        botonAtras.resize(150, 50)
        botonAtras.clicked.connect(self.regresar_pantalla_principal)
        ventanadeciudad.addWidget(botonAtras, 0, 0)
        return ventanadeciudad
    ''' @function regresar_pantalla_principal regresa desde el tab actual hasta el inicial'''
    def regresar_pantalla_principal(self):
        self.tipodebusqueda = 0
        self.tabPrincipal.setCurrentIndex(0)
    ''' @function null_tipo_busqueda lanza un pop up al usuario que le advierte que su elección es vacia'''
    def null_tipo_busqueda(self):
        mensajeerror = QMessageBox.critical(
        self,
        "Selección nula",
        " Por favor, elige una opción ",
        buttons = QMessageBox.Ok
        )
    ''' @function null_cadenabuscar lanza un pop up al usuario que le advierte que su cadena es vacia '''
    def null_cadenabuscar(self):
        mensajeerror = QMessageBox.critical(
        self,
        "Entrada nula",
        " La entrada es nula  ",
        buttons = QMessageBox.Ok
        )
    ''' @function cadena_no_encontrada lanza un pop_up que advierte al usuario que su cadena no fue encontrada '''
    def cadena_no_encontrada(self):
        mensajeerror = QMessageBox.critical(
        self,
        "Not Found",
        " Intenta otra vez ",
        buttons = QMessageBox.Ok
        )
    ''' @func realizar_busqueda al ser clickeado el botón de busqueda o presionado enter en la barra buscadora
        se ejecuta la busqueda, que por el momento solo checa que se haya seleccionado una opción, que la cadena
        no sea vacia y que no sea igual a Cadenanoencontrada, después de eso despliega una ventana provisional de vuelo
        o ciudad '''
    def realizar_busqueda(self):
        self.capanueva = QWidget()
        if self.tipodebusqueda == 0:
            self.null_tipo_busqueda()
            return
        if self.cadenabuscar == "":
            self.null_cadenabuscar()
            return
        if self.cadenabuscar == "Cadenanoencontrada":
            self.cadena_no_encontrada()
            return
        if self.tipodebusqueda == 1: self.capanueva.setLayout(self.ventana_vuelo())
        elif self.tipodebusqueda == 2: self.capanueva.setLayout(self.ventana_ciudad())
        self.tabPrincipal.addWidget(self.capanueva)
        self.numerotabs += 1
        self.tabPrincipal.setCurrentIndex(self.numerotabs)
app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.exec()
