# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_frameimageview.ui'
#
# Created: Sat Mar 10 21:26:25 2018
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frameImageView(object):
    def setupUi(self, frameImageView):
        frameImageView.setObjectName("frameImageView")
        frameImageView.resize(745, 537)
        self.labelImage = QtWidgets.QLabel(frameImageView)
        self.labelImage.setGeometry(QtCore.QRect(50, 40, 621, 431))
        self.labelImage.setObjectName("labelImage")

        self.retranslateUi(frameImageView)
        QtCore.QMetaObject.connectSlotsByName(frameImageView)

    def retranslateUi(self, frameImageView):
        _translate = QtCore.QCoreApplication.translate
        frameImageView.setWindowTitle(_translate("frameImageView", "Form"))
        self.labelImage.setText(_translate("frameImageView", "TextLabel"))

