# -*- coding: utf-8 -*-
#############################
import sys
#############################
#Imports absolutos
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
# Cargando el archivo sinergia
from sinergia import *

class Mast(QMainWindow):
	"""docstring for Raiz"""
	# Constructor de la clase 
	def __init__(self):
		super(Mast, self).__init__()
		QMainWindow.__init__(self)
		
		# Cargamos el archivo ui [Creado por Designer]
		loadUi('ui/principal.ui', self)
		# Le quitamos la barra de titulo para hacerla estilo material design
		self.setWindowFlags(Qt.SplashScreen)

		# Asignamos las respectivas imagenes a los labels
		self.minx.setCursor(Qt.PointingHandCursor)
		self.minx.setScaledContents(True)
		self.minx.setPixmap(QPixmap("img/min.ico"))

		# Label que minimizara y maximizara la ventana
		self.maxb.setCursor(Qt.PointingHandCursor)
		self.maxb.setScaledContents(True)
		self.maxb.setPixmap(QPixmap("img/mx.ico"))

		self.clos.setCursor(Qt.PointingHandCursor)
		self.clos.setScaledContents(True)
		self.clos.setPixmap(QPixmap("img/cierre.ico"))

		# Hacemos que los labels acepten los eventos del raton [click]
		self.minx.mouseReleaseEvent = self.mini
		self.maxb.mouseReleaseEvent = self.maxx
		self.clos.mouseReleaseEvent = self.salir
		
		# Variable para el evento de maximizar y minimizar 
		self.band = False
#.........................................................................................
	#Funciones para cerrar y minimizar la ventana
	def salir(self, event):
		sys.exit()

	def mini(self, event):
		self.setWindowState(Qt.WindowMinimized)
#.............................................................................................
	#Funciones para mover la ventana cuando esta no tenga la barra de titulo
	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.move(self.pos() + event.globalPos() - self.dragPos)
			self.dragPos = event.globalPos()
			event.accept()

	def mousePressEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.dragPos = event.globalPos()
			event.accept()
# ........................................................................................................
	# Funcion para el evento maximizar y minizar
	def maxx(self, event):
		if not self.band:
			self.setWindowState(Qt.WindowMaximized)
			self.band = True
		else:
			# self.setMinimumSize(900, 569)
			self.setWindowState(Qt.WindowNoState)
			self.band = False

			

#.............................................................................................................
# if __name__ == '__main__':
# 	app = QApplication(sys.argv)
# 	ap = Mast()
# 	ap.show()
# 	sys.exit(app.exec_())