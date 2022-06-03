from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi

from RebusGenerator import RebusGenerator

from WordToImage import WordToImage
from ImageToWord import ImageToWord

class MainPage(QMainWindow):

    def __init__(self):
        super().__init__()

        loadUi("mainPage.ui", self)

        self.wordToImgBtn.clicked.connect(self.openWordToImagePage)
        self.imgToWordBtn.clicked.connect(self.openImageToWordPage)
        self.WordToImage = WordToImage()
        self.ImageToWord = ImageToWord()

    def openWordToImagePage(self):
        self.WordToImage.show()

    def openImageToWordPage(self):
        self.ImageToWord.show()