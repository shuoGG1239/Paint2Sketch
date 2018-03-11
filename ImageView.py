from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

import paint2sketch
from ui_frameimageview import Ui_frameImageView


class ImageView(QWidget):
    def __init__(self):
        super(ImageView, self).__init__()
        self.ui = Ui_frameImageView()
        self.ui.setupUi(self)
        ret_img = paint2sketch.get_sketch("remu1.jpg")
        height, width = ret_img.shape
        bytes_per_line = width
        q_image = QImage(ret_img.data, width, height, bytes_per_line, QImage.Format_Indexed8)
        self.image = QPixmap.fromImage(q_image)
        self.ui.labelImage.setPixmap(
            self.image.scaled(self.ui.labelImage.width(), self.ui.labelImage.height(), Qt.KeepAspectRatio))
