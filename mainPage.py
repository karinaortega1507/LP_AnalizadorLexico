# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainPageOOiOEq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Analizador(object):
    def setupUi(self, Analizador):
        if not Analizador.objectName():
            Analizador.setObjectName(u"Analizador")
        Analizador.resize(778, 353)
        Analizador.setStyleSheet(u"selection-background-color: rgb(223, 208, 255);")
        self.btnLexic = QPushButton(Analizador)
        self.btnLexic.setObjectName(u"btnLexic")
        self.btnLexic.setGeometry(QRect(330, 190, 75, 23))
        self.cajaCodigo = QPlainTextEdit(Analizador)
        self.cajaCodigo.setObjectName(u"cajaCodigo")
        self.cajaCodigo.setGeometry(QRect(30, 150, 201, 151))
        self.tittle = QLabel(Analizador)
        self.tittle.setObjectName(u"tittle")
        self.tittle.setGeometry(QRect(320, 20, 151, 51))
        self.tittle.setStyleSheet(u"font: 75 10pt \"Tahoma\";\n"
"font: 75 12pt \"Tahoma\";\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"Tahoma\";\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.labelIngreseCodigo = QLabel(Analizador)
        self.labelIngreseCodigo.setObjectName(u"labelIngreseCodigo")
        self.labelIngreseCodigo.setGeometry(QRect(40, 100, 191, 21))
        self.labelIngreseCodigo.setStyleSheet(u"font: 75 8pt \"Tahoma\";\n"
"border-bottom-color: rgb(85, 170, 255);")
        self.labelOpciones = QLabel(Analizador)
        self.labelOpciones.setObjectName(u"labelOpciones")
        self.labelOpciones.setGeometry(QRect(280, 140, 171, 31))
        self.labelOpciones.setStyleSheet(u"font: 75 10pt \"Tahoma\";\n"
"font: 75 9pt \"Arial Narrow\";\n"
"font: 8pt \"Tahoma\";\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btnSintact = QPushButton(Analizador)
        self.btnSintact.setObjectName(u"btnSintact")
        self.btnSintact.setGeometry(QRect(330, 230, 75, 23))
        self.labelResultados = QLabel(Analizador)
        self.labelResultados.setObjectName(u"labelResultados")
        self.labelResultados.setGeometry(QRect(510, 100, 241, 31))
        self.labelResultados.setStyleSheet(u"font: 75 10pt \"Tahoma\";\n"
"font: 8pt \"Tahoma\";\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btnAnalizerNewCode = QPushButton(Analizador)
        self.btnAnalizerNewCode.setObjectName(u"btnAnalizerNewCode")
        self.btnAnalizerNewCode.setGeometry(QRect(280, 300, 191, 23))
        self.textEdit = QTextEdit(Analizador)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(513, 160, 231, 141))
        QWidget.setTabOrder(self.cajaCodigo, self.btnLexic)
        QWidget.setTabOrder(self.btnLexic, self.btnSintact)

        self.retranslateUi(Analizador)

        QMetaObject.connectSlotsByName(Analizador)
    # setupUi

    def retranslateUi(self, Analizador):
        Analizador.setWindowTitle(QCoreApplication.translate("Analizador", u"Form", None))
#if QT_CONFIG(tooltip)
        Analizador.setToolTip(QCoreApplication.translate("Analizador", u"<html><head/><body><p><span style=\" font-weight:600;\">Analizador de C\u00f3digo_LP</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnLexic.setText(QCoreApplication.translate("Analizador", u"L\u00e9xico", None))
        self.tittle.setText(QCoreApplication.translate("Analizador", u"Analizador de c\u00f3digo", None))
        self.labelIngreseCodigo.setText(QCoreApplication.translate("Analizador", u"Ingrese su c\u00f3digo para analizar aqu\u00ed", None))
        self.labelOpciones.setText(QCoreApplication.translate("Analizador", u"Seleccione una opci\u00f3n para analizar", None))
        self.btnSintact.setText(QCoreApplication.translate("Analizador", u"Sint\u00e1tico", None))
        self.labelResultados.setText(QCoreApplication.translate("Analizador", u"Los resultados se muestran a continuaci\u00f3n", None))
        self.btnAnalizerNewCode.setText(QCoreApplication.translate("Analizador", u"Analizar nuevo c\u00f3digo", None))
    # retranslateUi

