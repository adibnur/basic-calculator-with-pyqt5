# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("$10B Calculator")
        MainWindow.resize(411, 367)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 150, 71, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(90, 150, 71, 51))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(170, 150, 71, 51))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_dot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dot.setGeometry(QtCore.QRect(90, 270, 71, 51))
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_power = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_power.setGeometry(QtCore.QRect(170, 270, 71, 51))
        self.pushButton_power.setObjectName("pushButton_power")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(10, 270, 71, 51))
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 210, 71, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 210, 71, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 210, 71, 51))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(90, 90, 71, 51))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(170, 90, 71, 51))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 90, 71, 51))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(250, 210, 71, 51))
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_del = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_del.setGeometry(QtCore.QRect(250, 90, 71, 51))
        self.pushButton_del.setObjectName("pushButton_del")
        self.pushButton_mult = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mult.setGeometry(QtCore.QRect(250, 150, 71, 51))
        self.pushButton_mult.setObjectName("pushButton_mult")
        self.pushButton_ans = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ans.setGeometry(QtCore.QRect(250, 270, 71, 51))
        self.pushButton_ans.setObjectName("pushButton_ans")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(330, 210, 71, 51))
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_ac = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ac.setGeometry(QtCore.QRect(330, 90, 71, 51))
        self.pushButton_ac.setObjectName("pushButton_ac")
        self.pushButton_div = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_div.setGeometry(QtCore.QRect(330, 150, 71, 51))
        self.pushButton_div.setObjectName("pushButton_div")
        self.pushButton_eq = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_eq.setGeometry(QtCore.QRect(330, 270, 71, 51))
        self.pushButton_eq.setObjectName("pushButton_eq")
        self.label_in = QtWidgets.QLabel(self.centralwidget)
        self.label_in.setGeometry(QtCore.QRect(10, 10, 251, 61))
        self.label_in.setAutoFillBackground(False)
        self.label_in.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_in.setLineWidth(2)
        self.label_in.setMidLineWidth(2)
        self.label_in.setTextFormat(QtCore.Qt.AutoText)
        self.label_in.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_in.setIndent(0)
        self.label_in.setObjectName("label_in")
        self.label_out = QtWidgets.QLabel(self.centralwidget)
        self.label_out.setGeometry(QtCore.QRect(270, 10, 121, 61))
        self.label_out.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_out.setLineWidth(2)
        self.label_out.setMidLineWidth(2)
        self.label_out.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_out.setObjectName("label_out")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("$10B Calculator", "$10B Calculator"))
        self.pushButton_6.setText(_translate("$10B Calculator", "4"))
        self.pushButton_7.setText(_translate("$10B Calculator", "5"))
        self.pushButton_8.setText(_translate("$10B Calculator", "6"))
        self.pushButton_dot.setText(_translate("$10B Calculator", "."))
        self.pushButton_power.setText(_translate("$10B Calculator", "^"))
        self.pushButton_0.setText(_translate("$10B Calculator", "0"))
        self.pushButton_4.setText(_translate("$10B Calculator", "2"))
        self.pushButton_5.setText(_translate("$10B Calculator", "3"))
        self.pushButton_1.setText(_translate("$10B Calculator", "1"))
        self.pushButton_10.setText(_translate("$10B Calculator", "8"))
        self.pushButton_11.setText(_translate("$10B Calculator", "9"))
        self.pushButton_9.setText(_translate("$10B Calculator", "7"))
        self.pushButton_plus.setText(_translate("$10B Calculator", "+"))
        self.pushButton_del.setText(_translate("$10B Calculator", "Del"))
        self.pushButton_mult.setText(_translate("$10B Calculator", "*"))
        self.pushButton_ans.setText(_translate("$10B Calculator", "Ans"))
        self.pushButton_minus.setText(_translate("$10B Calculator", "-"))
        self.pushButton_ac.setText(_translate("$10B Calculator", "AC"))
        self.pushButton_div.setText(_translate("$10B Calculator", "/"))
        self.pushButton_eq.setText(_translate("$10B Calculator", "="))
        self.label_in.setText(_translate("$10B Calculator", f"<html><head/><body><p><span style=\" font-size:12pt;\">{self.input_field_text}</span></p></body></html>"))
        self.label_out.setText(_translate("$10B Calculator", f"<html><head/><body><p><span style=\" font-size:12pt;\">{self.input_field_text}</span></p></body></html>"))

        # map input buttons
        self.pushButton_6.clicked.connect(lambda : self.click_inp("4"))
        self.pushButton_7.clicked.connect(lambda : self.click_inp("5"))
        self.pushButton_8.clicked.connect(lambda : self.click_inp("6"))
        self.pushButton_dot.clicked.connect(lambda : self.click_inp("."))
        self.pushButton_power.clicked.connect(lambda : self.click_inp_sign("^"))
        self.pushButton_0.clicked.connect(lambda : self.click_inp("0"))
        self.pushButton_4.clicked.connect(lambda : self.click_inp("2"))
        self.pushButton_5.clicked.connect(lambda : self.click_inp("3"))
        self.pushButton_1.clicked.connect(lambda : self.click_inp("1"))
        self.pushButton_10.clicked.connect(lambda : self.click_inp("8"))
        self.pushButton_11.clicked.connect(lambda : self.click_inp("9"))
        self.pushButton_9.clicked.connect(lambda : self.click_inp("7"))
        self.pushButton_plus.clicked.connect(lambda : self.click_inp_sign("+"))
        self.pushButton_mult.clicked.connect(lambda : self.click_inp_sign("*"))
        self.pushButton_minus.clicked.connect(lambda : self.click_inp_sign("-"))
        self.pushButton_div.clicked.connect(lambda : self.click_inp_sign("/"))

        #map of erase buttons
        self.pushButton_del.clicked.connect(self.click_Del)
        self.pushButton_ac.clicked.connect(self.click_ac)

        #map of answer buttons
        self.pushButton_eq.clicked.connect(self.click_eq)
        self.pushButton_ans.clicked.connect(self.click_ans)

    def __init__(self):
        self.input_field_text = '0'
        self.ans = '0'
    
    def click_inp(self, inp):
        _translate = QtCore.QCoreApplication.translate
        if self.input_field_text == '0':
            self.input_field_text = inp
        else:
            self.input_field_text += inp

        self.label_in.setText(_translate("$10B Calculator", f"<html><head/><body><p><span style=\" font-size:12pt;\">{self.input_field_text}</span></p></body></html>"))

    def click_inp_sign(self, inp):
        _translate = QtCore.QCoreApplication.translate
        if self.input_field_text == '0':
            self.input_field_text = 'Ans'+inp
        else:
            self.input_field_text += inp

        self.label_in.setText(_translate("$10B Calculator", f"<html><head/><body><p><span style=\" font-size:12pt;\">{self.input_field_text}</span></p></body></html>"))

    def click_Del(self):
        _translate = QtCore.QCoreApplication.translate
        if len(self.input_field_text) == 1:
            self.input_field_text = '0'
        elif self.input_field_text[-3:] == 'Ans':
            self.input_field_text = self.input_field_text[:-3]
        else:
            self.input_field_text = self.input_field_text[:-1]
        
        self.label_in.setText(_translate("$10B Calculator", f"<html><head/><body><p><span style=\" font-size:12pt;\">{self.input_field_text}</span></p></body></html>"))

    def click_ac(self):
        _translate = QtCore.QCoreApplication.translate
        self.input_field_text = '0'
        
        self.label_in.setText(_translate("$10B Calculator", f"<html><head/><body><p><span style=\" font-size:12pt;\">{self.input_field_text}</span></p></body></html>"))
        self.label_out.setText(_translate("$10B Calculator", f"<html><head/><body><p><span style=\" font-size:12pt;\">{self.input_field_text}</span></p></body></html>"))

    def click_eq(self):
        _translate = QtCore.QCoreApplication.translate
        self.input_field_text = self.input_field_text.replace('^', '**')
        self.input_field_text = self.input_field_text.replace('Ans', self.ans)

        try:
            self.output_field_text = eval(self.input_field_text)
        except ZeroDivisionError:
            self.output_field_text = 0
            
        self.label_out.setText(_translate("$10B Calculator", f"<html><head/><body><p><span style=\" font-size:12pt;\">{self.output_field_text}</span></p></body></html>"))
        self.ans = str(self.output_field_text)
        self.input_field_text = '0'

    def click_ans(self):
        _translate = QtCore.QCoreApplication.translate
        if self.input_field_text == '0':
            self.input_field_text = 'Ans'
        else:    
            self.input_field_text += 'Ans'
        self.label_in.setText(_translate("$10B Calculator", f"<html><head/><body><p><span style=\" font-size:12pt;\">{self.input_field_text}</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
