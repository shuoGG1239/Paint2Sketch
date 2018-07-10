from PyQt5.QtCore import Qt, pyqtSlot, QFileInfo
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QFrame, QFileDialog
from QCandyUi.CandyWindow import colorful

import paint2sketch
from ui_frameimageview import Ui_frameImageView

@colorful('blue')
class ImageView(QWidget):
    img_path = "sakura1.jpg"
    sketch_pixmap = None

    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_frameImageView()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)
        self.sketch_pixmap = self.get_sketch_pixmap(self.img_path, (2, 2), 128, 255)
        self.set_label_image(self.ui.labelImageDst, self.sketch_pixmap)
        self.set_label_image(self.ui.labelImageSrc, QPixmap(self.img_path))
        self.ui.labelImageSrc.setFrameShape(QFrame.Box)
        self.ui.labelImageDst.setFrameShape(QFrame.Box)
        self.init_slider()

    @staticmethod
    def set_label_image(label, pixmap):
        """
        pixmap适应label
        :param label:
        :param pixmap:
        :return:
        """
        label.setPixmap(pixmap.scaled(
            label.width(), label.height(), Qt.KeepAspectRatio))

    @staticmethod
    def get_sketch_pixmap(image_url, conv_core, t1, t2):
        """
        根据调参值得到对应的线稿图
        :param image_url:
        :param conv_core:
        :param t1:
        :param t2:
        :return: QPixmap
        """
        img_mat = paint2sketch.get_sketch(image_url, conv_core, t1, t2)
        height, width = img_mat.shape
        bytes_per_line = width
        q_image = QImage(img_mat.data, width, height,
                         bytes_per_line, QImage.Format_Indexed8)
        return QPixmap.fromImage(q_image)

    def init_slider(self):
        self.ui.horizontalSliderConvCoreX.setMaximum(10)
        self.ui.horizontalSliderConvCoreX.setSingleStep(1)
        self.ui.horizontalSliderConvCoreX.setPageStep(1)
        self.ui.horizontalSliderConvCoreY.setMaximum(10)
        self.ui.horizontalSliderConvCoreY.setSingleStep(1)
        self.ui.horizontalSliderConvCoreY.setPageStep(1)
        self.ui.horizontalSliderT1.setMaximum(255)
        self.ui.horizontalSliderT1.setSingleStep(1)
        self.ui.horizontalSliderT1.setPageStep(1)
        self.ui.horizontalSliderT2.setMaximum(255)
        self.ui.horizontalSliderT2.setSingleStep(1)
        self.ui.horizontalSliderT2.setPageStep(1)
        # init value
        self.ui.horizontalSliderConvCoreX.setValue(2)
        self.ui.horizontalSliderConvCoreY.setValue(2)
        self.ui.horizontalSliderT1.setValue(128)
        self.ui.horizontalSliderT2.setValue(255)

    @pyqtSlot()
    def on_pushButtonOpen_clicked(self):
        img_full_path = QFileDialog.getOpenFileName()[0]
        if img_full_path is None or img_full_path == '':
            return
        self.load_transfer_image(img_full_path)

    @pyqtSlot()
    def on_pushButtonSave_clicked(self):
        file_full_path = QFileDialog.getSaveFileName()[0]
        if file_full_path is None or file_full_path == '':
            return
        self.sketch_pixmap.save(file_full_path + '.jpg')

    def load_transfer_image(self, img_url):
        """
        载入加处理加展示图片一条龙
        :param img_url:
        :return:
        """
        self.img_path = img_url
        core_X = self.ui.horizontalSliderConvCoreX.value()
        core_Y = self.ui.horizontalSliderConvCoreY.value()
        t1 = self.ui.horizontalSliderT1.value()
        t2 = self.ui.horizontalSliderT2.value()
        self.sketch_pixmap = self.get_sketch_pixmap(
            self.img_path, (core_X, core_Y), t1, t2)
        self.set_label_image(self.ui.labelImageDst, self.sketch_pixmap)
        self.set_label_image(self.ui.labelImageSrc, QPixmap(self.img_path))

    @pyqtSlot(int)
    def on_horizontalSliderConvCoreX_valueChanged(self, value):
        core_X = value
        core_Y = self.ui.horizontalSliderConvCoreY.value()
        t1 = self.ui.horizontalSliderT1.value()
        t2 = self.ui.horizontalSliderT2.value()
        self.sketch_pixmap = self.get_sketch_pixmap(
            self.img_path, (core_X, core_Y), t1, t2)
        self.set_label_image(self.ui.labelImageDst, self.sketch_pixmap)

    @pyqtSlot(int)
    def on_horizontalSliderConvCoreY_valueChanged(self, value):
        core_X = self.ui.horizontalSliderConvCoreX.value()
        core_Y = value
        t1 = self.ui.horizontalSliderT1.value()
        t2 = self.ui.horizontalSliderT2.value()
        self.sketch_pixmap = self.get_sketch_pixmap(
            self.img_path, (core_X, core_Y), t1, t2)
        self.set_label_image(self.ui.labelImageDst, self.sketch_pixmap)

    @pyqtSlot(int)
    def on_horizontalSliderT1_valueChanged(self, value):
        core_X = self.ui.horizontalSliderConvCoreX.value()
        core_Y = self.ui.horizontalSliderConvCoreY.value()
        t1 = value
        t2 = self.ui.horizontalSliderT2.value()
        self.sketch_pixmap = self.get_sketch_pixmap(
            self.img_path, (core_X, core_Y), t1, t2)
        self.set_label_image(self.ui.labelImageDst, self.sketch_pixmap)

    @pyqtSlot(int)
    def on_horizontalSliderT2_valueChanged(self, value):
        core_X = self.ui.horizontalSliderConvCoreX.value()
        core_Y = self.ui.horizontalSliderConvCoreY.value()
        t1 = self.ui.horizontalSliderT1.value()
        t2 = value
        self.sketch_pixmap = self.get_sketch_pixmap(
            self.img_path, (core_X, core_Y), t1, t2)
        self.set_label_image(self.ui.labelImageDst, self.sketch_pixmap)

    def dragEnterEvent(self, event):
        if (event.mimeData().hasUrls()):
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        if (event.mimeData().hasUrls()):
            event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            urlList = event.mimeData().urls()
            fileInfo = QFileInfo(urlList[0].toLocalFile())
            img_full_path = fileInfo.filePath()
            self.load_transfer_image(img_full_path)
            event.acceptProposedAction()
