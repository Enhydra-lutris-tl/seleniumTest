# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QVBoxLayout, QWidget)

global number2
number2 = [0, 0, 0, 0, 1]


class Ui_Form(object):

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1440, 897)
        Form.setMinimumSize(QSize(1440, 897))
        Form.setMaximumSize(QSize(1440, 900))
        Form.setStyleSheet(u"background: rgba(26, 28, 41, 1)")
        self.numeTable = QWidget(Form)
        self.numeTable.setObjectName(u"numeTable")
        self.numeTable.setGeometry(QRect(0, 0, 243, 900))
        self.numeTable.setStyleSheet(u"\n"
                                     "width: 234px;\n"
                                     "height: 900px;\n"
                                     "background: rgba(42, 43, 61, 1);\n"
                                     "")
        self.workbench_Button = QPushButton(self.numeTable)
        self.workbench_Button.setObjectName(u"workbench_Button")
        self.workbench_Button.setGeometry(QRect(30, 110, 173, 39))
        self.workbench_Button.setCursor(QCursor(Qt.OpenHandCursor))
        self.workbench_Button.setStyleSheet(u"\n"
                                            "border-radius: 6px;\n"
                                            "background: rgba(91, 133, 253, 1);\n"
                                            "padding: 10px 16px 10px 16px;\n"
                                            "color: rgba(255,255,255,1);\n"
                                            "font-size: 16px;\n"
                                            "font-weight: 500;")
        self.workbench_Button.clicked.connect(self.ceshi2(number2[0], 0))

        self.Model_Inject = QPushButton(self.numeTable)
        self.Model_Inject.setObjectName(u"Model_Inject")
        self.Model_Inject.setGeometry(QRect(30, 155, 173, 39))
        self.Model_Inject.setCursor(QCursor(Qt.OpenHandCursor))
        self.Model_Inject.setStyleSheet(u"\n"
                                        "border-radius: 6px;\n"
                                        "background: rgba(42, 43, 61, 1);\n"
                                        "padding: 10px 16px 10px 16px;\n"
                                        "color: rgba(255,255,255,1);\n"
                                        "font-size: 16px;\n"
                                        "font-weight: 500;")
        self.pushButton_3 = QPushButton(self.numeTable)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 200, 173, 39))
        self.pushButton_3.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_3.setStyleSheet(u"\n"
                                        "border-radius: 6px;\n"
                                        "background: rgba(42, 43, 61, 1);\n"
                                        "padding: 10px 16px 10px 16px;\n"
                                        "color: rgba(255,255,255,1);\n"
                                        "font-size: 16px;\n"
                                        "font-weight: 500;")
        self.pushButton_4 = QPushButton(self.numeTable)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(30, 245, 173, 39))
        self.pushButton_4.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_4.setStyleSheet(u"\n"
                                        "border-radius: 6px;\n"
                                        "background: rgba(42, 43, 61, 1);\n"
                                        "padding: 10px 16px 10px 16px;\n"
                                        "color: rgba(255,255,255,1);\n"
                                        "font-size: 16px;\n"
                                        "font-weight: 500;")
        self.pushButton_5 = QPushButton(self.numeTable)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(30, 290, 173, 39))
        self.pushButton_5.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_5.setStyleSheet(u"\n"
                                        "border-radius: 6px;\n"
                                        "background: rgba(42, 43, 61, 1);\n"
                                        "padding: 10px 16px 10px 16px;\n"
                                        "color: rgba(255,255,255,1);\n"
                                        "font-size: 16px;\n"
                                        "font-weight: 500;")
        self.pushButton_6 = QPushButton(self.numeTable)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(30, 335, 173, 39))
        self.pushButton_6.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_6.setStyleSheet(u"\n"
                                        "border-radius: 6px;\n"
                                        "background: rgba(42, 43, 61, 1);\n"
                                        "padding: 10px 16px 10px 16px;\n"
                                        "color: rgba(255,255,255,1);\n"
                                        "font-size: 16px;\n"
                                        "font-weight: 500;")
        self.pushButton_7 = QPushButton(self.numeTable)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(30, 380, 173, 39))
        self.pushButton_7.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_7.setStyleSheet(u"\n"
                                        "border-radius: 6px;\n"
                                        "background: rgba(42, 43, 61, 1);\n"
                                        "padding: 10px 16px 10px 16px;\n"
                                        "color: rgba(255,255,255,1);\n"
                                        "font-size: 16px;\n"
                                        "font-weight: 500;")
        self.pushButton_8 = QPushButton(self.numeTable)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(30, 425, 173, 39))
        self.pushButton_8.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_8.setStyleSheet(u"\n"
                                        "border-radius: 6px;\n"
                                        "background: rgba(42, 43, 61, 1);\n"
                                        "padding: 10px 16px 10px 16px;\n"
                                        "color: rgba(255,255,255,1);\n"
                                        "font-size: 16px;\n"
                                        "font-weight: 500;")
        self.headTable = QWidget(Form)
        self.headTable.setObjectName(u"headTable")
        self.headTable.setGeometry(QRect(0, 0, 1440, 80))
        self.headTable.setStyleSheet(u"left: 0px;\n"
                                     "top: 0px;\n"
                                     "width: 1440px;\n"
                                     "height: 80px;\n"
                                     "background: rgba(42, 43, 62, 1);\n"
                                     "")
        self.label = QLabel(self.headTable)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 26, 102, 28))
        self.label.setStyleSheet(u"\n"
                                 "font-size: 24px;\n"
                                 "font-weight: 700;\n"
                                 "color: rgba(255, 255, 255, 1);\n"
                                 "\n"
                                 "")
        self.lineEdit = QLineEdit(self.headTable)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(234, 20, 424, 40))
        self.lineEdit.setStyleSheet(u"padding:0 0 0 24px;\n"
                                    "border-radius: 20px;\n"
                                    "background: rgba(34, 36, 51, 1);\n"
                                    "")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(264, 110, 1146, 760))
        self.widget.setStyleSheet(u"left: 264px;\n"
                                  "top: 110px;\n"
                                  "width: 1146px;\n"
                                  "height: 760px;\n"
                                  "border-radius: 16px;\n"
                                  "background: rgba(42, 43, 61, 1);\n"
                                  "")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(545, 700, 201, 16))
        self.label_2.setStyleSheet(u"color:rgb(255,255,255)")
        self.layoutWidget = QWidget(self.widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 40, 444, 242))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSpacing(24)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.value_label_1 = QLabel(self.layoutWidget)
        self.value_label_1.setObjectName(u"value_label_1")
        self.value_label_1.setMinimumSize(QSize(80, 40))
        self.value_label_1.setMaximumSize(QSize(80, 40))
        self.value_label_1.setStyleSheet(u"border: 1px solid rgba(93, 94, 107, 1);\n"
                                         "color:rgb(255,255,255);\n"
                                         "border-radius: 2px 0 0 2px;\n"
                                         "\n"
                                         "")
        self.value_label_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.value_label_1)

        self.value_input_1 = QLineEdit(self.layoutWidget)
        self.value_input_1.setObjectName(u"value_input_1")
        self.value_input_1.setMinimumSize(QSize(360, 40))
        self.value_input_1.setMaximumSize(QSize(360, 40))
        self.value_input_1.setStyleSheet(u"color:rgb(255,255,255);\n"
                                         "border-radius: 0 4px 4px 0;\n"
                                         "background: rgba(34, 36, 51, 1);\n"
                                         "padding:0 0 0 12px\n"
                                         "")

        self.horizontalLayout.addWidget(self.value_input_1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.value_label_2 = QLabel(self.layoutWidget)
        self.value_label_2.setObjectName(u"value_label_2")
        self.value_label_2.setMinimumSize(QSize(80, 40))
        self.value_label_2.setMaximumSize(QSize(80, 40))
        self.value_label_2.setStyleSheet(u"border: 1px solid rgba(93, 94, 107, 1);\n"
                                         "color:rgb(255,255,255);\n"
                                         "border-radius: 2px 0 0 2px;\n"
                                         "\n"
                                         "")
        self.value_label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.value_label_2)

        self.value_input_2 = QLineEdit(self.layoutWidget)
        self.value_input_2.setObjectName(u"value_input_2")
        self.value_input_2.setMinimumSize(QSize(360, 40))
        self.value_input_2.setMaximumSize(QSize(360, 40))
        self.value_input_2.setStyleSheet(u"color:rgb(255,255,255);\n"
                                         "border-radius: 0 4px 4px 0;\n"
                                         "background: rgba(34, 36, 51, 1);\n"
                                         "padding:0 0 0 12px")

        self.horizontalLayout_2.addWidget(self.value_input_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.value_label_3 = QLabel(self.layoutWidget)
        self.value_label_3.setObjectName(u"value_label_3")
        self.value_label_3.setMinimumSize(QSize(80, 40))
        self.value_label_3.setMaximumSize(QSize(80, 40))
        self.value_label_3.setSizeIncrement(QSize(0, 0))
        self.value_label_3.setStyleSheet(u"border: 1px solid rgba(93, 94, 107, 1);\n"
                                         "color:rgb(255,255,255);\n"
                                         "border-radius: 2px 0 0 2px;\n"
                                         "\n"
                                         "")
        self.value_label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.value_label_3)

        self.value_input_3 = QLineEdit(self.layoutWidget)
        self.value_input_3.setObjectName(u"value_input_3")
        self.value_input_3.setMinimumSize(QSize(360, 40))
        self.value_input_3.setMaximumSize(QSize(360, 40))
        self.value_input_3.setStyleSheet(u"color:rgb(255,255,255);\n"
                                         "border-radius: 0 4px 4px 0;\n"
                                         "background: rgba(34, 36, 51, 1);\n"
                                         "padding:0 0 0 12px")

        self.horizontalLayout_7.addWidget(self.value_input_3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.value_label_4 = QLabel(self.layoutWidget)
        self.value_label_4.setObjectName(u"value_label_4")
        self.value_label_4.setMinimumSize(QSize(80, 40))
        self.value_label_4.setMaximumSize(QSize(80, 40))
        self.value_label_4.setSizeIncrement(QSize(0, 0))
        self.value_label_4.setStyleSheet(u"border: 1px solid rgba(93, 94, 107, 1);\n"
                                         "color:rgb(255,255,255);\n"
                                         "border-radius: 2px 0 0 2px;\n"
                                         "\n"
                                         "")
        self.value_label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.value_label_4)

        self.value_input_4 = QLineEdit(self.layoutWidget)
        self.value_input_4.setObjectName(u"value_input_4")
        self.value_input_4.setMinimumSize(QSize(360, 40))
        self.value_input_4.setMaximumSize(QSize(360, 40))
        self.value_input_4.setStyleSheet(u"color:rgb(255,255,255);\n"
                                         "border-radius: 0 4px 4px 0;\n"
                                         "background: rgba(34, 36, 51, 1);\n"
                                         "padding:0 0 0 12px")

        self.horizontalLayout_9.addWidget(self.value_input_4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.layoutWidget1 = QWidget(self.widget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(110, 400, 314, 52))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_10.setSpacing(60)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.clearnButton = QPushButton(self.layoutWidget1)
        self.clearnButton.setObjectName(u"clearnButton")
        self.clearnButton.setMinimumSize(QSize(104, 50))
        self.clearnButton.setMaximumSize(QSize(104, 50))
        self.clearnButton.setStyleSheet(u"\n"
                                        "border-radius: 6px;\n"
                                        "border: 1px solid rgb(255, 104, 97);            \n"
                                        "color: rgb(255, 104, 97);\n"
                                        "font-size: 16px;\n"
                                        "font-weight: 400;")

        self.horizontalLayout_10.addWidget(self.clearnButton)

        self.calculateButton = QPushButton(self.layoutWidget1)
        self.calculateButton.setObjectName(u"calculateButton")
        self.calculateButton.setMinimumSize(QSize(148, 50))
        self.calculateButton.setMaximumSize(QSize(148, 50))
        self.calculateButton.setStyleSheet(u"\n"
                                           "border-radius: 6px;\n"
                                           "background: rgba(91, 133, 253, 1);\n"
                                           "font-size: 16px;\n"
                                           "font-weight: 400;\n"
                                           "color: rgba(255, 255, 255, 1);\n"
                                           "")

        self.horizontalLayout_10.addWidget(self.calculateButton)
        self.calculateButton.clicked.connect(self.ceshi)

        self.message_label = QLabel(self.widget)
        self.message_label.setObjectName(u"message_label")
        self.message_label.setGeometry(QRect(545, 40, 561, 641))
        self.message_label.setStyleSheet(u"border-radius: 0;\n"
                                         "background: rgba(34, 36, 51, 1);\n"
                                         "padding:12px 0 12px 12px;\n"
                                         "color:rgba(255,255,255,0.5);\n"
                                         "font-size:16px"
                                         )
        self.message_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.workbench_Button.setText(QCoreApplication.translate("Form", u"\u5de5\u4f5c\u53f0", None))
        self.Model_Inject.setText(QCoreApplication.translate("Form", u"\u6a21\u578b\u5bfc\u5165", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u5de5\u5177\u7bb1", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u529f\u80fd3", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("Form", u"QtTest", None))
        self.label_2.setText(QCoreApplication.translate("Form",
                                                        u"\u6b64\u5904\u5c55\u793a\u8ba1\u7b97\u8fc7\u7a0b\u53ca\u7ed3\u679c\uff01",
                                                        None))
        self.value_label_1.setText(QCoreApplication.translate("Form", u"\u53c2\u65701", None))
        self.value_input_1.setPlaceholderText(
            QCoreApplication.translate("Form", u"\u8f93\u5165\u9884\u4f30\u503c", None))
        self.value_label_2.setText(QCoreApplication.translate("Form", u"\u53c2\u65702", None))
        self.value_input_2.setPlaceholderText(
            QCoreApplication.translate("Form", u"\u8f93\u5165\u9884\u4f30\u503c", None))
        self.value_label_3.setText(QCoreApplication.translate("Form", u"\u53c2\u65702", None))
        self.value_input_3.setPlaceholderText(
            QCoreApplication.translate("Form", u"\u8f93\u5165\u9884\u4f30\u503c", None))
        self.value_label_4.setText(QCoreApplication.translate("Form", u"\u53c2\u65702", None))
        self.value_input_4.setPlaceholderText(
            QCoreApplication.translate("Form", u"\u8f93\u5165\u9884\u4f30\u503c", None))
        self.clearnButton.setText(QCoreApplication.translate("Form", u"\u6e05\u9664", None))
        self.calculateButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u8ba1\u7b97", None))
        self.message_label.setText("")

    # retranslateUi

    @Slot()
    def ceshi(self):
        message = self.message_label.text()
        if self.value_input_1.text() != '' and self.value_input_2.text() != '' and self.value_input_3.text() != '' and self.value_input_4.text() != '':

            number = int(self.value_input_1.text()) + int(self.value_input_2.text()) + int(
                self.value_input_3.text()) + int(self.value_input_4.text())
            self.message_label.setText(message + '计算完成：' + str(number) + '\n')
        else:
            self.message_label.setText(message + '有没有填写的值\n')

    @Slot()
    def ceshi2(self, number, count):
        if number == 0:
            for i in range(5):
                number2[i] = 0
            number2[count] = 1
        print(number2)
