from launcher_ui import Ui_Dialog
from PyQt5.QtWidgets import QFileDialog
from pathlib import Path

class Ui_Dialog_launcher(Ui_Dialog):
 
    def __init__(self):
        super(Ui_Dialog,self).__init__()
        self.state={}
        self.state['lable_cn_pathstr']=""
        self.state['lable_cnen_pathstr']=""
        self.state['inputdir_pathstr']=""
        self.state['outputdir_pathstr']=""

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        #print(dir(super()))
        #print(super().lable_cn_btn)
        self.lable_cn_btn.clicked.connect(self.on_push_button_1_clicked)
        self.lable_cnen_btn.clicked.connect(self.on_push_button_2_clicked)
        self.inputdir_btn.clicked.connect(self.on_push_button_3_clicked)
        self.outputdir_btn.clicked.connect(self.on_push_button_4_clicked)
        self.action_do_conv.clicked.connect(self.on_push_button_5_clicked)
        try:
            import pickle
            f=open('statesave','rb')
            self.state=pickle.load(f)
            self.state_to_ui()
        except IOError:
            pass

    def on_push_button_1_clicked(self):
        init_dir_path=self.state['lable_cn_pathstr']
        if not Path(init_dir_path).exists():
            init_dir_path= "\\"
        dir_path,filetype=QFileDialog.getOpenFileName(self.lable_cn_btn,"choose lable_cn_btn",
            init_dir_path,"All Files (*);;Text Files (*.txt)") 
        stra=dir_path#.toUtf8()#unicode(dir_path.toUtf8(), 'utf-8', 'ignore')
        self.state['lable_cn_pathstr']=stra
        self.state_to_ui()


    def on_push_button_2_clicked(self):
        init_dir_path=self.state['lable_cnen_pathstr']
        if not Path(init_dir_path).exists():
            init_dir_path= "\\"
        dir_path,filetype=QFileDialog.getOpenFileName(self.lable_cn_btn,"choose lable_cn_btn",
            init_dir_path,"All Files (*);;Text Files (*.txt)") 
        stra=dir_path#.toUtf8()#unicode(dir_path.toUtf8(), 'utf-8', 'ignore')
        self.state['lable_cnen_pathstr']=stra
        self.state_to_ui()

    def on_push_button_3_clicked(self):
        init_dir_path=self.state['inputdir_pathstr']
        if not Path(init_dir_path).exists():
            init_dir_path= "\\"
        dir_path=QFileDialog.getExistingDirectory(self.lable_cn_btn,"choose lable_cn_btn",init_dir_path)
        stra=dir_path#.toUtf8()#unicode(dir_path.toUtf8(), 'utf-8', 'ignore')
        self.state['inputdir_pathstr']=stra
        self.state_to_ui()

 
    def on_push_button_4_clicked(self):
        init_dir_path=self.state['outputdir_pathstr']
        if not Path(init_dir_path).exists():
            init_dir_path= "\\"
        dir_path=QFileDialog.getExistingDirectory(self.lable_cn_btn,"choose lable_cn_btn",init_dir_path)
        stra=dir_path#.toUtf8()#unicode(dir_path.toUtf8(), 'utf-8', 'ignore')
        self.state['outputdir_pathstr']=stra
        self.state_to_ui()

    def state_to_ui(self):
        self.lable_cn_textview.setText(self.state['lable_cn_pathstr'])
        self.lable_cnen_textview.setText(self.state['lable_cnen_pathstr'])
        self.inputdir_textview.setText(self.state['inputdir_pathstr'])
        self.outputdir_textview.setText(self.state['outputdir_pathstr'])

    def on_push_button_5_clicked(self):
        self.log("start convert")

        import threading
        t= threading.Thread(target=self.conv_hanler,args=(self,
        self.state['lable_cn_pathstr'],
        self.state['lable_cnen_pathstr'],
        self.state['inputdir_pathstr'],
        self.state['outputdir_pathstr']) )
        t.setDaemon(True)
        t.start()


        self.log("end convert")
        pass

    def register_action_do_conv_hanler(self,conv_hanler):
        self.conv_hanler=conv_hanler
        pass



    def log(self,stra):
        import time
        nowstr=time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime())
        self.result_out_textview.appendPlainText(nowstr+stra)
        pass

    def __del__(self):
        import pickle
        f=open('statesave','wb')  
        pickle.dump(self.state,f)  
        f.close()  