from PIL import Image, ImageFilter, ImageEnhance
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
windows8 = QLabel("Яскравість")
windows9 = QLabel("Блюр")
windows10 = QLabel("Контрастність")

mono1 = QPushButton("Папака")
mono2 = QPushButton("Вліво")
mono3 = QPushButton("Вправо")
mono4 = QPushButton("Дзеркало")
mono5 = QPushButton("Різкість")
mono6 = QPushButton("Ч/Б")
mono7 = QPushButton("Яскравість")
mono8 = QPushButton("Блюр")
mono9 = QPushButton("Контрастність")
mono10 = QPushButton("Скинути фільтри")

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
Non.addWidget(mono7)
Non.addWidget(mono8)
Non.addWidget(mono9)
Non.addWidget(mono10)
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

    def mirror(self):
        if self.image:
            self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.showImage()

    def apply_sharpness(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.SHARPEN)
            self.showImage()

    def convert_to_bw(self):
        if self.image:
            self.image = self.image.convert("L").convert("RGBA")
            self.showImage()

    def apply_blur(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.BLUR)
            self.showImage()

    def adjust_brightness(self, factor):
        if self.image:
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(factor)
            self.showImage()

    def adjust_contrast(self, factor):
        if self.image:
            enhancer = ImageEnhance.Contrast(self.image)
            self.image = enhancer.enhance(factor)
            self.showImage()

    def reset_filters(self):
        if self.image:
            # Reload the original image without any filters
            self.load()
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
mono1.clicked.connect(open_floder)
mono2.clicked.connect(work_with_photo.rotate_left)
mono3.clicked.connect(work_with_photo.rotate_right)
mono4.clicked.connect(work_with_photo.mirror)
mono5.clicked.connect(work_with_photo.apply_sharpness)
mono6.clicked.connect(work_with_photo.convert_to_bw)
mono7.clicked.connect(lambda: work_with_photo.adjust_brightness(1.5))
mono8.clicked.connect(work_with_photo.apply_blur)
mono9.clicked.connect(lambda: work_with_photo.adjust_contrast(1.5))
mono10.clicked.connect(work_with_photo.reset_filters)








window.setLayout(mainLine)
window.show()
app.exec()