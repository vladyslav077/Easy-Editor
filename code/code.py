from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
window.resize(800, 550)



menuBth = QPushButton("Вліво")
restBth = QPushButton("Вправо")
rektorBth = QPushButton("Різкість")
tagsBth = QPushButton("Ч/Б")
tags2Bth = QPushButton("Папка")
fara = QListWidget()


mainLine = QHBoxLayout()
qLine = QHBoxLayout()
mainLine.addLayout(qLine)

firstLine = QVBoxLayout()
firstLine.addWidget(tags2Bth)
firstLine.addWidget(fara)



mainLine.addLayout(firstLine)

secondline = QVBoxLayout()



v2 = QVBoxLayout()




window.setLayout(mainLine)
window.show()
app.exec()