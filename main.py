import ImageView
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from qss_ui_theme import qss_setting
from qss_ui_theme import green_theme
from qss_ui_theme import window_titlebar

WINDOW_TITLE = 'Paint2Sketch'


def run_with_titlebar():
    app = QApplication(sys.argv)
    imgeFrame = ImageView.ImageView()
    mainWindow = window_titlebar.WindowWithTitleBar(imgeFrame, qss_setting.DARKBLUEGREEN, 0)
    mainWindow.setWindowTitle(WINDOW_TITLE)
    mainWindow.setWindowIcon(QIcon(window_titlebar.imageroot + 'myicon.ico'))
    green_theme.setAppGreenStyle()
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run_with_titlebar()
