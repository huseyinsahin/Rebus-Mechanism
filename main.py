from PyQt5.QtWidgets import QApplication
from mainPage import MainPage

app = QApplication([])
window = MainPage()
window.show()
app.exec_()
