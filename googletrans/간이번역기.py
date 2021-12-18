import googletrans
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

translator = googletrans.Translator()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1031, 794)
        self.widget = QtWidgets.QWidget(MainWindow)

        font = QtGui.QFont()
        font.setPointSize(1)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")

        # 번역 버튼
        self.btn1 = QtWidgets.QPushButton(self.widget)
        self.btn1.setGeometry(QtCore.QRect(850, 90, 111, 41))
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕")
        font.setPointSize(16)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet("color:rgb(130, 114, 255)")
        self.btn1.setObjectName("btn1")
        self.btn1.clicked.connect(self.press_btn_trans)

        # 지우기 버튼
        self.btn2 = QtWidgets.QPushButton(self.widget)
        self.btn2.setGeometry(QtCore.QRect(440, 700, 121, 51))
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕")
        font.setPointSize(14)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("color:rgb(130, 114, 255)")
        self.btn2.setObjectName("btn2")
        self.btn2.clicked.connect(self.clear_btn2)

        self.result_label = QtWidgets.QLabel(self.widget)
        self.result_label.setGeometry(QtCore.QRect(340, 20, 331, 51))
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕")
        font.setPointSize(20)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.result_label.setFont(font)
        self.result_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_label.setAutoFillBackground(False)
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label.setObjectName("result_label")

        self.text_input = QtWidgets.QTextEdit(self.widget)
        self.text_input.setGeometry(QtCore.QRect(63, 90, 741, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_input.setFont(font)
        self.text_input.setObjectName("text_input")

        # 영어 섹션
        self.english = QtWidgets.QTextBrowser(self.widget)
        self.english.setGeometry(QtCore.QRect(60, 180, 901, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.english.setFont(font)
        self.english.setObjectName("english")

        self.result_label_2 = QtWidgets.QLabel(self.widget)
        self.result_label_2.setGeometry(QtCore.QRect(60, 150, 91, 21))
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.result_label_2.setFont(font)
        self.result_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_label_2.setAutoFillBackground(False)
        self.result_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label_2.setObjectName("result_label_2")

        # 일어 섹션
        self.japaness = QtWidgets.QTextBrowser(self.widget)
        self.japaness.setGeometry(QtCore.QRect(60, 280, 901, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.japaness.setFont(font)
        self.japaness.setObjectName("japaness")

        self.result_label_3 = QtWidgets.QLabel(self.widget)
        self.result_label_3.setGeometry(QtCore.QRect(60, 250, 91, 21))
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.result_label_3.setFont(font)
        self.result_label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_label_3.setAutoFillBackground(False)
        self.result_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label_3.setObjectName("result_label_3")

        # 중국어 섹션
        self.chiness = QtWidgets.QTextBrowser(self.widget)
        self.chiness.setGeometry(QtCore.QRect(60, 380, 901, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chiness.setFont(font)
        self.chiness.setObjectName("chiness")

        self.result_label_4 = QtWidgets.QLabel(self.widget)
        self.result_label_4.setGeometry(QtCore.QRect(60, 350, 91, 21))
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.result_label_4.setFont(font)
        self.result_label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_label_4.setAutoFillBackground(False)
        self.result_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label_4.setObjectName("result_label_4")

        # 프랑스어 섹션
        self.franch = QtWidgets.QTextBrowser(self.widget)
        self.franch.setGeometry(QtCore.QRect(60, 580, 901, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.franch.setFont(font)
        self.franch.setObjectName("franch")

        self.result_label_5 = QtWidgets.QLabel(self.widget)
        self.result_label_5.setGeometry(QtCore.QRect(60, 450, 91, 21))
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.result_label_5.setFont(font)
        self.result_label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_label_5.setAutoFillBackground(False)
        self.result_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label_5.setObjectName("result_label_5")

        # 이탈리아어 섹션
        self.italiano = QtWidgets.QTextBrowser(self.widget)
        self.italiano.setGeometry(QtCore.QRect(60, 480, 901, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.italiano.setFont(font)
        self.italiano.setObjectName("italiano")

        self.result_label_6 = QtWidgets.QLabel(self.widget)
        self.result_label_6.setGeometry(QtCore.QRect(60, 550, 91, 21))
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.result_label_6.setFont(font)
        self.result_label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_label_6.setAutoFillBackground(False)
        self.result_label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label_6.setObjectName("result_label_6")
        MainWindow.setCentralWidget(self.widget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "간이 번역기"))
        MainWindow.setWindowIcon(QIcon('icons/google-logo.png'))
        self.btn1.setText(_translate("MainWindow", "번역!!!"))
        self.btn2.setText(_translate("MainWindow", "지우기"))
        self.result_label.setText(_translate("MainWindow", "번 역 기"))
        self.text_input.setText(_translate("MainWindow", ""))
        self.result_label_2.setText(_translate("MainWindow", "English"))
        self.result_label_3.setText(_translate("MainWindow", "日語"))
        self.result_label_4.setText(_translate("MainWindow", "중국어"))
        self.result_label_5.setText(_translate("MainWindow", "français"))
        self.result_label_6.setText(_translate("MainWindow", "Italiano"))

    def press_btn_trans(self):
        text = self.text_input.toPlainText()
        resulten = translator.translate(text, dest='en').text  # 영
        self.english.setText(resulten)

        resultja = translator.translate(text, dest='ja').text  # 일
        self.japaness.setText(resultja)
        # zh-cn
        resultcn = translator.translate(text, dest='zh-cn').text  # 중
        self.chiness.setText(resultcn)

        resultfr = translator.translate(text, dest='fr').text  # 프
        self.franch.setText(resultfr)

        resultit = translator.translate(text, dest='it').text  # 이
        self.italiano.setText(resultit)

    def clear_btn2(self):
        self.text_input.clear()
        self.english.clear()
        self.japaness.clear()
        self.chiness.clear()
        self.franch.clear()
        self.italiano.clear()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
