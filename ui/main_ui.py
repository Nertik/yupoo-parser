# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(508, 322)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(17)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.link_field = QLineEdit(self.centralwidget)
        self.link_field.setObjectName(u"link_field")
        font1 = QFont()
        font1.setPointSize(14)
        self.link_field.setFont(font1)
        self.link_field.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.link_field, 0, 1, 1, 2)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 255, 126))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.section_layout = QVBoxLayout()
        self.section_layout.setObjectName(u"section_layout")

        self.horizontalLayout.addLayout(self.section_layout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 2, 2)

        self.fast_loading_checkbox = QCheckBox(self.centralwidget)
        self.fast_loading_checkbox.setObjectName(u"fast_loading_checkbox")
        self.fast_loading_checkbox.setEnabled(True)
        sizePolicy.setHeightForWidth(self.fast_loading_checkbox.sizePolicy().hasHeightForWidth())
        self.fast_loading_checkbox.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(15)
        self.fast_loading_checkbox.setFont(font2)
        self.fast_loading_checkbox.setAcceptDrops(False)
        self.fast_loading_checkbox.setLayoutDirection(Qt.LeftToRight)
        self.fast_loading_checkbox.setAutoFillBackground(False)
        self.fast_loading_checkbox.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 18px;\n"
"	height: 18px;\n"
"}\n"
"QCheckBox {\n"
"	margin-left: 10px;\n"
"	spacing: 15px;\n"
"}")
        self.fast_loading_checkbox.setAutoRepeat(False)

        self.gridLayout.addWidget(self.fast_loading_checkbox, 1, 2, 1, 1)

        self.open_folder_button = QPushButton(self.centralwidget)
        self.open_folder_button.setObjectName(u"open_folder_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.open_folder_button.sizePolicy().hasHeightForWidth())
        self.open_folder_button.setSizePolicy(sizePolicy1)
        self.open_folder_button.setMinimumSize(QSize(0, 50))
        self.open_folder_button.setMaximumSize(QSize(16777215, 50))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        self.open_folder_button.setFont(font3)

        self.gridLayout.addWidget(self.open_folder_button, 2, 2, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        font4 = QFont()
        font4.setBold(False)
        self.line.setFont(font4)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 3)

        self.update_section_list_btn = QPushButton(self.centralwidget)
        self.update_section_list_btn.setObjectName(u"update_section_list_btn")
        self.update_section_list_btn.setMinimumSize(QSize(0, 50))
        self.update_section_list_btn.setMaximumSize(QSize(16777215, 50))
        self.update_section_list_btn.setFont(font2)

        self.gridLayout.addWidget(self.update_section_list_btn, 4, 0, 1, 3)

        self.start_parsing_btn = QPushButton(self.centralwidget)
        self.start_parsing_btn.setObjectName(u"start_parsing_btn")
        sizePolicy1.setHeightForWidth(self.start_parsing_btn.sizePolicy().hasHeightForWidth())
        self.start_parsing_btn.setSizePolicy(sizePolicy1)
        self.start_parsing_btn.setMinimumSize(QSize(0, 50))
        self.start_parsing_btn.setMaximumSize(QSize(16777215, 50))
        self.start_parsing_btn.setFont(font2)

        self.gridLayout.addWidget(self.start_parsing_btn, 5, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Link", None))
        self.link_field.setText("")
        self.fast_loading_checkbox.setText(QCoreApplication.translate("MainWindow", u"Fast image loading\n"
"(some images may\n"
"not load completely)", None))
        self.open_folder_button.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
        self.update_section_list_btn.setText(QCoreApplication.translate("MainWindow", u"Update section list", None))
        self.start_parsing_btn.setText(QCoreApplication.translate("MainWindow", u"Start parsing", None))
    # retranslateUi

