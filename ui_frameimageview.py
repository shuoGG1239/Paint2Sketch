# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_frameimageview.ui'
#
# Created: Tue Apr  3 09:03:20 2018
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frameImageView(object):
    def setupUi(self, frameImageView):
        frameImageView.setObjectName("frameImageView")
        frameImageView.resize(688, 422)
        self.labelImageDst = QtWidgets.QLabel(frameImageView)
        self.labelImageDst.setGeometry(QtCore.QRect(10, 10, 461, 391))
        self.labelImageDst.setObjectName("labelImageDst")
        self.horizontalSliderConvCoreX = QtWidgets.QSlider(frameImageView)
        self.horizontalSliderConvCoreX.setGeometry(QtCore.QRect(495, 270, 160, 19))
        self.horizontalSliderConvCoreX.setMaximum(10)
        self.horizontalSliderConvCoreX.setPageStep(1)
        self.horizontalSliderConvCoreX.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderConvCoreX.setObjectName("horizontalSliderConvCoreX")
        self.labelImageSrc = QtWidgets.QLabel(frameImageView)
        self.labelImageSrc.setGeometry(QtCore.QRect(485, 10, 181, 171))
        self.labelImageSrc.setObjectName("labelImageSrc")
        self.pushButtonOpen = QtWidgets.QPushButton(frameImageView)
        self.pushButtonOpen.setGeometry(QtCore.QRect(485, 210, 88, 41))
        self.pushButtonOpen.setObjectName("pushButtonOpen")
        self.horizontalSliderConvCoreY = QtWidgets.QSlider(frameImageView)
        self.horizontalSliderConvCoreY.setGeometry(QtCore.QRect(495, 308, 160, 19))
        self.horizontalSliderConvCoreY.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderConvCoreY.setObjectName("horizontalSliderConvCoreY")
        self.horizontalSliderT1 = QtWidgets.QSlider(frameImageView)
        self.horizontalSliderT1.setGeometry(QtCore.QRect(495, 345, 160, 19))
        self.horizontalSliderT1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderT1.setObjectName("horizontalSliderT1")
        self.horizontalSliderT2 = QtWidgets.QSlider(frameImageView)
        self.horizontalSliderT2.setGeometry(QtCore.QRect(495, 380, 160, 19))
        self.horizontalSliderT2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderT2.setObjectName("horizontalSliderT2")
        self.pushButtonSave = QtWidgets.QPushButton(frameImageView)
        self.pushButtonSave.setGeometry(QtCore.QRect(577, 210, 88, 41))
        self.pushButtonSave.setObjectName("pushButtonSave")

        self.retranslateUi(frameImageView)
        QtCore.QMetaObject.connectSlotsByName(frameImageView)

    def retranslateUi(self, frameImageView):
        _translate = QtCore.QCoreApplication.translate
        frameImageView.setWindowTitle(_translate("frameImageView", "Form"))
        self.labelImageDst.setText(_translate("frameImageView", "LabelImageDst"))
        self.labelImageSrc.setText(_translate("frameImageView", "LabelImageSrc"))
        self.pushButtonOpen.setText(_translate("frameImageView", "Open"))
        self.pushButtonSave.setText(_translate("frameImageView", "Save"))

