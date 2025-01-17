# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'luncher.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(497, 375)
        self.inputdir_btn = QtWidgets.QPushButton(Dialog)
        self.inputdir_btn.setGeometry(QtCore.QRect(250, 20, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.inputdir_btn.setFont(font)
        self.inputdir_btn.setStyleSheet("background-color:rgb(255, 127, 127)")
        self.inputdir_btn.setObjectName("inputdir_btn")
        self.inputdir_textview = QtWidgets.QLineEdit(Dialog)
        self.inputdir_textview.setGeometry(QtCore.QRect(10, 160, 461, 20))
        self.inputdir_textview.setStyleSheet("background-color:rgb(255, 127, 127)")
        self.inputdir_textview.setObjectName("inputdir_textview")
        self.lable_cn_btn = QtWidgets.QPushButton(Dialog)
        self.lable_cn_btn.setGeometry(QtCore.QRect(10, 20, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lable_cn_btn.setFont(font)
        self.lable_cn_btn.setStyleSheet("background-color:rgb(0, 255, 127)")
        self.lable_cn_btn.setObjectName("lable_cn_btn")
        self.lable_cnen_btn = QtWidgets.QPushButton(Dialog)
        self.lable_cnen_btn.setGeometry(QtCore.QRect(120, 20, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lable_cnen_btn.setFont(font)
        self.lable_cnen_btn.setStyleSheet("background-color:rgb(255, 255, 127)")
        self.lable_cnen_btn.setObjectName("lable_cnen_btn")
        self.outputdir_btn = QtWidgets.QPushButton(Dialog)
        self.outputdir_btn.setGeometry(QtCore.QRect(360, 20, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.outputdir_btn.setFont(font)
        self.outputdir_btn.setStyleSheet("background-color:rgb(255, 127, 255)")
        self.outputdir_btn.setObjectName("outputdir_btn")
        self.lable_cn_textview = QtWidgets.QLineEdit(Dialog)
        self.lable_cn_textview.setGeometry(QtCore.QRect(10, 100, 461, 20))
        self.lable_cn_textview.setStyleSheet("background-color:rgb(0, 255, 127)")
        self.lable_cn_textview.setObjectName("lable_cn_textview")
        self.lable_cnen_textview = QtWidgets.QLineEdit(Dialog)
        self.lable_cnen_textview.setGeometry(QtCore.QRect(10, 130, 461, 20))
        self.lable_cnen_textview.setStyleSheet("background-color:rgb(255, 255, 127)")
        self.lable_cnen_textview.setObjectName("lable_cnen_textview")
        self.outputdir_textview = QtWidgets.QLineEdit(Dialog)
        self.outputdir_textview.setGeometry(QtCore.QRect(10, 190, 451, 20))
        self.outputdir_textview.setStyleSheet("background-color:rgb(255, 127, 255)")
        self.outputdir_textview.setObjectName("outputdir_textview")
        self.result_out_textview = QtWidgets.QPlainTextEdit(Dialog)
        self.result_out_textview.setGeometry(QtCore.QRect(20, 250, 311, 111))
        self.result_out_textview.setObjectName("result_out_textview")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 220, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.action_do_conv = QtWidgets.QPushButton(Dialog)
        self.action_do_conv.setGeometry(QtCore.QRect(350, 260, 111, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.action_do_conv.setFont(font)
        self.action_do_conv.setObjectName("action_do_conv")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AIHub datasheet formater"))
        self.inputdir_btn.setText(_translate("Dialog", "input dir"))
        self.lable_cn_btn.setText(_translate("Dialog", "label cn"))
        self.lable_cnen_btn.setText(_translate("Dialog", "label cn2en"))
        self.outputdir_btn.setText(_translate("Dialog", "output dir"))
        self.label.setText(_translate("Dialog", "result"))
        self.action_do_conv.setText(_translate("Dialog", "start"))

