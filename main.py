import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

import ImageView

WINDOW_TITLE = 'Paint2Sketch'


def run_with_titlebar():
    app = QApplication(sys.argv)
    imgeFrame = ImageView.ImageView()
    imgeFrame.setWindowTitle(WINDOW_TITLE)
    imgeFrame.setWindowIcon(QIcon('myicon.ico'))
    imgeFrame.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run_with_titlebar()
