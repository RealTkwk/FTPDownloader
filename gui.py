# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FTPDownloader.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(632, 670)
        MainWindow.setMinimumSize(QtCore.QSize(632, 670))
        MainWindow.setMaximumSize(QtCore.QSize(632, 670))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 61, 21))
        self.label.setObjectName("label")
        self.lineIP = QtWidgets.QLineEdit(self.centralwidget)
        self.lineIP.setGeometry(QtCore.QRect(80, 10, 113, 21))
        self.lineIP.setInputMask("")
        self.lineIP.setAlignment(QtCore.Qt.AlignCenter)
        self.lineIP.setPlaceholderText("")
        self.lineIP.setObjectName("lineIP")
        self.lineUser = QtWidgets.QLineEdit(self.centralwidget)
        self.lineUser.setGeometry(QtCore.QRect(270, 10, 113, 21))
        self.lineUser.setAlignment(QtCore.Qt.AlignCenter)
        self.lineUser.setObjectName("lineUser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 10, 61, 21))
        self.label_2.setObjectName("label_2")
        self.linePass = QtWidgets.QLineEdit(self.centralwidget)
        self.linePass.setGeometry(QtCore.QRect(480, 10, 113, 21))
        self.linePass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePass.setObjectName("linePass")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 10, 61, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(12, 90, 60, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 90, 131, 16))
        self.label_5.setObjectName("label_5")
        self.lineCaso = QtWidgets.QLineEdit(self.centralwidget)
        self.lineCaso.setGeometry(QtCore.QRect(12, 360, 241, 20))
        self.lineCaso.setObjectName("lineCaso")
        self.lineNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.lineNombre.setGeometry(QtCore.QRect(270, 360, 141, 20))
        self.lineNombre.setObjectName("lineNombre")
        self.lineNombreMainframe = QtWidgets.QLineEdit(self.centralwidget)
        self.lineNombreMainframe.setGeometry(QtCore.QRect(420, 360, 171, 20))
        self.lineNombreMainframe.setObjectName("lineNombreMainframe")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(12, 340, 47, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(270, 340, 47, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(420, 340, 120, 20))
        self.label_8.setObjectName("label_8")
        self.pushAddPrueba = QtWidgets.QPushButton(self.centralwidget)
        self.pushAddPrueba.setGeometry(QtCore.QRect(10, 390, 51, 23))
        self.pushAddPrueba.setObjectName("pushAddPrueba")
        self.pushDeletePrueba = QtWidgets.QPushButton(self.centralwidget)
        self.pushDeletePrueba.setGeometry(QtCore.QRect(70, 390, 51, 23))
        self.pushDeletePrueba.setObjectName("pushDeletePrueba")
        self.pushRenamePrueba = QtWidgets.QPushButton(self.centralwidget)
        self.pushRenamePrueba.setGeometry(QtCore.QRect(130, 390, 64, 23))
        self.pushRenamePrueba.setObjectName("pushRenamePrueba")
        self.pushClearPruebas = QtWidgets.QPushButton(self.centralwidget)
        self.pushClearPruebas.setGeometry(QtCore.QRect(200, 390, 51, 23))
        self.pushClearPruebas.setObjectName("pushClearPruebas")
        self.pushClearAll = QtWidgets.QPushButton(self.centralwidget)
        self.pushClearAll.setGeometry(QtCore.QRect(500, 53, 75, 23))
        self.pushClearAll.setObjectName("pushClearAll")
        self.pushDownload = QtWidgets.QPushButton(self.centralwidget)
        self.pushDownload.setGeometry(QtCore.QRect(244, 620, 71, 23))
        self.pushDownload.setObjectName("pushDownload")
        self.checkTx = QtWidgets.QCheckBox(self.centralwidget)
        self.checkTx.setGeometry(QtCore.QRect(603, 360, 20, 20))
        self.checkTx.setText("")
        self.checkTx.setObjectName("checkTx")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(600, 342, 47, 13))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(304, 433, 20, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(12, 37, 100, 30))
        self.label_11.setObjectName("label_11")
        self.lineReq = QtWidgets.QLineEdit(self.centralwidget)
        self.lineReq.setGeometry(QtCore.QRect(12, 61, 261, 19))
        self.lineReq.setInputMask("")
        self.lineReq.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineReq.setPlaceholderText("")
        self.lineReq.setObjectName("lineReq")
        self.pushRenameArchivo = QtWidgets.QPushButton(self.centralwidget)
        self.pushRenameArchivo.setGeometry(QtCore.QRect(440, 390, 62, 23))
        self.pushRenameArchivo.setObjectName("pushRenameArchivo")
        self.pushDeleteArchivo = QtWidgets.QPushButton(self.centralwidget)
        self.pushDeleteArchivo.setGeometry(QtCore.QRect(374, 390, 51, 23))
        self.pushDeleteArchivo.setObjectName("pushDeleteArchivo")
        self.pushAddArchivo = QtWidgets.QPushButton(self.centralwidget)
        self.pushAddArchivo.setGeometry(QtCore.QRect(308, 390, 51, 23))
        self.pushAddArchivo.setObjectName("pushAddArchivo")
        self.pushClearArchivos = QtWidgets.QPushButton(self.centralwidget)
        self.pushClearArchivos.setGeometry(QtCore.QRect(520, 390, 51, 23))
        self.pushClearArchivos.setObjectName("pushClearArchivos")
        self.listPruebas = QtWidgets.QListWidget(self.centralwidget)
        self.listPruebas.setGeometry(QtCore.QRect(12, 108, 241, 230))
        self.listPruebas.setObjectName("listPruebas")
        self.listArchivos = QtWidgets.QListWidget(self.centralwidget)
        self.listArchivos.setGeometry(QtCore.QRect(269, 108, 351, 230))
        self.listArchivos.setObjectName("listArchivos")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 86, 650, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 425, 650, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 39, 650, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.plainTextLog = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextLog.setGeometry(QtCore.QRect(10, 450, 611, 160))
        self.plainTextLog.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.plainTextLog.setObjectName("plainTextLog")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(617, 635, 16, 16))
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 610, 611, 5))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.pushStop = QtWidgets.QPushButton(self.centralwidget)
        self.pushStop.setGeometry(QtCore.QRect(314, 620, 71, 23))
        self.pushStop.setObjectName("pushStop")
        self.label.raise_()
        self.lineIP.raise_()
        self.lineUser.raise_()
        self.label_2.raise_()
        self.linePass.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.lineCaso.raise_()
        self.lineNombre.raise_()
        self.lineNombreMainframe.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.pushAddPrueba.raise_()
        self.pushDeletePrueba.raise_()
        self.pushRenamePrueba.raise_()
        self.pushClearPruebas.raise_()
        self.checkTx.raise_()
        self.label_9.raise_()
        self.pushDownload.raise_()
        self.pushClearAll.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.lineReq.raise_()
        self.pushRenameArchivo.raise_()
        self.pushDeleteArchivo.raise_()
        self.pushAddArchivo.raise_()
        self.pushClearArchivos.raise_()
        self.listPruebas.raise_()
        self.listArchivos.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.plainTextLog.raise_()
        self.pushButton.raise_()
        self.progressBar.raise_()
        self.pushStop.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mainframe Downloader"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>IP:</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>User:</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Password:</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Pruebas</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Archivos</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Caso</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>Nombre</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>Archivo en Mainframe</p></body></html>"))
        self.pushAddPrueba.setText(_translate("MainWindow", "Agregar"))
        self.pushDeletePrueba.setText(_translate("MainWindow", "Eliminar"))
        self.pushRenamePrueba.setText(_translate("MainWindow", "Renombrar"))
        self.pushClearPruebas.setText(_translate("MainWindow", "Reset"))
        self.pushClearAll.setText(_translate("MainWindow", "Limpiar todo"))
        self.pushDownload.setText(_translate("MainWindow", "Descargar"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">.Tx</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Log</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Requerimiento</span></p></body></html>"))
        self.pushRenameArchivo.setText(_translate("MainWindow", "Renombrar"))
        self.pushDeleteArchivo.setText(_translate("MainWindow", "Eliminar"))
        self.pushAddArchivo.setText(_translate("MainWindow", "Agregar"))
        self.pushClearArchivos.setText(_translate("MainWindow", "Reset"))
        self.pushButton.setText(_translate("MainWindow", "i"))
        self.pushStop.setText(_translate("MainWindow", "Cancelar"))

