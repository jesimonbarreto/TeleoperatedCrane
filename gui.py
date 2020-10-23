# -*- coding: utf-8 -*-
from connection import Connection
import time
# Form implementation generated from reading ui file 'C:\Users\JB\Documents\lab_3\guindaste.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
#
# Convertido para PyQt5

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_Guindaste(object):

    def setupUi(self, Guindaste):
        #create connection
        control = Connection()

        # Cores da GUI
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtGui.QColor(225,230,245))
        palette.setColor(QtGui.QPalette.Light, QtGui.QColor(190,190,235))

        # Janela principal da GUI
        Guindaste.setObjectName(_fromUtf8("Guindaste"))
        Guindaste.resize(875, 650)
        Guindaste.setPalette(palette)
        Guindaste.setFont(QtGui.QFont("Helvetica"))

        # Titulo central "Controle do Guindaste"
        self.label_5 = QtWidgets.QLabel(Guindaste)
        self.label_5.setGeometry(QtCore.QRect(245, 10, 400, 41))
        self.label_5.setStyleSheet(_fromUtf8("font: 18pt \"Helvetica\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        # Titulo esquerdo superior "Estado do Guindaste"
        self.label_6 = QtWidgets.QLabel(Guindaste)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 221, 41))
        self.label_6.setStyleSheet(_fromUtf8("font: 14pt \"Helvetica\";"))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        # Imagem guindaste
        self.pixmap = QtGui.QPixmap('crane.png')
        self.label_13 = QtWidgets.QLabel(Guindaste)
        self.label_13.setPixmap(self.pixmap)
        self.label_13.setGeometry(QtCore.QRect(30, 100, 170, 230))
        self.label_13.setScaledContents(True)

        #lcd colors
        self.off_color = QtGui.QPalette()
        self.off_color.setColor(QtGui.QPalette.Light, QtGui.QColor(255,145,145))
        self.on_color = QtGui.QPalette()
        self.on_color.setColor(QtGui.QPalette.Light, QtGui.QColor(145,225,145))

        # LCDs superiores esquerdos
        self.lcdNumber_4 = QtWidgets.QLCDNumber(Guindaste)
        self.lcdNumber_4.setGeometry(QtCore.QRect(180, 170, 60, 30))
        self.lcdNumber_4.setObjectName(_fromUtf8("lcdNumber_4"))
        self.lcdNumber_4.setPalette(self.off_color)

        self.label_10 = QtWidgets.QLabel(Guindaste)
        self.label_10.setGeometry(QtCore.QRect(150, 140, 121, 31))
        self.label_10.setObjectName(_fromUtf8("label_10"))

        self.lcdNumber_5 = QtWidgets.QLCDNumber(Guindaste)
        self.lcdNumber_5.setGeometry(QtCore.QRect(180, 240, 60, 30))
        self.lcdNumber_5.setObjectName(_fromUtf8("lcdNumber_5"))
        self.lcdNumber_5.setPalette(self.off_color)

        self.label_12 = QtWidgets.QLabel(Guindaste)
        self.label_12.setGeometry(QtCore.QRect(150, 210, 131, 31))
        self.label_12.setObjectName(_fromUtf8("label_12"))

        # Tela central
        self.graphicsView = QtWidgets.QGraphicsView(Guindaste)
        self.graphicsView.setGeometry(QtCore.QRect(287.5, 100, 300, 221))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))

        # LCDs superiores direitos
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Guindaste)
        self.lcdNumber_2.setGeometry(QtCore.QRect(701.25, 120, 60, 30))
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))

        self.label_7 = QtWidgets.QLabel(Guindaste)
        self.label_7.setGeometry(QtCore.QRect(660, 90, 160, 31))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.lcdNumber = QtWidgets.QLCDNumber(Guindaste)
        self.lcdNumber.setGeometry(QtCore.QRect(701.25, 190, 60, 30))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))

        self.label = QtWidgets.QLabel(Guindaste)
        self.label.setGeometry(QtCore.QRect(660, 160, 131, 31))
        self.label.setObjectName(_fromUtf8("label"))

        self.lcdNumber_6 = QtWidgets.QLCDNumber(Guindaste)
        self.lcdNumber_6.setGeometry(QtCore.QRect(701.25, 260, 60, 30))
        self.lcdNumber_6.setObjectName(_fromUtf8("lcdNumber_6"))
        self.lcdNumber_6.setPalette(self.off_color)

        self.label_8 = QtWidgets.QLabel(Guindaste)
        self.label_8.setGeometry(QtCore.QRect(660, 230, 131, 31))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        # Titulo esquerdo "Controles do Guindaste"
        self.label_2 = QtWidgets.QLabel(Guindaste)
        self.label_2.setGeometry(QtCore.QRect(10, 333, 241, 41))
        self.label_2.setStyleSheet(_fromUtf8("font: 14pt \"Helvetica\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        # Quadro inferior esquerdo "Controle do Guindaste"
        self.groupBox_4 = QtWidgets.QGroupBox(Guindaste)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 380, 181, 151))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))

        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 35, 80, 30))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 90, 80, 30))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        # Quadro inferior esquerdo "Controle do imã"
        self.groupBox_3 = QtWidgets.QGroupBox(Guindaste)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 540, 181, 101))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))

        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 40, 80, 30))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

        # Quadro inferior central "Controle Direcional com Botões"
        self.groupBox = QtWidgets.QGroupBox(Guindaste)
        self.groupBox.setGeometry(QtCore.QRect(200, 380, 381, 261))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(150, 35, 80, 30))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 35, 130, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 85, 80, 45))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 195, 80, 45))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(63, 140, 80, 45))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(237, 140, 80, 45))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        # Quadro inferior direito "Controle Direcional Deslizante"
        self.groupBox_2 = QtWidgets.QGroupBox(Guindaste)
        self.groupBox_2.setGeometry(QtCore.QRect(590, 380, 275, 261))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))

        self.dial = QtWidgets.QDial(self.groupBox_2)
        self.dial.setGeometry(QtCore.QRect(45, 110, 100, 64))
        self.dial.setObjectName(_fromUtf8("dial"))

        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(45, 80, 100, 30))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.verticalSlider = QtWidgets.QSlider(self.groupBox_2)
        self.verticalSlider.setGeometry(QtCore.QRect(190, 80, 15, 150))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))

        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(140, 30, 120, 30))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        # Janelas de confirmacao
        self.confirmWindow = QtWidgets.QMessageBox()
        self.confirmWindow.setIcon(QtWidgets.QMessageBox.Question)
        self.confirmWindow.setWindowTitle('Controle do Imã')
        self.confirmWindow.setText('Desligar imã?')
        self.confirmWindow.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        self.confirmWindow.setDefaultButton(QtWidgets.QMessageBox.No)
        self.buttonY = self.confirmWindow.button(QtWidgets.QMessageBox.Yes)
        self.buttonY.setText('Sim')
        self.buttonN = self.confirmWindow.button(QtWidgets.QMessageBox.No)
        self.buttonN.setText('Não')

        self.confirmWindow_2 = QtWidgets.QMessageBox()
        self.confirmWindow_2.setIcon(QtWidgets.QMessageBox.Question)
        self.confirmWindow_2.setWindowTitle('Controle do Guindaste')
        self.confirmWindow_2.setText("AVISO: Imã ligado.\nDesligue-o antes de concluir esta ação.")
        self.confirmWindow_2.setStandardButtons(QtWidgets.QMessageBox.Ok)


        self.groupBox_4.raise_()
        self.groupBox_3.raise_()
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.lcdNumber.raise_()
        self.label.raise_()
        self.verticalSlider.raise_()
        self.graphicsView.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.lcdNumber_2.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_10.raise_()
        self.lcdNumber_4.raise_()
        self.label_12.raise_()
        self.lcdNumber_5.raise_()
        self.lcdNumber_6.raise_()
        self.lcdNumber_4.display('Off')
        self.lcdNumber_6.display('Off')
        self.lcdNumber_5.display('Off')
        self.lcdNumber_2.display(0)

        #Start conection Connection
        def connect():
            print('Start Connection')
            _, status = control.init_connection(ip = '127.0.0.1' , port = 19997)
            if status:
                self.lcdNumber_4.display('UP')
                self.lcdNumber_4.setPalette(self.on_color)
            else:
                self.lcdNumber_4.display('Off')
                self.lcdNumber_4.setPalette(self.off_color)

        self.pushButton_7.clicked.connect(connect)
        
        # Transforma os algulos negativos para positivos
        def getAngle():
            angle = control.getCurrentAngleClaw()
            if angle < 0:
                angle += 360
            return angle

        # Left
        def left():
            #try catch no int
            cod = self.lineEdit.text()
            try:
                old_angle = getAngle()
                step = float(cod)
                status = control.commandLeft(step)
            except:
                status = False
            if status:
                desired_angle = old_angle + step
                cnt = 0
                angle = getAngle()
                while(abs(angle - desired_angle) > 0.05 and cnt < 500):
                    self.lcdNumber_2.display(round(angle))
                    app.processEvents()
                    angle = getAngle()
                    cnt+=1
            else:
                print('Não pode ser alterado por não estar ligado ou Falta valor de passo no campo acima')

        self.pushButton.clicked.connect(left)

        # Right
        def right():
            cod = self.lineEdit.text()
            try:
                old_angle = getAngle()
                step = float(cod)
                status = control.commandRight(step)
            except:
                status = False
            if status:
                desired_angle = old_angle - step
                cnt = 0
                angle = getAngle()
                while(abs(angle - desired_angle) > 0.05 and cnt < 500):
                    self.lcdNumber_2.display(round(angle))
                    app.processEvents()
                    angle = getAngle()
                    cnt+=1
            else:
                print('Não pode ser alterado por não estar ligado ou Falta valor de passo no campo acima')

        self.pushButton_4.clicked.connect(right)

        # Up
        def Up():
            cod = self.lineEdit.text()
            try:
                step = float(cod)
                status = control.commandUp(step)
            except:
                status = False 
            
            if status:

                dist = control.getStatusDist()
                self.lcdNumber.display(dist)
            else:
                print('Não pode ser alterado por não estar ligado ou Falta valor de passo no campo acima')

        self.pushButton_5.clicked.connect(Up)

        # Down
        def Down():
            cod = self.lineEdit.text()
            try:
                step = float(cod)
                status = control.commandDown(step)
            except:
                status = False
            
            if status:
                dist = control.getStatusDist()
                self.lcdNumber.display(dist)
            else:
                print('Não pode ser alterado por não estar ligado ou Falta valor de passo no campo acima')
        self.pushButton_3.clicked.connect(Down)

        # Ima
        def magnet():
            if control.craneStatus and control.connectionStatus:
                status = control.getMagnetStatus()
                if status:
                    self.confirmWindow.exec_()
                    if self.confirmWindow.clickedButton() == self.buttonY:
                        control.commandMagnetOnOff()
                        print('Imã Desligado')
                        self.lcdNumber_6.display('Off')
                        self.lcdNumber_6.setPalette(self.off_color)
                else:
                    control.commandMagnetOnOff()
                    print('Imã Ligado')
                    self.lcdNumber_6.display('UP')
                    self.lcdNumber_6.setPalette(self.on_color)
            else:
                print('Sem conexão ou guindaste desligado.')
        self.pushButton_6.clicked.connect(magnet)

        # On/Off Crane
        def crane():
            if control.connectionStatus:
                status = control.getCraneStatus()
                if status:
                    if control.getMagnetStatus():
                        self.confirmWindow_2.exec_()
                        print("Não é possível desligar o guindaste com o imã ainda ligado.")
                    else:
                        print('Desligado')
                        control.commandCraneOnOff()
                        self.lcdNumber_5.display('OFF')
                        self.lcdNumber_5.setPalette(self.off_color)
                        self.lcdNumber_2.display(0)
                else:
                    print('Ligado')
                    control.commandCraneOnOff()
                    self.lcdNumber_5.display('UP')
                    self.lcdNumber_5.setPalette(self.on_color)
                    
                    angle = getAngle()
                    self.lcdNumber_2.display(round(angle))
                        
                    dist = control.getStatusDist()
                    self.lcdNumber.display(dist)
            else:
                print('Sem conexão.')
        self.pushButton_2.clicked.connect(crane)

        self.retranslateUi(Guindaste)
        QtCore.QMetaObject.connectSlotsByName(Guindaste)

    def retranslateUi(self, Guindaste):
        Guindaste.setWindowTitle(_translate("Guindaste", "Dialog", None))
        self.label.setText(_translate("Guindaste", "Distância para o piso:", None))
        self.label_2.setText(_translate("Guindaste", "Controles do Guindaste:", None))
        self.label_4.setText(_translate("Guindaste", "Altura do Guincho", None))
        self.label_5.setText(_translate("Guindaste", "GUINDASTE TELEOPERADO", None))
        self.label_6.setText(_translate("Guindaste", "Estado do Guindaste:", None))
        self.label_7.setText(_translate("Guindaste", "Ângulo da Lança [Graus]:", None))
        self.label_8.setText(_translate("Guindaste", "Estado do imã:", None))
        self.groupBox.setTitle(_translate("Guindaste", "Controle Direcional com Botões", None))
        self.label_9.setText(_translate("Guindaste", "Movimento por Clique:", None))
        self.pushButton_5.setText(_translate("Guindaste", "Subir\nGuincho", None))
        self.pushButton_4.setText(_translate("Guindaste", "Lança p/\nDireita", None))
        self.pushButton_3.setText(_translate("Guindaste", "Baixar\nGuincho", None))
        self.pushButton.setText(_translate("Guindaste", "Lança p/\nEsquerda", None))
        self.groupBox_2.setTitle(_translate("Guindaste", "Controle Direcional Deslizante", None))
        self.label_3.setText(_translate("Guindaste", "Ângulo da Lança", None))
        self.groupBox_3.setTitle(_translate("Guindaste", "Controle do Imã", None))
        self.pushButton_6.setText(_translate("Guindaste", "On/Off", None))
        self.groupBox_4.setTitle(_translate("Guindaste", "Sistema do Guindaste", None))
        self.pushButton_2.setText(_translate("Guindaste", "On/Off", None))
        self.pushButton_7.setText(_translate("Guindaste", "Conectar", None))
        self.label_10.setText(_translate("Guindaste", "Estado de Conexão:", None))
        self.label_12.setText(_translate("Guindaste", "Estado do Guindaste:", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Guindaste = QtWidgets.QDialog()
    ui = Ui_Guindaste()
    ui.setupUi(Guindaste)
    Guindaste.show()
    sys.exit(app.exec_())
