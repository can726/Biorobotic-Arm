# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Apr  5 14:14:04 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FaceDetection(object):
    def setupUi(self, FaceDetection):
        FaceDetection.setObjectName("FaceDetection")
        FaceDetection.setEnabled(True)
        FaceDetection.resize(992, 562)
        FaceDetection.setMinimumSize(QtCore.QSize(992, 562))
        FaceDetection.setMaximumSize(QtCore.QSize(16777215, 562))
        self.centralwidget = QtGui.QWidget(FaceDetection)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.video = VideoWidget(self.centralwidget)
        self.video.setMinimumSize(QtCore.QSize(640, 480))
        self.video.setMaximumSize(QtCore.QSize(640, 480))
        self.video.setAutoFillBackground(False)
        self.video.setObjectName("video")
        self.verticalLayout.addWidget(self.video)
        self.horizontal_speed = QtGui.QSlider(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontal_speed.sizePolicy().hasHeightForWidth())
        self.horizontal_speed.setSizePolicy(sizePolicy)
        self.horizontal_speed.setCursor(QtCore.Qt.SizeHorCursor)
        self.horizontal_speed.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.horizontal_speed.setMinimum(-100)
        self.horizontal_speed.setMaximum(100)
        self.horizontal_speed.setPageStep(0)
        self.horizontal_speed.setOrientation(QtCore.Qt.Horizontal)
        self.horizontal_speed.setObjectName("horizontal_speed")
        self.verticalLayout.addWidget(self.horizontal_speed)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.vertical_speed = QtGui.QSlider(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vertical_speed.sizePolicy().hasHeightForWidth())
        self.vertical_speed.setSizePolicy(sizePolicy)
        self.vertical_speed.setCursor(QtCore.Qt.SizeVerCursor)
        self.vertical_speed.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.vertical_speed.setMinimum(-100)
        self.vertical_speed.setMaximum(100)
        self.vertical_speed.setPageStep(0)
        self.vertical_speed.setOrientation(QtCore.Qt.Vertical)
        self.vertical_speed.setObjectName("vertical_speed")
        self.horizontalLayout.addWidget(self.vertical_speed)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.serial_select = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serial_select.sizePolicy().hasHeightForWidth())
        self.serial_select.setSizePolicy(sizePolicy)
        self.serial_select.setCursor(QtCore.Qt.PointingHandCursor)
        self.serial_select.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.serial_select.setObjectName("serial_select")
        self.serial_select.addItem("")
        self.verticalLayout_3.addWidget(self.serial_select)
        self.log = QtGui.QTextEdit(self.groupBox_3)
        self.log.setEnabled(True)
        self.log.setUndoRedoEnabled(True)
        self.log.setReadOnly(True)
        self.log.setObjectName("log")
        self.verticalLayout_3.addWidget(self.log)
        self.command_edit = QtGui.QLineEdit(self.groupBox_3)
        self.command_edit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.command_edit.sizePolicy().hasHeightForWidth())
        self.command_edit.setSizePolicy(sizePolicy)
        self.command_edit.setPlaceholderText("Command")
        self.command_edit.setObjectName("command_edit")
        self.verticalLayout_3.addWidget(self.command_edit)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 184))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.fan_enabled = QtGui.QCheckBox(self.groupBox)
        self.fan_enabled.setCursor(QtCore.Qt.PointingHandCursor)
        self.fan_enabled.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.fan_enabled.setObjectName("fan_enabled")
        self.verticalLayout_6.addWidget(self.fan_enabled)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.speed_dial = QtGui.QDial(self.groupBox)
        self.speed_dial.setCursor(QtCore.Qt.PointingHandCursor)
        self.speed_dial.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.speed_dial.setMaximum(100)
        self.speed_dial.setSliderPosition(80)
        self.speed_dial.setOrientation(QtCore.Qt.Horizontal)
        self.speed_dial.setInvertedAppearance(False)
        self.speed_dial.setInvertedControls(False)
        self.speed_dial.setObjectName("speed_dial")
        self.horizontalLayout_3.addWidget(self.speed_dial)
        self.speed_label = QtGui.QLabel(self.groupBox)
        self.speed_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.speed_label.setObjectName("speed_label")
        self.horizontalLayout_3.addWidget(self.speed_label)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.faces_enabled = QtGui.QCheckBox(self.groupBox_2)
        self.faces_enabled.setCursor(QtCore.Qt.PointingHandCursor)
        self.faces_enabled.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.faces_enabled.setObjectName("faces_enabled")
        self.verticalLayout_4.addWidget(self.faces_enabled)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        FaceDetection.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 992, 22))
        self.menubar.setObjectName("menubar")
        self.menuBioRob_FaceDetection = QtGui.QMenu(self.menubar)
        self.menuBioRob_FaceDetection.setObjectName("menuBioRob_FaceDetection")
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        FaceDetection.setMenuBar(self.menubar)
        self.menuBioRob_FaceDetection.addSeparator()
        self.menubar.addAction(self.menuBioRob_FaceDetection.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(FaceDetection)
        QtCore.QObject.connect(self.faces_enabled, QtCore.SIGNAL("toggled(bool)"), self.horizontal_speed.setDisabled)
        QtCore.QObject.connect(self.faces_enabled, QtCore.SIGNAL("toggled(bool)"), self.vertical_speed.setDisabled)
        QtCore.QObject.connect(self.fan_enabled, QtCore.SIGNAL("toggled(bool)"), self.speed_dial.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(FaceDetection)

    def retranslateUi(self, FaceDetection):
        FaceDetection.setWindowTitle(QtGui.QApplication.translate("FaceDetection", "BioRob FaceDetection", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("FaceDetection", "Connection", None, QtGui.QApplication.UnicodeUTF8))
        self.serial_select.setItemText(0, QtGui.QApplication.translate("FaceDetection", "Not Connected", None, QtGui.QApplication.UnicodeUTF8))
        self.log.setHtml(QtGui.QApplication.translate("FaceDetection", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("FaceDetection", "Fan", None, QtGui.QApplication.UnicodeUTF8))
        self.fan_enabled.setText(QtGui.QApplication.translate("FaceDetection", "Automatic", None, QtGui.QApplication.UnicodeUTF8))
        self.speed_label.setText(QtGui.QApplication.translate("FaceDetection", "80 %", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("FaceDetection", "Movement", None, QtGui.QApplication.UnicodeUTF8))
        self.faces_enabled.setText(QtGui.QApplication.translate("FaceDetection", "Follow faces", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBioRob_FaceDetection.setTitle(QtGui.QApplication.translate("FaceDetection", "BioRob FaceDetection", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("FaceDetection", "About", None, QtGui.QApplication.UnicodeUTF8))

from videowidget import VideoWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FaceDetection = QtGui.QMainWindow()
    ui = Ui_FaceDetection()
    ui.setupUi(FaceDetection)
    FaceDetection.show()
    sys.exit(app.exec_())

