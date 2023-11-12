from PIL import Image
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import *
import os
app = QApplication([])
window = QWidget()
window.resize(800, 500)
mainLine = QHBoxLayout()
Non = QHBoxLayout()

def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap



app.setStyleSheet("""
        QWidget {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.14 blue, stop: 0.62 purple,stop: 0.90 yellow);
        }
        QPushButton
        {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.14 blue, stop: 0.62 purple,stop: 0.90 yellow);
            border-style: inset;
            font-family: Impact;
            min-width: 6em;
            padding: 6px;
        }

        QPushButton:hover {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.14 blue, stop: 0.62 purple,stop: 0.90 gold);
        }
        QTextEdit
        {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.14 blue, stop: 0.62 purple,stop: 0.90 yellow);

        }
        QTextEdit:hover {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.14 blue, stop: 0.62 purple,stop: 0.90 gold);
        }



""")








windows1 = QLabel("ПАПКА")
windows2 = QLabel("Вліво")
windows3 = QLabel("Вправо")
windows4 = QLabel("ДЗеркало")
windows5 = QLabel("Різкість")
windows6 = QLabel("Ч/Б")
windows7 = QLabel("Фоточка")

mono1 = QPushButton("Папака")
mono2 = QPushButton("Вліво")
mono3 = QPushButton("Вправо")
mono4 = QPushButton("Дзеркало")
mono5 = QPushButton("Різкість")
mono6 = QPushButton("Ч/Б")
text = QListWidget()

Mon = QVBoxLayout()
Mon.addWidget(mono1)
Mon.addWidget(text)
mainLine.addLayout(Mon)
Mon1 = QVBoxLayout()
Mon1.addWidget(windows7)
Non = QHBoxLayout()
Non.addWidget(mono2)
Non.addWidget(mono3)
Non.addWidget(mono4)
Non.addWidget(mono5)
Non.addWidget(mono6)
Mon1.addLayout(Non)
mainLine.addLayout(Mon1)

class WorkPhoto:
    def __init__(self):
        self.image = None
        self.folder = None
        self.filename = None



    def load(self):
        imagePath = os.path.join(self.folder, self.filename)
        self.image = Image.open(imagePath)



    def showImage(self):
        pixel = pil2pixmap(self.image)
        pixel = pixel.scaled(800, 600, Qt.KeepAspectRatio)
        windows7.setPixmap(pixel)


    def rotate_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.showImage()


    def rotate_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.showImage()

work_with_photo = WorkPhoto()

def open_floder():
    work_with_photo.folder = QFileDialog.getExistingDirectory()
    files = os.listdir(work_with_photo.folder)
    text.clear()
    text.addItems(files)


def showChosenImage():
    work_with_photo.filename = text.currentItem().text()
    work_with_photo.load()
    work_with_photo.showImage()

text.currentRowChanged.connect(showChosenImage)
mono2.clicked.connect(work_with_photo.rotate_left)
mono3.clicked.connect(work_with_photo.rotate_right)
mono1.clicked.connect(open_floder)











window.setLayout(mainLine)
window.show()
app.exec()