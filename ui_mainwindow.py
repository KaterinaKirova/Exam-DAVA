# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'win.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT \
    as NavigationToolbar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 920)
        MainWindow.setMinimumSize(QSize(100, 100))
        MainWindow.setMaximumSize(QSize(2000, 1900))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.frame_7)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(400, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(380, 20))
        self.frame.setMaximumSize(QSize(20, 110))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.groupBox_period = QGroupBox(self.frame)
        self.groupBox_period.setObjectName(u"groupBox_period")
        self.groupBox_period.setMinimumSize(QSize(20, 20))
        self.groupBox_period.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setPointSize(10)
        self.groupBox_period.setFont(font)
        self.formLayout = QFormLayout(self.groupBox_period)
        self.formLayout.setObjectName(u"formLayout")
        self.label_from = QLabel(self.groupBox_period)
        self.label_from.setObjectName(u"label_from")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_from)

        self.dateEdit_from = QDateEdit(self.groupBox_period)
        self.dateEdit_from.setObjectName(u"dateEdit_from")
        self.dateEdit_from.setDateTime(QDateTime(QDate(2014, 1, 1), QTime(18, 0, 0)))
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dateEdit_from)

        self.label_to = QLabel(self.groupBox_period)
        self.label_to.setObjectName(u"label_to")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_to)

        self.dateEdit_to = QDateEdit(self.groupBox_period)
        self.dateEdit_to.setObjectName(u"dateEdit_to")
        self.dateEdit_to.setDateTime(QDateTime(QDate().currentDate(), QTime(19, 0, 0)))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dateEdit_to)


        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.groupBox_period)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 200))
        self.frame_3.setMaximumSize(QSize(16777215, 270))
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_selec_camera = QGroupBox(self.frame_3)
        self.groupBox_selec_camera.setObjectName(u"groupBox_selec_camera")
        self.groupBox_selec_camera.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_selec_camera)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.comboBox_camera = QComboBox(self.groupBox_selec_camera)
        self.comboBox_camera.addItem("")
        self.comboBox_camera.addItem("")
        self.comboBox_camera.addItem("")
        self.comboBox_camera.addItem("")
        self.comboBox_camera.addItem("")
        self.comboBox_camera.addItem("")
        self.comboBox_camera.addItem("")
        self.comboBox_camera.addItem("")
        self.comboBox_camera.addItem("")
        self.comboBox_camera.addItem("")
        self.comboBox_camera.addItem("")
        self.comboBox_camera.setObjectName(u"comboBox_camera")

        self.verticalLayout_3.addWidget(self.comboBox_camera)


        self.verticalLayout.addWidget(self.groupBox_selec_camera)

        self.groupBox_options = QGroupBox(self.frame_3)
        self.groupBox_options.setObjectName(u"groupBox_options")
        self.groupBox_options.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_options)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBox_options = QComboBox(self.groupBox_options)
        self.comboBox_options.addItem("")
        self.comboBox_options.setObjectName(u"comboBox_options")

        self.verticalLayout_4.addWidget(self.comboBox_options)


        self.verticalLayout.addWidget(self.groupBox_options)

        self.groupBox_select_method = QGroupBox(self.frame_3)
        self.groupBox_select_method.setObjectName(u"groupBox_select_method")
        self.groupBox_select_method.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_select_method)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.comboBox_method = QComboBox(self.groupBox_select_method)
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.comboBox_method.setObjectName(u"comboBox_method")

        self.verticalLayout_5.addWidget(self.comboBox_method)


        self.verticalLayout.addWidget(self.groupBox_select_method)

        self.groupBox_select_type = QGroupBox(self.frame_3)
        self.groupBox_select_type.setObjectName(u"groupBox_select_type")
        self.groupBox_select_type.setFont(font)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_select_type)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.comboBox_type = QComboBox(self.groupBox_select_type)
        self.comboBox_type.setObjectName(u"comboBox_type")

        self.verticalLayout_6.addWidget(self.comboBox_type)


        self.verticalLayout.addWidget(self.groupBox_select_type)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(400, 45))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_Export = QPushButton(self.frame_6)
        self.pushButton_Export.setObjectName(u"pushButton_Export")
        self.pushButton_Export.setFont(font)

        self.gridLayout.addWidget(self.pushButton_Export, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 150))
        self.frame_4.setMaximumSize(QSize(400, 700))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_about = QGroupBox(self.frame_4)
        self.groupBox_about.setObjectName(u"groupBox_about")
        self.groupBox_about.setFont(font)
        self.label_info = QLabel(self.groupBox_about)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setGeometry(QRect(0, 20, 181, 141))
        self.label_info.setFont(font)

        self.horizontalLayout_4.addWidget(self.groupBox_about)

        self.groupBox_about_3 = QGroupBox(self.frame_4)
        self.groupBox_about_3.setObjectName(u"groupBox_about_3")
        self.groupBox_about_3.setFont(font)
        self.label_label_info_result = QLabel(self.groupBox_about_3)
        self.label_label_info_result.setObjectName(u"label_label_info_result")
        self.label_label_info_result.setGeometry(QRect(10, 10, 171, 151))
        self.label_label_info_result.setFont(font)

        self.horizontalLayout_4.addWidget(self.groupBox_about_3)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 90))
        self.frame_5.setMaximumSize(QSize(16777215, 400))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.groupBox_about_2 = QGroupBox(self.frame_5)
        self.groupBox_about_2.setObjectName(u"groupBox_about_2")
        self.groupBox_about_2.setGeometry(QRect(10, 0, 361, 171))
        self.groupBox_about_2.setFont(font)
        self.label_info_option = QLabel(self.groupBox_about_2)
        self.label_info_option.setObjectName(u"label_info_option")
        self.label_info_option.setGeometry(QRect(10, 10, 351, 161))
        self.label_info_option.setFont(font)

        self.verticalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.horizontalLayout_2.addWidget(self.frame_8)


        self.horizontalLayout.addWidget(self.frame_7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1324, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas)
        self.verticalLayout_7.addWidget(self.toolbar)
        self.verticalLayout_7.addWidget(self.canvas)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.frame_7.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.groupBox_period.setTitle(QCoreApplication.translate("MainWindow", u"Please select a period of time:", None))
        self.label_from.setText(QCoreApplication.translate("MainWindow", u"from:", None))
#if QT_CONFIG(tooltip)
        self.dateEdit_from.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select the date from which the results will be displayed</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_to.setText(QCoreApplication.translate("MainWindow", u"to:", None))
#if QT_CONFIG(tooltip)
        self.dateEdit_to.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select the date until the results will be displayed</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_selec_camera.setTitle(QCoreApplication.translate("MainWindow", u"Please select a camera: ", None))
        self.comboBox_camera.setItemText(0, "")
        self.comboBox_camera.setItemText(1, QCoreApplication.translate("MainWindow", u"3DPIXA_FinalTest", None))
        self.comboBox_camera.setItemText(2, QCoreApplication.translate("MainWindow", u"allPIXAevo_FinalTest", None))
        self.comboBox_camera.setItemText(3, QCoreApplication.translate("MainWindow", u"allPIXApro_FinalTest", None))
        self.comboBox_camera.setItemText(4, QCoreApplication.translate("MainWindow", u"allPIXAwave_FinalTest", None))
        self.comboBox_camera.setItemText(5, QCoreApplication.translate("MainWindow", u"allPIXA_FinalTest", None))
        self.comboBox_camera.setItemText(6, QCoreApplication.translate("MainWindow", u"Niagara_FinalTest", None))
        self.comboBox_camera.setItemText(7, QCoreApplication.translate("MainWindow", u"P22_FinalTest", None))
        self.comboBox_camera.setItemText(8, QCoreApplication.translate("MainWindow", u"PIXAswir_FinalTest", None))
        self.comboBox_camera.setItemText(9, QCoreApplication.translate("MainWindow", u"SIS_NG_FinalTest", None))
        self.comboBox_camera.setItemText(10, QCoreApplication.translate("MainWindow", u"truePIXA_FinalTest", None))

#if QT_CONFIG(tooltip)
        self.comboBox_camera.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select a camera</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_options.setTitle(QCoreApplication.translate("MainWindow", u"Please select a option:", None))
        self.comboBox_options.setItemText(0, "")

#if QT_CONFIG(tooltip)
        self.comboBox_options.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select a option</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_select_method.setTitle(QCoreApplication.translate("MainWindow", u"Please select a method: ", None))
        self.comboBox_method.setItemText(0, "")
        self.comboBox_method.setItemText(1, QCoreApplication.translate("MainWindow", u"All results sorted by time", None))
        self.comboBox_method.setItemText(2, QCoreApplication.translate("MainWindow", u"Average for each type", None))
        self.comboBox_method.setItemText(3, QCoreApplication.translate("MainWindow", u"Choose which camera type to show", None))

#if QT_CONFIG(tooltip)
        self.comboBox_method.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select a method to display the data:</p><p>1) All results sorted by time - displays a line chart of all results in the above time period</p><p>2) Average for each type - shows a bar chart of the minimum, average and maximum value of each individual type. </p><p>3) Choose which camera type to show - displays a line chart of only the specified type. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_select_type.setTitle(QCoreApplication.translate("MainWindow", u"Please select a camera type:", None))
#if QT_CONFIG(tooltip)
        self.comboBox_type.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select camera type</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Show the result</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
#if QT_CONFIG(tooltip)
        self.pushButton_Export.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0415xport the results in CSV format</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_Export.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.groupBox_about.setTitle(QCoreApplication.translate("MainWindow", u"About the camera:", None))
#if QT_CONFIG(tooltip)
        self.label_info.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Displays information from the selected camera</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_info.setText("")
        self.groupBox_about_3.setTitle(QCoreApplication.translate("MainWindow", u"Test Results:", None))
#if QT_CONFIG(tooltip)
        self.label_label_info_result.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Displays information about test results. How many accepted, passed and failed tests the camera has. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_label_info_result.setText("")
        self.groupBox_about_2.setTitle(QCoreApplication.translate("MainWindow", u"Option:", None))
#if QT_CONFIG(tooltip)
        self.label_info_option.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Displays information from the selected option</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_info_option.setText("")
    # retranslateUi

