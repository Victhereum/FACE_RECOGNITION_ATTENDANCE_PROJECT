# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FRASGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.camera_frame = QtWidgets.QFrame(self.centralwidget)
        self.camera_frame.setGeometry(QtCore.QRect(-1, -1, 801, 431))
        self.camera_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.camera_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.camera_frame.setObjectName("camera_frame")
        self.status_frame = QtWidgets.QFrame(self.centralwidget)
        self.status_frame.setGeometry(QtCore.QRect(-1, 439, 801, 121))
        self.status_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.status_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.status_frame.setObjectName("status_frame")
        self.on_application = QtWidgets.QPushButton(self.status_frame)
        self.on_application.setGeometry(QtCore.QRect(20, 20, 41, 23))
        self.on_application.setObjectName("on_application")
        self.off_application = QtWidgets.QPushButton(self.status_frame)
        self.off_application.setGeometry(QtCore.QRect(70, 20, 41, 23))
        self.off_application.setObjectName("off_application")
        self.name = QtWidgets.QLabel(self.status_frame)
        self.name.setGeometry(QtCore.QRect(20, 90, 301, 16))
        self.name.setObjectName("name")
        self.timestamp = QtWidgets.QLabel(self.status_frame)
        self.timestamp.setGeometry(QtCore.QRect(420, 90, 301, 16))
        self.timestamp.setObjectName("timestamp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuCamera = QtWidgets.QMenu(self.menubar)
        self.menuCamera.setObjectName("menuCamera")
        MainWindow.setMenuBar(self.menubar)
        self.actionRegister = QtWidgets.QAction(MainWindow)
        self.actionRegister.setObjectName("actionRegister")
        self.actionImport_Image = QtWidgets.QAction(MainWindow)
        self.actionImport_Image.setObjectName("actionImport_Image")
        self.actionSystem_WebCam = QtWidgets.QAction(MainWindow)
        self.actionSystem_WebCam.setObjectName("actionSystem_WebCam")
        self.actionExternal_WebCam = QtWidgets.QAction(MainWindow)
        self.actionExternal_WebCam.setObjectName("actionExternal_WebCam")
        self.actionCCTV = QtWidgets.QAction(MainWindow)
        self.actionCCTV.setObjectName("actionCCTV")
        self.actionOthers = QtWidgets.QAction(MainWindow)
        self.actionOthers.setObjectName("actionOthers")
        self.menuFile.addAction(self.actionRegister)
        self.menuFile.addAction(self.actionImport_Image)
        self.menuCamera.addAction(self.actionSystem_WebCam)
        self.menuCamera.addAction(self.actionExternal_WebCam)
        self.menuCamera.addAction(self.actionCCTV)
        self.menuCamera.addAction(self.actionOthers)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCamera.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.on_application.setText(_translate("MainWindow", "ON"))
        self.off_application.setText(_translate("MainWindow", "OFF"))
        self.name.setText(_translate("MainWindow", "Name:"))
        self.timestamp.setText(_translate("MainWindow", "Time Stamp:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuCamera.setTitle(_translate("MainWindow", "Camera"))
        self.actionRegister.setText(_translate("MainWindow", "Register"))
        self.actionImport_Image.setText(_translate("MainWindow", "Import Image"))
        self.actionSystem_WebCam.setText(_translate("MainWindow", "System WebCam"))
        self.actionExternal_WebCam.setText(_translate("MainWindow", "External WebCam"))
        self.actionCCTV.setText(_translate("MainWindow", "CCTV"))
        self.actionOthers.setText(_translate("MainWindow", "Others"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
