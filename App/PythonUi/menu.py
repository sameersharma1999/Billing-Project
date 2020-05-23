from PyQt5 import QtCore, QtGui, QtWidgets


class UiMwMainWindow(object):
    def setup_main_window(self, mwMainWindow):
        mwMainWindow.setObjectName("mwMainWindow")
        mwMainWindow.resize(852, 900)
        mwMainWindow.setMinimumSize(QtCore.QSize(852, 900))
        mwMainWindow.setMaximumSize(QtCore.QSize(852, 900))
        mwMainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mwcentralwidget = QtWidgets.QWidget(mwMainWindow)
        self.mwcentralwidget.setObjectName("mwcentralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.mwcentralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mwOuterFrame = QtWidgets.QFrame(self.mwcentralwidget)
        self.mwOuterFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mwOuterFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mwOuterFrame.setObjectName("mwOuterFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.mwOuterFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.mwInnerFrame = QtWidgets.QFrame(self.mwOuterFrame)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mwInnerFrame.sizePolicy().hasHeightForWidth())
        self.mwInnerFrame.setSizePolicy(sizePolicy)
        self.mwInnerFrame.setMinimumSize(QtCore.QSize(0, 665))
        self.mwInnerFrame.setMaximumSize(QtCore.QSize(1000, 1000))
        self.mwInnerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mwInnerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mwInnerFrame.setObjectName("mwInnerFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.mwInnerFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mwVerticalLayout = QtWidgets.QVBoxLayout()
        self.mwVerticalLayout.setObjectName("mwVerticalLayout")
        self.mwHorizontalLayout = QtWidgets.QHBoxLayout()
        self.mwHorizontalLayout.setObjectName("mwHorizontalLayout")
        self.mwAddCustomelrLabel = QtWidgets.QLabel(self.mwInnerFrame)
        self.mwAddCustomelrLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mwAddCustomelrLabel.setText("")
        self.mwAddCustomelrLabel.setPixmap(QtGui.QPixmap("../../images/add_customer.png"))
        self.mwAddCustomelrLabel.setObjectName("mwAddCustomelrLabel")
        self.mwHorizontalLayout.addWidget(self.mwAddCustomelrLabel)
        self.mwAddItemLabel = QtWidgets.QLabel(self.mwInnerFrame)
        self.mwAddItemLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mwAddItemLabel.setText("")
        self.mwAddItemLabel.setPixmap(QtGui.QPixmap("../../images/add_item.png"))
        self.mwAddItemLabel.setObjectName("mwAddItemLabel")
        self.mwHorizontalLayout.addWidget(self.mwAddItemLabel)
        self.mwInvoiceLabel = QtWidgets.QLabel(self.mwInnerFrame)
        self.mwInvoiceLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mwInvoiceLabel.setText("")
        self.mwInvoiceLabel.setPixmap(QtGui.QPixmap("../../images/invoice.png"))
        self.mwInvoiceLabel.setObjectName("mwInvoiceLabel")
        self.mwHorizontalLayout.addWidget(self.mwInvoiceLabel)
        self.mwVerticalLayout.addLayout(self.mwHorizontalLayout)
        self.mwHoriaontalLayout2 = QtWidgets.QHBoxLayout()
        self.mwHoriaontalLayout2.setObjectName("mwHoriaontalLayout2")
        self.mwEditCustomerLabel = QtWidgets.QLabel(self.mwInnerFrame)
        self.mwEditCustomerLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mwEditCustomerLabel.setText("")
        self.mwEditCustomerLabel.setPixmap(QtGui.QPixmap("../../images/edit_customer.png"))
        self.mwEditCustomerLabel.setObjectName("mwEditCustomerLabel")
        self.mwHoriaontalLayout2.addWidget(self.mwEditCustomerLabel)
        self.mwEditItemLabel = QtWidgets.QLabel(self.mwInnerFrame)
        self.mwEditItemLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mwEditItemLabel.setText("")
        self.mwEditItemLabel.setPixmap(QtGui.QPixmap("../../images/edit_item.png"))
        self.mwEditItemLabel.setObjectName("mwEditItemLabel")
        self.mwHoriaontalLayout2.addWidget(self.mwEditItemLabel)
        self.mmLockLabel = QtWidgets.QLabel(self.mwInnerFrame)
        self.mmLockLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mmLockLabel.setText("")
        self.mmLockLabel.setPixmap(QtGui.QPixmap("../../images/lock.png"))
        self.mmLockLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mmLockLabel.setObjectName("mmLockLabel")
        self.mwHoriaontalLayout2.addWidget(self.mmLockLabel)
        self.mwVerticalLayout.addLayout(self.mwHoriaontalLayout2)
        self.mwHoriaontalLayout3 = QtWidgets.QHBoxLayout()
        self.mwHoriaontalLayout3.setObjectName("mwHoriaontalLayout3")
        self.mmCustomerLabel = QtWidgets.QLabel(self.mwInnerFrame)
        self.mmCustomerLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mmCustomerLabel.setText("")
        self.mmCustomerLabel.setPixmap(QtGui.QPixmap("../../images/CustomerDB.png"))
        self.mmCustomerLabel.setObjectName("mmCustomerLabel")
        self.mwHoriaontalLayout3.addWidget(self.mmCustomerLabel)
        self.mmItemLabel = QtWidgets.QLabel(self.mwInnerFrame)
        self.mmItemLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mmItemLabel.setText("")
        self.mmItemLabel.setPixmap(QtGui.QPixmap("../../images/ItemDB.png"))
        self.mmItemLabel.setObjectName("mmItemLabel")
        self.mwHoriaontalLayout3.addWidget(self.mmItemLabel)
        self.label_6 = QtWidgets.QLabel(self.mwInnerFrame)
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../../images/graph.png"))
        self.label_6.setObjectName("label_6")
        self.mwHoriaontalLayout3.addWidget(self.label_6)
        self.mwVerticalLayout.addLayout(self.mwHoriaontalLayout3)
        self.gridLayout_3.addLayout(self.mwVerticalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.mwInnerFrame, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.mwOuterFrame, 0, 0, 1, 1)
        mwMainWindow.setCentralWidget(self.mwcentralwidget)

        self.retranslateUi(mwMainWindow)
        QtCore.QMetaObject.connectSlotsByName(mwMainWindow)

    def retranslateUi(self, mwMainWindow):
        _translate = QtCore.QCoreApplication.translate
        mwMainWindow.setWindowTitle(_translate("mwMainWindow", "MainWindow"))
        self.mwAddCustomelrLabel.setToolTip(_translate("mwMainWindow", "Add Customer"))
        self.mwAddItemLabel.setToolTip(_translate("mwMainWindow", "Add Item"))
        self.mwInvoiceLabel.setToolTip(_translate("mwMainWindow", "Invoice Generate"))
        self.mwEditCustomerLabel.setToolTip(_translate("mwMainWindow", "Edit Customer"))
        self.mwEditItemLabel.setToolTip(_translate("mwMainWindow", "Edit Item"))
        self.mmLockLabel.setToolTip(_translate("mwMainWindow", "Change Password"))
        self.mmLockLabel.setStatusTip(_translate("mwMainWindow", "Change password"))
        self.mmCustomerLabel.setToolTip(_translate("mwMainWindow", "View all customers"))
        self.mmCustomerLabel.setStatusTip(_translate("mwMainWindow", "Customer data"))
        self.mmItemLabel.setToolTip(_translate("mwMainWindow", "View all Items"))
        self.mmItemLabel.setStatusTip(_translate("mwMainWindow", "All items"))
        self.label_6.setToolTip(_translate("mwMainWindow", "Sales Graph\'s"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     mwMainWindow = QtWidgets.QMainWindow()
#     ui = Ui_mwMainWindow()
#     ui.setupUi(mwMainWindow)
#     mwMainWindow.show()
#     sys.exit(app.exec_())