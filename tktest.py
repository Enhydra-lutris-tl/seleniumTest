#!/bin/env python3
import sys

from PySide6.QtCore import Qt, Signal, Slot, QThread, QRect, QSize
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, \
    QStyle, QTextEdit, QMessageBox

import httpx

import sys
from untitled import Ui_Form


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        # build ui
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
