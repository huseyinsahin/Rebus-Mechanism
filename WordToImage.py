#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi

from PyQt5 import QtCore, QtGui, QtWidgets
from RebusGenerator import RebusGenerator

import random

class WordToImage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.rbGen = RebusGenerator()
        self.qLabel = []
        loadUi("WordToImage.ui", self)
        self.pushButton.clicked.connect(self.generator)
        
    def generator(self):
        word = self.textEdit.toPlainText()
        if word == "":
            QMessageBox.about(self, "Uyarı", "Lütfen kelime giriniz")
            return
        imageList = self.rbGen.generat(word)
        if not imageList:
            QMessageBox.about(self, "Üzgünüz", "Farklı bir kelime giriniz")
            self.textEdit.setPlainText("")
            return

        pictureX = 60
        if len(self.qLabel) > 0:
            self.hideImages()
        for item  in imageList:
            pixmap = QtGui.QPixmap(item[3:])
            image = QtWidgets.QLabel(self.centralwidget)
            #image.setGeometry(QtCore.QRect(pictureX, 210, 100, 100))
            image.setGeometry(QtCore.QRect(pictureX, 210, pixmap.width(), pixmap.height()))
            pictureX = pictureX + pixmap.width()-2
            image.setPixmap(pixmap)
            imageName = "image" + str(pictureX)
            self.qLabel.append(image)
            image.setObjectName(imageName)
            image.show()
            
        if self.rbGen.levenshteinFlag:
            text = QtWidgets.QLabel(self.centralwidget)
            text.setGeometry(QtCore.QRect(115, 360, 500, 20))
            text.setStyleSheet("""font: bold 16px;""")
            pos = 1
            val = ""
            for item in self.rbGen.getDiffList():
                if (pos%2!=0):
                    val = val + item
                if (pos % 2 == 0):
                    val = val + " = " + item
                    if pos > 2:
                        val = val + ", "
                pos += 1
            
            text.setObjectName("textDiffWord" )
            text.setText(val)
            self.qLabel.append(text)
            text.show()
            
    def hideImages(self):
        for item in self.qLabel:
            item.setHidden(True)
        
        