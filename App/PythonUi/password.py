from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pLoginWindow(object):
    def setup_ui(self, pLoginWindow):
        pLoginWindow.setObjectName("pLoginWindow")
        pLoginWindow.resize(681, 389)
        pLoginWindow.setMinimumSize(QtCore.QSize(681, 389))
        pLoginWindow.setMaximumSize(QtCore.QSize(681, 391))
        pLoginWindow.setSizeIncrement(QtCore.QSize(0, 0))
        pLoginWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pcentralwidget = QtWidgets.QWidget(pLoginWindow)
        self.pcentralwidget.setObjectName("pcentralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.pcentralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pMainFrame = QtWidgets.QFrame(self.pcentralwidget)
        self.pMainFrame.setMinimumSize(QtCore.QSize(661, 371))
        self.pMainFrame.setMaximumSize(QtCore.QSize(661, 371))
        self.pMainFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pMainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pMainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pMainFrame.setObjectName("pMainFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.pMainFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pInnerFrame = QtWidgets.QFrame(self.pMainFrame)
        self.pInnerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pInnerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pInnerFrame.setObjectName("pInnerFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.pInnerFrame)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.pInnerVerticalLayout = QtWidgets.QVBoxLayout()
        self.pInnerVerticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.pInnerVerticalLayout.setSpacing(0)
        self.pInnerVerticalLayout.setObjectName("pInnerVerticalLayout")
        self.pImageHorizontalLayout = QtWidgets.QHBoxLayout()
        self.pImageHorizontalLayout.setObjectName("pImageHorizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(215, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.pImageHorizontalLayout.addItem(spacerItem1)
        self.pImgLabel = QtWidgets.QLabel(self.pInnerFrame)
        self.pImgLabel.setText("")
        self.pImgLabel.setPixmap(QtGui.QPixmap("../../images/login_image.png"))
        self.pImgLabel.setObjectName("pImgLabel")
        self.pImageHorizontalLayout.addWidget(self.pImgLabel)
        spacerItem2 = QtWidgets.QSpacerItem(210, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.pImageHorizontalLayout.addItem(spacerItem2)
        self.pInnerVerticalLayout.addLayout(self.pImageHorizontalLayout)
        self.pPasswordHorizontalLayout = QtWidgets.QHBoxLayout()
        self.pPasswordHorizontalLayout.setSpacing(0)
        self.pPasswordHorizontalLayout.setObjectName("pPasswordHorizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(190, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.pPasswordHorizontalLayout.addItem(spacerItem3)
        self.pPasswordLineEdit = QtWidgets.QLineEdit(self.pInnerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pPasswordLineEdit.sizePolicy().hasHeightForWidth())
        self.pPasswordLineEdit.setSizePolicy(sizePolicy)
        self.pPasswordLineEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pPasswordLineEdit.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pPasswordLineEdit.setFont(font)
        self.pPasswordLineEdit.setStyleSheet("border: 2px solid gray;\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "background-color: rgb(203, 203, 203);\n"
                                             "border-color: rgb(203, 203, 203);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border-radius: 8px;\n"
                                             "")
        self.pPasswordLineEdit.setText("")
        self.pPasswordLineEdit.setObjectName("pPasswordLineEdit")
        self.pPasswordHorizontalLayout.addWidget(self.pPasswordLineEdit)
        self.pArrowLlabel = QtWidgets.QLabel(self.pInnerFrame)
        self.pArrowLlabel.setText("")
        self.pArrowLlabel.setPixmap(QtGui.QPixmap("../../images/enter_arrow.png"))
        self.pArrowLlabel.setObjectName("pArrowLlabel")
        self.pPasswordHorizontalLayout.addWidget(self.pArrowLlabel)
        spacerItem4 = QtWidgets.QSpacerItem(180, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.pPasswordHorizontalLayout.addItem(spacerItem4)
        self.pInnerVerticalLayout.addLayout(self.pPasswordHorizontalLayout)
        self.pForgotHorizontalLayout = QtWidgets.QHBoxLayout()
        self.pForgotHorizontalLayout.setObjectName("pForgotHorizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.pForgotHorizontalLayout.addItem(spacerItem5)
        self.pForgotPasswordLabel = QtWidgets.QLabel(self.pInnerFrame)
        self.pForgotPasswordLabel.setObjectName("pForgotPasswordLabel")
        self.pForgotHorizontalLayout.addWidget(self.pForgotPasswordLabel)
        spacerItem6 = QtWidgets.QSpacerItem(240, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.pForgotHorizontalLayout.addItem(spacerItem6)
        self.pInnerVerticalLayout.addLayout(self.pForgotHorizontalLayout)
        self.gridLayout.addLayout(self.pInnerVerticalLayout, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.pInnerFrame, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(350, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem7, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.pMainFrame, 0, 0, 1, 1)
        pLoginWindow.setCentralWidget(self.pcentralwidget)
        self.actionChange_password = QtWidgets.QAction(pLoginWindow)
        self.actionChange_password.setObjectName("actionChange_password")

        self.retranslateUi(pLoginWindow)
        QtCore.QMetaObject.connectSlotsByName(pLoginWindow)

    def retranslateUi(self, pLoginWindow):
        _translate = QtCore.QCoreApplication.translate
        pLoginWindow.setWindowTitle(_translate("pLoginWindow", "Login"))
        self.pPasswordLineEdit.setToolTip(_translate("pLoginWindow", "Enter Password"))
        self.pArrowLlabel.setToolTip(_translate("pLoginWindow", "Enter"))
        self.pForgotPasswordLabel.setToolTip(_translate("pLoginWindow", "Rest Password"))
        self.pForgotPasswordLabel.setText(_translate("pLoginWindow", "Forgot Password?"))
        self.actionChange_password.setText(_translate("pLoginWindow", "Change password"))
