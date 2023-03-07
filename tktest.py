import sys
import setwecat
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit


class QmyWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类的构造函数，创建QWidget窗体
        self.setupUi()

    def setupUi(self):
        """页面初始化"""
        # 设置窗体大小及标题
        self.resize(500, 400)
        self.setWindowTitle("PyQt5测试")
        # 创建布局
        # self.layout = QVBoxLayout()

        # QPushButton组件示例
        self.button1 = QPushButton('测试按钮', self)
        self.button1.setProperty('name', 'btn1')
        self.button2 = QPushButton('自动发信息', self)
        self.button2.setProperty('name', 'btn2')
        self.input1 = QLineEdit("hello", self)
        # QPushButton组件设置
        self.button1.setEnabled(False)  # button1设置按钮不可用
        self.button2.setIcon(QIcon('logo.png'))  # button2设置按钮图标
        # self.button2.resize(200, 100)
        self.button2.move(200, 300)
        # QPushButton关联信号
        self.button2.clicked.connect(self.on_button2_clicked)  # button2按钮关联点击信号
        # 输入组件设置
        self.input1.setPlaceholderText("输入内容")
        self.input1.move(100, 20)
        self.input1.resize(200, 60)
        self.input1.setCursor(Qt.PointingHandCursor)
        # 将组件添加到布局中
        # self.layout.addWidget(self.button1)
        # self.layout.addWidget(self.button2)
        # self.layout.addWidget(self.input1)
        # 为窗体添加布局
        # self.setLayout(self.layout)

    def on_button2_clicked(self):
        """button2按钮点击槽函数"""
        setwecat.main()
        print("button2按钮被点击啦！")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myMain = QmyWidget()

    # qss引入方法
    with open('index.qss', 'r', encoding='UTF-8') as f:
        print('打开文件')
        app.setStyleSheet(f.read())
    # qssStyle = '''
    #         QPushButton[name="btn1"] {
    #             background-color:red;
    #             color:yellow;
    #             height:120;
    #             font-size:60px;
    #         }
    #         QPushButton[name="btn2"] {
    #             background-color:blue;
    #             color:yellow;
    #             height:60;
    #             width:120;
    #             font-size:11px;
    #         }
    #         '''
    # myMain.setStyleSheet(qssStyle)
    myMain.show()
    sys.exit(app.exec_())
