# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QProgressBar, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(461, 421)
        Form.setFocusPolicy(Qt.TabFocus)
        self.start_parsing_btn = QPushButton(Form)
        self.start_parsing_btn.setObjectName(u"start_parsing_btn")
        self.start_parsing_btn.setGeometry(QRect(10, 360, 441, 51))
        font = QFont()
        font.setPointSize(15)
        self.start_parsing_btn.setFont(font)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 51, 21))
        font1 = QFont()
        font1.setPointSize(17)
        self.label.setFont(font1)
        self.link_line = QLineEdit(Form)
        self.link_line.setObjectName(u"link_line")
        self.link_line.setGeometry(QRect(70, 16, 381, 31))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        self.link_line.setFont(font2)
        self.link_line.setFocusPolicy(Qt.NoFocus)
        self.link_line.setFrame(True)
        self.link_line.setDragEnabled(True)
        self.link_line.setClearButtonEnabled(True)
        self.update_section_list_btn = QPushButton(Form)
        self.update_section_list_btn.setObjectName(u"update_section_list_btn")
        self.update_section_list_btn.setGeometry(QRect(10, 300, 441, 51))
        self.update_section_list_btn.setFont(font)
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 220, 441, 20))
        font3 = QFont()
        font3.setBold(False)
        self.line.setFont(font3)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 240, 441, 51))
        self.progressBar.setValue(0)
        self.fast_loading_checkbox = QCheckBox(Form)
        self.fast_loading_checkbox.setObjectName(u"fast_loading_checkbox")
        self.fast_loading_checkbox.setEnabled(True)
        self.fast_loading_checkbox.setGeometry(QRect(200, 80, 239, 69))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fast_loading_checkbox.sizePolicy().hasHeightForWidth())
        self.fast_loading_checkbox.setSizePolicy(sizePolicy)
        self.fast_loading_checkbox.setFont(font)
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
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 167, 239, 41))
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 59, 181, 151))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -10, 166, 159))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_8 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setFont(font)
        self.checkBox_8.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 18px;\n"
"	height: 18px;\n"
"}\n"
"QCheckBox {	\n"
"	margin-left: 10px;\n"
"	spacing: 15px;\n"
"}")

        self.verticalLayout_3.addWidget(self.checkBox_8)

        self.checkBox_12 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setFont(font)
        self.checkBox_12.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 18px;\n"
"	height: 18px;\n"
"}\n"
"QCheckBox {	\n"
"	margin-left: 10px;\n"
"	spacing: 15px;\n"
"}")

        self.verticalLayout_3.addWidget(self.checkBox_12)

        self.checkBox_11 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setFont(font)
        self.checkBox_11.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 18px;\n"
"	height: 18px;\n"
"}\n"
"QCheckBox {	\n"
"	margin-left: 10px;\n"
"	spacing: 15px;\n"
"}")

        self.verticalLayout_3.addWidget(self.checkBox_11)

        self.checkBox_9 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setFont(font)
        self.checkBox_9.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 18px;\n"
"	height: 18px;\n"
"}\n"
"QCheckBox {	\n"
"	margin-left: 10px;\n"
"	spacing: 15px;\n"
"}")

        self.verticalLayout_3.addWidget(self.checkBox_9)

        self.checkBox_10 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setFont(font)
        self.checkBox_10.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 18px;\n"
"	height: 18px;\n"
"}\n"
"QCheckBox {	\n"
"	margin-left: 10px;\n"
"	spacing: 15px;\n"
"}")

        self.verticalLayout_3.addWidget(self.checkBox_10)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Yupoo parser", None))
#if QT_CONFIG(statustip)
        Form.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        Form.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        Form.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        Form.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.start_parsing_btn.setText(QCoreApplication.translate("Form", u"Start parsing", None))
        self.label.setText(QCoreApplication.translate("Form", u"Link", None))
        self.link_line.setText("")
        self.update_section_list_btn.setText(QCoreApplication.translate("Form", u"Update section list", None))
        self.fast_loading_checkbox.setText(QCoreApplication.translate("Form", u"Fast image loading\n"
"(some images may\n"
"not load completely)", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Open Folder", None))
        self.checkBox_8.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.checkBox_12.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.checkBox_11.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.checkBox_9.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.checkBox_10.setText(QCoreApplication.translate("Form", u"CheckBox", None))
    # retranslateUi

