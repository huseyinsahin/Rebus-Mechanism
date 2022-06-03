from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from GuessingGame import GuessingGame

class ImageToWord(QMainWindow):

    def __init__(self):
        super().__init__()

        self.game = GuessingGame()
        self.qLabel = []
        
        loadUi("ImageToWord.ui", self)
        
        self.imageList = self.game.getRebusImage()
        self.createRebus()
        
        self.pushButton.clicked.connect(self.guessCompareRebus)
        self.changeRebusBtn.clicked.connect(self.changeRebus)
        
    def changeRebus(self):
        self.hideImages()
        self.imageList = self.game.changeRebusImage()
        self.createRebus()
        
    def createRebus(self):
        pictureX = 60
        for item  in self.imageList:
            pixmap = QtGui.QPixmap(item[3:])
            image = QtWidgets.QLabel(self.centralwidget)
            image.setGeometry(QtCore.QRect(pictureX, 40, pixmap.width(), pixmap.height()))
            pictureX = pictureX + pixmap.width()-2
            image.setPixmap(pixmap)
            imageName = "image" + str(pictureX)
            self.qLabel.append(image)
            image.setObjectName(imageName)
            image.show()
        
    def guessCompareRebus(self):
        gamerWord = self.textEdit.toPlainText().lower()
        if (self.game.guessWordCompareToRebus(gamerWord)):
            QMessageBox.about(self, "Tebrikler", "Doğru tahmin!")
            self.imageList.clear()
            self.hideImages()
            self.imageList = self.game.getRebusImage()
            self.createRebus()
            self.textEdit.setPlainText("")
        else:
            QMessageBox.about(self, "Üzgünüz", "Yanlış tahmin!")
            self.textEdit.setPlainText("")
            
    def hideImages(self):
        for item in self.qLabel:
            item.setHidden(True)
        
        
        