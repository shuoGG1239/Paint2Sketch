# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_frameimageview.ui'
#
# Created: Thu Jun 27 21:41:17 2019
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frameImageView(object):
    def setupUi(self, frameImageView):
        frameImageView.setObjectName("frameImageView")
        frameImageView.resize(753, 440)
        self.horizontalLayout = QtWidgets.QHBoxLayout(frameImageView)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelImageDst = QtWidgets.QLabel(frameImageView)
        self.labelImageDst.setFrameShape(QtWidgets.QFrame.Box)
        self.labelImageDst.setText("")
        self.labelImageDst.setObjectName("labelImageDst")
        self.horizontalLayout.addWidget(self.labelImageDst)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelImageSrc = QtWidgets.QLabel(frameImageView)
        self.labelImageSrc.setFrameShape(QtWidgets.QFrame.Box)
        self.labelImageSrc.setText("")
        self.labelImageSrc.setObjectName("labelImageSrc")
        self.verticalLayout.addWidget(self.labelImageSrc)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonOpen = QtWidgets.QPushButton(frameImageView)
        self.pushButtonOpen.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButtonOpen.setObjectName("pushButtonOpen")
        self.horizontalLayout_2.addWidget(self.pushButtonOpen)
        self.pushButtonSave = QtWidgets.QPushButton(frameImageView)
        self.pushButtonSave.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout_2.addWidget(self.pushButtonSave)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalSlider = QtWidgets.QSlider(frameImageView)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(frameImageView)
        QtCore.QMetaObject.connectSlotsByName(frameImageView)

    def retranslateUi(self, frameImageView):
        _translate = QtCore.QCoreApplication.translate
        frameImageView.setWindowTitle(_translate("frameImageView", "Form"))
        self.pushButtonOpen.setText(_translate("frameImageView", "Open"))
        self.pushButtonSave.setText(_translate("frameImageView", "Save"))

