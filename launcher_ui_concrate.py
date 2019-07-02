from launcher_ui import Ui_Dialog
from PyQt5.QtWidgets import QFileDialog

class Ui_Dialog_launcher(Ui_Dialog):
 
    def __init__(self):
        super(Ui_Dialog,self).__init__()
        self.lable_cn_pathstr=""
        self.lable_cnen_pathstr=""
        self.inputdir_pathstr=""
        self.outputdir_pathstr=""

        """
        self.inputdir_btn.setFont(font)
        self.inputdir_btn.setStyleSheet("background-color:rgb(255, 127, 127)")
        self.inputdir_btn.setObjectName("inputdir_btn")
        self.inputdir_textview = QtWidgets.QLineEdit(Dialog)
        self.inputdir_textview.setGeometry(QtCore.QRect(10, 160, 461, 20))
        self.inputdir_textview.setStyleSheet("background-color:rgb(255, 127, 127)")
        self.inputdir_textview.setObjectName("inputdir_textview")
        self.lable_cn_btn = QtWidgets.QPushButton(Dialog)
        self.lable_cn_btn.setGeometry(QtCore.QRect(10, 20, 101, 71))
        """
    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        #print(dir(super()))
        #print(super().lable_cn_btn)
        self.lable_cn_btn.clicked.connect(self.on_push_button_1_clicked)
        self.lable_cnen_btn.clicked.connect(self.on_push_button_2_clicked)
        self.inputdir_btn.clicked.connect(self.on_push_button_3_clicked)
        self.outputdir_btn.clicked.connect(self.on_push_button_4_clicked)
        self.action_do_conv.clicked.connect(self.on_push_button_5_clicked)

    def on_push_button_1_clicked(self):
        dir_path=QFileDialog.getExistingDirectory(self.lable_cn_btn,"choose lable_cn_btn","\\")
        stra=dir_path#.toUtf8()#unicode(dir_path.toUtf8(), 'utf-8', 'ignore')
        self.lable_cn_pathstr=stra
        self.lable_cn_textview.setText(stra)

    def on_push_button_2_clicked(self):
        dir_path=QFileDialog.getExistingDirectory(self.lable_cn_btn,"choose lable_cn_btn","\\")
        stra=dir_path#.toUtf8()#unicode(dir_path.toUtf8(), 'utf-8', 'ignore')
        self.lable_cnen_pathstr=stra
        self.lable_cnen_textview.setText(stra)

    def on_push_button_3_clicked(self):
        dir_path=QFileDialog.getExistingDirectory(self.lable_cn_btn,"choose lable_cn_btn","\\")
        stra=dir_path#.toUtf8()#unicode(dir_path.toUtf8(), 'utf-8', 'ignore')
        self.inputdir_pathstr=stra
        self.inputdir_textview.setText(stra)

 
    def on_push_button_4_clicked(self):
        dir_path=QFileDialog.getExistingDirectory(self.lable_cn_btn,"choose lable_cn_btn","\\")
        stra=dir_path#.toUtf8()#unicode(dir_path.toUtf8(), 'utf-8', 'ignore')
        self.outputdir_pathstr=stra
        self.outputdir_textview.setText(stra)

    def on_push_button_5_clicked(self):

        self.conv_hanler(self,
        self.lable_cn_pathstr,
        self.lable_cnen_pathstr,
        self.inputdir_pathstr,
        self.outputdir_pathstr)
        pass

    def register_action_do_conv_hanler(self,conv_hanler):
        self.conv_hanler=conv_hanler
        pass

    def log(self,stra):
        import time
        nowstr=time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime())
        self.result_out_textview.appendPlainText(nowstr+stra)
        pass