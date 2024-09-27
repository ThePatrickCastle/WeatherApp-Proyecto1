'''
Modulo Interacción entre el usuario y la aplicación, así como las acciones que la app puede ejecutar
Author: @Edgar Salgado González
Contributor: @ThePatrickCastle
Contributor: @C4mdax
Version 1.0

'''

import sys, os

import schedule
import time

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton,
    QLabel, QStackedLayout, QGridLayout, QLineEdit, QComboBox, QGridLayout,
    QListWidget, QMessageBox, QCompleter
    )

from api.recommendations import Recommendations
from data.input_cleaner import InputCleaner
from data.ticket_finder import TicketFinder


basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    '''
    Clase MainWindow. La ventana principal con la que interactua el usuario del programa

    '''
    def __init__(self):
        super().__init__()
        self.tipodebusqueda = 0
        self.cadenabuscar = ""
        self.numerotabs = 0

        self.setFixedSize(1300, 700)
        
        self.tabPrincipal = QStackedLayout()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("AreoNimbus!")
        self.setStyleSheet("""
            QMainWindow {
                background-color: #FFFFFF;
            }
            QLabel {
                color: #2E4053;
            }
            QPushButton {
                background-color: #3498DB;
                color: white;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
            QLineEdit {
                border: 1px solid #2E4053;
                border-radius: 5px;
                padding: 8px;
            }
            QComboBox {
                border: 1px solid #2E4053;
                border-radius: 5px;
                padding: 5px;
            }
        """)
        tabdesplegado = self.creador_tab()
        capainicial = QWidget()
        capainicial.setLayout(tabdesplegado)
        self.tabPrincipal.addWidget(capainicial)
        
        #tamaño
        screen = QApplication.primaryScreen().geometry()
        self.resize(int(screen.width() * 0.6), int(screen.height() * 0.6))

        capafinal = QWidget()
        capafinal.setLayout(self.tabPrincipal)
        self.setCentralWidget(capafinal)

    def creador_tab(self):
        '''
        @func creador_tab crea una nueva tab con el sub-menú ya desplegado o sin desplegar, por
        si es nuevo uso o no
        @param self, siendo una referencia a la ventana principal
        '''
        tabinicial = QGridLayout()
        barrasuperior = QHBoxLayout()
        barrabuscadora = QHBoxLayout()
        self.setWindowTitle("WeatherFly!")
        logo = QLabel("WeatherFly!")
        logo.setFont(QFont('Roboto', 50))
        logo.setAlignment(Qt.AlignLeft | Qt. AlignVCenter)
        imagenlogo = QLabel(" Imagen logo")

        screen = QApplication.primaryScreen().geometry()
        screen_width = screen.width()
        screen_height = screen.height()

        width_20_percent = int(screen_width * 0.15)
        height_20_percent = int(screen_height * 0.15)

        imagenlogoeditable = QPixmap(os.path.join(basedir + "/ui/resources/aero_nimbus_simple_logo.png"))
        imagenlogoeditable = imagenlogoeditable.scaled(width_20_percent, height_20_percent, Qt.KeepAspectRatio)

        imagenlogo.setPixmap(imagenlogoeditable)
        imagenlogo.setAlignment(Qt.AlignCenter)

        barrasuperior.addWidget(imagenlogo)
        barrasuperior.addWidget(logo)
        tabinicial.addLayout(barrasuperior, 0, 0)
        tabinicial.addLayout(barrabuscadora, 1, 0)
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
        return tabinicial
    def cambiar_tipo_busqueda(self, indice):
        '''
        @func cambiar_tipo_busqueda hace que al seleccionar uno de los dos tipos de busqueda desde la QComboBox listadebusqueda
        determinemos que tipo de busqueda se realizará
        @param self, indice. self siendo la ventana principal en sí. indice siendo el índice de la QComboBox elegida
        '''
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


    def guardar_busqueda(self, cadenarecibida):
        '''
        @func guardar_busqueda guarda en cadenabuscar lo escrito en la QLineEdit barraescritora en tiempo real, o sea, que
        guarda en la variable al mismo tiempo que se escribe
        @param self, cadenarecibida. self siendo el programa en sí. cadenarecibida siendo la cadena escrita en barraescritora
        '''
        self.cadenabuscar = cadenarecibida

    def ventana_vuelo(self,iata_origen, estado_origen, iata_destino, estado_destino):
        '''
        @func ventana_vuelo crea a partir de la cadena recibida un nuevo tab con todo lo que se necesita desplegar
        para la ventana del vuelo
        '''
        origen = Recommendations(estado_origen)
        destino = Recommendations(estado_destino)

        informacion_origen = origen.get_atributes()

        informacion_destino = destino.get_atributes()
        recomendaciones_destino = destino.get_recommendations()


        ventanadevuelo = QGridLayout()
        ticketvuelo = QLabel(f"Ticket {self.cadenabuscar}")
        ticketvuelo.setFont(QFont('Times', 15))
        ticketvuelo.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        cdcomienza = QLabel(f" {iata_origen}, {estado_origen} ")
        cdcomienza.setFont(QFont('Times', 30))
        cdcomienza.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        hrllegada = QLabel(f" {iata_destino}, {estado_destino} ")
        hrllegada.setFont(QFont('Times', 30))
        hrllegada.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        ventanadevuelo.addWidget(ticketvuelo, 0, 1)
        ventanadevuelo.addWidget(cdcomienza, 1, 0)
        ventanadevuelo.addWidget(hrllegada, 1, 2)
        avion = QLabel(" Avion ")

        screen = QApplication.primaryScreen().geometry()
        screen_width = screen.width()
        screen_height = screen.height()

        width_20_percent = int(screen_width * 0.10)
        height_20_percent = int(screen_height * 0.10)

        avion_logo = QPixmap(os.path.join(basedir + "/ui/resources/Avion.png"))
        avion_logo = avion_logo.scaled(width_20_percent, height_20_percent, Qt.KeepAspectRatio)

        avion.setPixmap(avion_logo)
        avion.setScaledContents(True)
        avion.setAlignment(Qt.AlignCenter)

        ventanadevuelo.addWidget(avion, 1, 1)
        listaclimaida = QListWidget()
        ventanadevuelo.addWidget(listaclimaida, 2, 0)
        listarecomendar = QListWidget()
        listaclimallegada = QListWidget()
        juntalistas = QVBoxLayout()
        juntalistas.addWidget(listaclimallegada)
        juntalistas.addWidget(listarecomendar)

        for info in informacion_origen:
            listaclimaida.addItem(info)

        for info in informacion_destino:
            listaclimallegada.addItem(info)

        for recommedation in recomendaciones_destino:
            listarecomendar.addItem(recommedation)


        ventanadevuelo.addLayout(juntalistas, 2, 2)

        return ventanadevuelo


    def ventana_ciudad(self, cadenaLimpia):
        '''
        @func ventana_ciudad crea a partir de la cadena recibida un nuevo tab con todo lo que se necesita desplegar
        para la ventana de la ciudad
        '''
        ciudad = Recommendations(cadenaLimpia)
        informacion_ciudad = ciudad.get_atributes()
        recomendaciones_ciudad = ciudad.get_recommendations()

        ventanadeciudad = QGridLayout()
        nombreciudad = QLabel(cadenaLimpia)
        nombreciudad.setFont(QFont('Times', 20, QFont.Bold))
        nombreciudad.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        nombreciudad.setStyleSheet("color: #2E4053; padding: 10px;")
        
        #ventanadeciudad.addWidget(nombreciudad, 0, 1)
        textoclimas = QLabel(f" Información de {cadenaLimpia} ")
        textoclimas.setFont(QFont('Times', 20))
        textoclimas.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        textoclimas.setStyleSheet("background-color: #ECF0F1; padding: 5px; border-radius: 5px;")
        
       # ventanadeciudad.addWidget(textoclimas, 1, 0)
        textorecomendaciones = QLabel(" Recomendaciones: ")
        textorecomendaciones.setFont(QFont('Times', 20))
        textorecomendaciones.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        textorecomendaciones.setStyleSheet("background-color: #ECF0F1; padding: 5px; border-radius: 5px;")
        
        ventanadeciudad.addWidget(nombreciudad, 1, 1)
        ventanadeciudad.addWidget(textoclimas, 2, 0)
        ventanadeciudad.addWidget(textorecomendaciones, 3, 1)

        listaclimas = QListWidget()
        listaclimas.setStyleSheet("""
        QListWidget {
            border: 1px solid #000000;
            background-color: #F7F9F9;
            border-radius: 15px;
            padding: 2px;
        }
        QListWidget::item {
            padding: 4px;
            color: #2C3E50;
        }
        QListWidget::item:selected {
            background-color: #85C1E9;
            color: #FFFFFF;
        }
    """)
        listarecomendar = QListWidget()
        listarecomendar.setStyleSheet("""
        QListWidget {
            border: 1px solid #000000;
            background-color: #F2F4F4;
            border-radius: 15px;
            padding: 0px;
        }
        QListWidget::item {
            padding: 4px;
            color: #2C3E50;
        }
        QListWidget::item:selected {
            background-color: #48C9B0;
            color: #FFFFFF;
        }
    """)

        ventanadeciudad.setSpacing(10)
        ventanadeciudad.setContentsMargins(5,5,5,5)
        
        for info in informacion_ciudad:
            listaclimas.addItem(info)

        for recommendation in recomendaciones_ciudad:
            listarecomendar.addItem(recommendation)

        ventanadeciudad.addWidget(listaclimas, 2, 0)
        ventanadeciudad.addWidget(listarecomendar, 2, 1)
        return ventanadeciudad

    def null_tipo_busqueda(self):
        '''
        @function null_tipo_busqueda lanza un pop up al usuario que le advierte que su elección es vacia
        '''
        mensajeerror = QMessageBox.critical(self,"Selección nula", " Por favor, elige una opción ", buttons = QMessageBox.Ok)


    def null_cadenabuscar(self):
        '''
         @function null_cadenabuscar lanza un pop up al usuario que le advierte que su cadena es vacia
        '''
        mensajeerror = QMessageBox.critical(self, "Entrada nula", " La entrada es nula  ", buttons = QMessageBox.Ok)

    def cadena_no_encontrada(self):
        '''
        @function cadena_no_encontrada lanza un pop_up que advierte al usuario que su cadena no fue encontrada
        '''
        mensajeerror = QMessageBox.critical(self, "Not Found",  "La cadena no ha sido encontrada, intente nuevamente", buttons = QMessageBox.Ok)


    def realizar_busqueda(self):
        '''
        @func realizar_busqueda al ser clickeado el botón de busqueda o presionado enter en la barra buscadora
        se ejecuta la busqueda, que por el momento solo checa que se haya seleccionado una opción, que la cadena
        no sea vacia y que no sea igual a Cadenanoencontrada, después de eso despliega una ventana provisional de vuelo
        o ciudad
        '''
        tabnueva = self.creador_tab()
        if self.tipodebusqueda == 0:
            self.null_tipo_busqueda()
            return

        if self.cadenabuscar == "":
            self.null_cadenabuscar()
            return

        if self.tipodebusqueda == 1:
            finder = TicketFinder("./data/finder/vuelos.csv")
            codigos_iata = finder.read_ticket(self.cadenabuscar)
            if codigos_iata == "Ticket de vuelo no encontrado":
                self.cadena_no_encontrada()
                return
            else:
                reader_origen = InputCleaner(codigos_iata[0])
                estado_origen = reader_origen.encontrar_mejor_apareamiento()
                reader_destino = InputCleaner(codigos_iata[1])
                estado_destino = reader_destino.encontrar_mejor_apareamiento()

                tabnueva.addLayout(self.ventana_vuelo(codigos_iata[0], estado_origen, codigos_iata[1], estado_destino), 2, 0)


        elif self.tipodebusqueda == 2:
            reader = InputCleaner(self.cadenabuscar)
            cadenaLimpia = reader.encontrar_mejor_apareamiento()

            if cadenaLimpia == "No valid match found":
                self.cadena_no_encontrada()
                return
            else:
                tabnueva.addLayout(self.ventana_ciudad(cadenaLimpia), 2, 0)
        capanueva = QWidget()
        capanueva.setLayout(tabnueva)
        self.tabPrincipal.addWidget(capanueva)
        self.numerotabs += 1
        self.tabPrincipal.setCurrentIndex(self.numerotabs)

def borrar_datos():
    Recommendations.limpiar_base_de_datos()

schedule.every(20).minutes.do(borrar_datos)

app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.exec()

ventana_abierta = True

while ventana_abierta:
    schedule.run_pending()
    ventana_abierta = False
