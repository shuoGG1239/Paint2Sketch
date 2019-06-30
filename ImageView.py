import threading

from PyQt5.QtCore import Qt, pyqtSlot, QFileInfo, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QFileDialog
from QCandyUi.CandyWindow import colorful

import Loading
import sketch
from ui_frameimageview import Ui_frameImageView


@colorful('blue')
class ImageView(QWidget):
    signal_sketch_finished = pyqtSignal(list)

    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_frameImageView()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)
        self.img_path = ""
        self.sketch_pixmaps = []
        self.init_slider()
        self.loadingLabel = Loading.Loading(self)
        self.signal_sketch_finished.connect(self.__slot_update_images)

    @pyqtSlot(list)
    def __slot_update_images(self, pixmaps):
        self.sketch_pixmaps = pixmaps
        self.ui.horizontalSlider.setMaximum(len(self.sketch_pixmaps) - 1)
        self.ui.horizontalSlider.setValue(0)
        self.set_label_image(self.ui.labelImageDst, self.sketch_pixmaps[0])
        self.loadingLabel.hide()

    def job_sketch(self, image_url):
        result = []
        try:
            result = self.get_sketch_pixmaps(image_url)
        finally:
            self.signal_sketch_finished.emit(result)

    def run_transform_async(self, image_url):
        self.loadingLabel.show()
        threading.Thread(target=self.job_sketch, args=(image_url,)).start()

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

    def get_sketch_pixmaps(self, image_url):
        """
         获取各种调参得到的线稿图
        :param image_url:
        :return: list of QPixmap
        """
        mats = sketch.transforms(image_url)
        pixmaps = []
        for m in mats:
            height, width = m.shape
            bytes_per_line = width
            q_image = QImage(m.data, width, height,
                             bytes_per_line, QImage.Format_Indexed8)
            pixmaps.append(QPixmap.fromImage(q_image))
        return pixmaps

    def init_slider(self):
        self.ui.horizontalSlider.setMaximum(5)
        self.ui.horizontalSlider.setSingleStep(1)
        self.ui.horizontalSlider.setPageStep(1)

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
        index = self.ui.horizontalSlider.value()
        self.sketch_pixmaps[index].save(file_full_path + '.jpg')

    def load_transfer_image(self, img_url):
        """
        载入加处理加展示图片一条龙
        :param img_url:
        :return:
        """
        self.img_path = img_url
        self.set_label_image(self.ui.labelImageSrc, QPixmap(img_url))
        self.ui.labelImageDst.clear()
        self.run_transform_async(img_url)

    @pyqtSlot(int)
    def on_horizontalSlider_valueChanged(self, value):
        if self.sketch_pixmaps is None or len(self.sketch_pixmaps) == 0:
            return
        self.set_label_image(self.ui.labelImageDst, self.sketch_pixmaps[value])

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
