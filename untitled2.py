# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
                               QPushButton, QSizePolicy, QTabWidget, QVBoxLayout,
                               QWidget)


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
        self.workbench_Button.setCursor(QCursor(Qt.ArrowCursor))
        self.workbench_Button.setStyleSheet(u"QPushButton{\n"
                                            "border-radius: 6px;\n"
                                            "background: rgba(91, 133, 253, 1);\n"
                                            "padding: 10px 16px 10px 16px;\n"
                                            "color: rgba(255,255,255,1);\n"
                                            "font-size: 16px;\n"
                                            "font-weight: 500;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "background: rgba(120, 133, 253, 1);\n"
                                            "}\n"
                                            "")
        self.workbench_Button.clicked.connect(lambda: self.ceshi(0))
        self.Model_Inject = QPushButton(self.numeTable)
        self.Model_Inject.setObjectName(u"Model_Inject")
        self.Model_Inject.setGeometry(QRect(30, 155, 173, 39))
        self.Model_Inject.setCursor(QCursor(Qt.ArrowCursor))
        self.Model_Inject.setStyleSheet(u"QPushButton{\n"
                                        "border-radius: 6px;\n"
                                        "background: rgba(42, 43, 61, 1);\n"
                                        "padding: 10px 16px 10px 16px;\n"
                                        "color: rgba(255,255,255,1);\n"
                                        "font-size: 16px;\n"
                                        "font-weight: 500;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "background: rgba(120, 133, 253, 1);\n"
                                        "}")
        self.Model_Inject.clicked.connect(lambda: self.ceshi(1))
        self.pushButton_3 = QPushButton(self.numeTable)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 200, 173, 39))
        self.pushButton_3.setCursor(QCursor(Qt.ArrowCursor))
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
        self.pushButton_4.setCursor(QCursor(Qt.ArrowCursor))
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
        self.pushButton_5.setCursor(QCursor(Qt.ArrowCursor))
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
        self.pushButton_7.setCursor(QCursor(Qt.ArrowCursor))
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
        self.pushButton_8.setCursor(QCursor(Qt.ArrowCursor))
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
        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(230, 80, 1211, 821))
        self.tabWidget_2 = QTabWidget(self.widget_3)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(30, 0, 1146, 820))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.widget_4 = QWidget(self.tab_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(0, 0, 1146, 760))
        self.widget_4.setStyleSheet(u"left: 264px;\n"
                                    "top: 110px;\n"
                                    "width: 1146px;\n"
                                    "height: 760px;\n"
                                    "border-radius: 16px;\n"
                                    "background: rgba(42, 43, 61, 1);\n"
                                    "")
        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(545, 700, 201, 16))
        self.label_4.setStyleSheet(u"color:rgb(255,255,255)")
        self.layoutWidget_4 = QWidget(self.widget_4)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(50, 40, 444, 242))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_4.setSpacing(24)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.value_label_9 = QLabel(self.layoutWidget_4)
        self.value_label_9.setObjectName(u"value_label_9")
        self.value_label_9.setMinimumSize(QSize(80, 40))
        self.value_label_9.setMaximumSize(QSize(80, 40))
        self.value_label_9.setStyleSheet(u"border: 1px solid rgba(93, 94, 107, 1);\n"
                                         "color:rgb(255,255,255);\n"
                                         "border-radius: 2px 0 0 2px;\n"
                                         "\n"
                                         "")
        self.value_label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.value_label_9)

        self.value_input_9 = QLineEdit(self.layoutWidget_4)
        self.value_input_9.setObjectName(u"value_input_9")
        self.value_input_9.setMinimumSize(QSize(360, 40))
        self.value_input_9.setMaximumSize(QSize(360, 40))
        self.value_input_9.setStyleSheet(u"color:rgb(255,255,255);\n"
                                         "border-radius: 0 4px 4px 0;\n"
                                         "background: rgba(34, 36, 51, 1);\n"
                                         "padding:0 0 0 12px\n"
                                         "")

        self.horizontalLayout_5.addWidget(self.value_input_9)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.value_label_10 = QLabel(self.layoutWidget_4)
        self.value_label_10.setObjectName(u"value_label_10")
        self.value_label_10.setMinimumSize(QSize(80, 40))
        self.value_label_10.setMaximumSize(QSize(80, 40))
        self.value_label_10.setStyleSheet(u"border: 1px solid rgba(93, 94, 107, 1);\n"
                                          "color:rgb(255,255,255);\n"
                                          "border-radius: 2px 0 0 2px;\n"
                                          "\n"
                                          "")
        self.value_label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.value_label_10)

        self.value_input_10 = QLineEdit(self.layoutWidget_4)
        self.value_input_10.setObjectName(u"value_input_10")
        self.value_input_10.setMinimumSize(QSize(360, 40))
        self.value_input_10.setMaximumSize(QSize(360, 40))
        self.value_input_10.setStyleSheet(u"color:rgb(255,255,255);\n"
                                          "border-radius: 0 4px 4px 0;\n"
                                          "background: rgba(34, 36, 51, 1);\n"
                                          "padding:0 0 0 12px")

        self.horizontalLayout_6.addWidget(self.value_input_10)

        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.value_label_11 = QLabel(self.layoutWidget_4)
        self.value_label_11.setObjectName(u"value_label_11")
        self.value_label_11.setMinimumSize(QSize(80, 40))
        self.value_label_11.setMaximumSize(QSize(80, 40))
        self.value_label_11.setSizeIncrement(QSize(0, 0))
        self.value_label_11.setStyleSheet(u"border: 1px solid rgba(93, 94, 107, 1);\n"
                                          "color:rgb(255,255,255);\n"
                                          "border-radius: 2px 0 0 2px;\n"
                                          "\n"
                                          "")
        self.value_label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.value_label_11)

        self.value_input_11 = QLineEdit(self.layoutWidget_4)
        self.value_input_11.setObjectName(u"value_input_11")
        self.value_input_11.setMinimumSize(QSize(360, 40))
        self.value_input_11.setMaximumSize(QSize(360, 40))
        self.value_input_11.setStyleSheet(u"color:rgb(255,255,255);\n"
                                          "border-radius: 0 4px 4px 0;\n"
                                          "background: rgba(34, 36, 51, 1);\n"
                                          "padding:0 0 0 12px")

        self.horizontalLayout_9.addWidget(self.value_input_11)

        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.value_label_12 = QLabel(self.layoutWidget_4)
        self.value_label_12.setObjectName(u"value_label_12")
        self.value_label_12.setMinimumSize(QSize(80, 40))
        self.value_label_12.setMaximumSize(QSize(80, 40))
        self.value_label_12.setSizeIncrement(QSize(0, 0))
        self.value_label_12.setStyleSheet(u"border: 1px solid rgba(93, 94, 107, 1);\n"
                                          "color:rgb(255,255,255);\n"
                                          "border-radius: 2px 0 0 2px;\n"
                                          "\n"
                                          "")
        self.value_label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.value_label_12)

        self.value_input_12 = QLineEdit(self.layoutWidget_4)
        self.value_input_12.setObjectName(u"value_input_12")
        self.value_input_12.setMinimumSize(QSize(360, 40))
        self.value_input_12.setMaximumSize(QSize(360, 40))
        self.value_input_12.setStyleSheet(u"color:rgb(255,255,255);\n"
                                          "border-radius: 0 4px 4px 0;\n"
                                          "background: rgba(34, 36, 51, 1);\n"
                                          "padding:0 0 0 12px")

        self.horizontalLayout_13.addWidget(self.value_input_12)

        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.layoutWidget_5 = QWidget(self.widget_4)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(110, 400, 314, 52))
        self.horizontalLayout_14 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_14.setSpacing(60)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.clearnButton_3 = QPushButton(self.layoutWidget_5)
        self.clearnButton_3.setObjectName(u"clearnButton_3")
        self.clearnButton_3.setMinimumSize(QSize(104, 50))
        self.clearnButton_3.setMaximumSize(QSize(104, 50))
        self.clearnButton_3.setStyleSheet(u"\n"
                                          "border-radius: 6px;\n"
                                          "border: 1px solid rgb(255, 104, 97);            \n"
                                          "color: rgb(255, 104, 97);\n"
                                          "font-size: 16px;\n"
                                          "font-weight: 400;")

        self.horizontalLayout_14.addWidget(self.clearnButton_3)

        self.calculateButton_3 = QPushButton(self.layoutWidget_5)
        self.calculateButton_3.setObjectName(u"calculateButton_3")
        self.calculateButton_3.setMinimumSize(QSize(148, 50))
        self.calculateButton_3.setMaximumSize(QSize(148, 50))
        self.calculateButton_3.setStyleSheet(u"\n"
                                             "border-radius: 6px;\n"
                                             "background: rgba(91, 133, 253, 1);\n"
                                             "font-size: 16px;\n"
                                             "font-weight: 400;\n"
                                             "color: rgba(255, 255, 255, 1);\n"
                                             "")

        self.horizontalLayout_14.addWidget(self.calculateButton_3)

        self.message_label_3 = QLabel(self.widget_4)
        self.message_label_3.setObjectName(u"message_label_3")
        self.message_label_3.setGeometry(QRect(545, 40, 561, 641))
        self.message_label_3.setStyleSheet(u"border-radius: 0;\n"
                                           "background: rgba(34, 36, 51, 1);\n"
                                           "padding:12px 0 12px 12px;\n"
                                           "color:rgb(255,255,255);\n"
                                           "font-size:16px")
        self.message_label_3.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.widget_5 = QWidget(self.tab_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(0, 0, 971, 691))
        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(440, 300, 111, 51))
        self.label_5.setStyleSheet(u"background:rgb(255,255,255);\n"
                                   "font-size:24px")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(380, -5, 511, 31))

        self.retranslateUi(Form)

        self.tabWidget_2.setCurrentIndex(0)

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
        self.label_4.setText(QCoreApplication.translate("Form",
                                                        u"\u6b64\u5904\u5c55\u793a\u8ba1\u7b97\u8fc7\u7a0b\u53ca\u7ed3\u679c\uff01",
                                                        None))
        self.value_label_9.setText(QCoreApplication.translate("Form", u"\u53c2\u65701", None))
        self.value_input_9.setPlaceholderText(
            QCoreApplication.translate("Form", u"\u8f93\u5165\u9884\u4f30\u503c", None))
        self.value_label_10.setText(QCoreApplication.translate("Form", u"\u53c2\u65702", None))
        self.value_input_10.setPlaceholderText(
            QCoreApplication.translate("Form", u"\u8f93\u5165\u9884\u4f30\u503c", None))
        self.value_label_11.setText(QCoreApplication.translate("Form", u"\u53c2\u65702", None))
        self.value_input_11.setPlaceholderText(
            QCoreApplication.translate("Form", u"\u8f93\u5165\u9884\u4f30\u503c", None))
        self.value_label_12.setText(QCoreApplication.translate("Form", u"\u53c2\u65702", None))
        self.value_input_12.setPlaceholderText(
            QCoreApplication.translate("Form", u"\u8f93\u5165\u9884\u4f30\u503c", None))
        self.clearnButton_3.setText(QCoreApplication.translate("Form", u"\u6e05\u9664", None))
        self.calculateButton_3.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u8ba1\u7b97", None))
        self.message_label_3.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3),
                                    QCoreApplication.translate("Form", u"Tab 1", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"111111", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4),
                                    QCoreApplication.translate("Form", u"Tab 2", None))
        self.label_6.setText("")

    # retranslateUi

    @Slot()
    def ceshi(self, number):
        print(111111111, number)
        ORstyle=u"QPushButton{\n""border-radius: 6px;\n""background: rgba(42, 43, 61, 1);\n""padding: 10px 16px 10px 16px;\n""color: rgba(255,255,255,1);\n""font-size: 16px;\n""font-weight: 500;\n""}\n""QPushButton:hover{\n""background: rgba(120, 133, 253, 0.5);\n""}\n"""
        CDstyle=u"QPushButton{\n""border-radius: 6px;\n""background: rgba(91, 133, 253, 1);\n""padding: 10px 16px 10px 16px;\n""color: rgba(255,255,255,1);\n""font-size: 16px;\n""font-weight: 500;\n""}\n""QPushButton:hover{\n""background: rgba(120, 133, 253, 0.5);\n""}\n"""
        self.tabWidget_2.setCurrentIndex(number)
        for i in range(2):
            if i == 0:
                self.workbench_Button.setStyleSheet(ORstyle)
            elif i == 1:
                self.Model_Inject.setStyleSheet(ORstyle)
        if number == 0:
            self.workbench_Button.setStyleSheet(CDstyle)
        elif number == 1:
            self.Model_Inject.setStyleSheet(CDstyle)