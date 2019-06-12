# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       login.py
# Autor:        LUIS JOSE IRAHETA MEDRANO
# Copyright:    (c) 2019 LUIS IRAHETA
# ----------------------------------------------------------------------------

__versión__ = "1.0"

"""
El módulo *login* tiene como objetivo mostrar la forma de crear una ventana de login
sencilla.
"""

from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMessageBox, QApplication, QMainWindow, QFrame, QLabel, QComboBox, QLineEdit,
                             QPushButton)

from settings.DB2 import *


# ===================== CLASE ventanaLogin =========================

class ventanaLogin(QMainWindow):
    def __init__(self, parent=None):
        super(ventanaLogin, self).__init__(parent)

        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("./assets/icono.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint |
                            Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 500)

        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(243, 243, 243))
        self.setPalette(paleta)

        self.initUI()

    def initUI(self):

      # ==================== FRAME ENCABEZADO ====================

        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(51, 0, 102))

        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(paleta)
        frame.setFixedWidth(400)
        frame.setFixedHeight(84)
        frame.move(0, 0)

        labelIcono = QLabel(frame)
        labelIcono.setFixedWidth(40)
        labelIcono.setFixedHeight(40)
        labelIcono.setPixmap(QPixmap("./assets/icono.png").scaled(40, 40, Qt.KeepAspectRatio,
                                                                  Qt.SmoothTransformation))
        labelIcono.move(37, 22)

        fuenteTitulo = QFont()
        fuenteTitulo.setPointSize(20)
        fuenteTitulo.setBold(True)

        labelTitulo = QLabel("<font color='white'>Proyección</font>", frame)
        labelTitulo.setFont(fuenteTitulo)
        labelTitulo.move(90, 20)

        fuenteSubtitulo = QFont()
        fuenteSubtitulo.setPointSize(12)

        labelSubtitulo = QLabel("<font color='white'>Pronósticos de ventas"
                                ".</font>", frame)
        labelSubtitulo.setFont(fuenteSubtitulo)
        labelSubtitulo.move(115, 50)

        # ========================================================

        labelUsuario = QLabel("Usuario", self)
        labelUsuario.move(60, 170)

        frameUsuario = QFrame(self)
        frameUsuario.setFrameShape(QFrame.StyledPanel)
        frameUsuario.setFixedWidth(280)
        frameUsuario.setFixedHeight(28)
        frameUsuario.move(60, 196)

        imagenUsuario = QLabel(frameUsuario)
        imagenUsuario.setPixmap(QPixmap("./assets/usuario.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                                       Qt.SmoothTransformation))
        imagenUsuario.move(10, 4)

        self.lineEditUsuario = QLineEdit(frameUsuario)
        self.lineEditUsuario.setFrame(False)
        self.lineEditUsuario.setTextMargins(8, 0, 4, 1)
        self.lineEditUsuario.setFixedWidth(238)
        self.lineEditUsuario.setFixedHeight(26)
        self.lineEditUsuario.move(40, 1)

        # ========================================================

        labelContrasenia = QLabel("Contraseña", self)
        labelContrasenia.move(60, 224)

        frameContrasenia = QFrame(self)
        frameContrasenia.setFrameShape(QFrame.StyledPanel)
        frameContrasenia.setFixedWidth(280)
        frameContrasenia.setFixedHeight(28)
        frameContrasenia.move(60, 250)

        imagenContrasenia = QLabel(frameContrasenia)
        imagenContrasenia.setPixmap(QPixmap("./assets/contrasena.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                                              Qt.SmoothTransformation))
        imagenContrasenia.move(10, 4)

        self.lineEditContrasenia = QLineEdit(frameContrasenia)
        self.lineEditContrasenia.setFrame(False)
        self.lineEditContrasenia.setEchoMode(QLineEdit.Password)
        self.lineEditContrasenia.setTextMargins(8, 0, 4, 1)
        self.lineEditContrasenia.setFixedWidth(238)
        self.lineEditContrasenia.setFixedHeight(26)
        self.lineEditContrasenia.move(40, 1)

      # ================== WIDGETS QPUSHBUTTON ===================

        buttonLogin = QPushButton("Iniciar sesión", self)
        buttonLogin.setFixedWidth(135)
        buttonLogin.setFixedHeight(28)
        buttonLogin.move(60, 286)

        buttonCancelar = QPushButton("Cancelar", self)
        buttonCancelar.setFixedWidth(135)
        buttonCancelar.setFixedHeight(28)
        buttonCancelar.move(205, 286)

      # ==================== MÁS INFORMACIÓN =====================

        labelInformacion = QLabel(
            "<a href='https://github.com/liluisjose1'>Más información</a>.", self)
        labelInformacion.setOpenExternalLinks(True)
        labelInformacion.setToolTip("Help")
        labelInformacion.move(15, 344)

      # ==================== SEÑALES BOTONES =====================

        buttonLogin.clicked.connect(self.Login)
        buttonCancelar.clicked.connect(self.close)

  # ======================= FUNCIONES ============================

    def Login(self):
        usuario = self.lineEditUsuario.text()
        contrasenia = self.lineEditContrasenia.text()

        QMessageBox.warning(
              self, "info", "Prueba")
        self.lineEditUsuario.clear()
        self.lineEditContrasenia.clear()

    def keyPressEvent(self, event):
      if event.key() == Qt.Key_Return:
        self.Login()
      elif event.key() == Qt.Key_Escape:
        self.close()
      elif event.key() == Qt.Key_F1:
        QMessageBox.question(
            self, "Mensaje", "Oprimiste la tecla F1")

# ================================================================


if __name__ == '__main__':

    import sys
    aplicacion = QApplication(sys.argv)

    fuente = QFont()
    fuente.setPointSize(10)
    fuente.setFamily("Bahnschrift Light")

    aplicacion.setFont(fuente)

    ventana = ventanaLogin()
    ventana.show()

    sys.exit(aplicacion.exec_())
