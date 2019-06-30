from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget, QLabel


class Loading(QLabel):
    def __init__(self, parent, gif_path='./asset/loading.gif'):
        QWidget.__init__(self, parent)
        self.init_loading_gif(gif_path)

    def init_loading_gif(self, gif_path):
        """
        初始化loading动画
        :return:
        """
        gif = QMovie(gif_path)
        gif.start()
        parent = self.parent()
        if parent:
            x, y = (parent.width() / 2) - 24, (parent.height() / 2) - 24
        else:
            x, y = 0, 0
        self.setMovie(gif)
        self.adjustSize()
        self.setGeometry(x, y, self.width(), self.height())
        self.setVisible(False)

    def show(self):
        parent = self.parent()
        if parent:
            x, y = (parent.width() / 2) - 24, (parent.height() / 2) - 24
        else:
            x, y = 0, 0
        self.setGeometry(x, y, self.width(), self.height())
        super().show()

    def hide(self):
        super().hide()
