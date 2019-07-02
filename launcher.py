

from PyQt5 import QtWidgets, QtGui
import sys


from launcher_ui_concrate import Ui_Dialog_launcher


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog_launcher()

    ui.setupUi(MainWindow)
    ui.register_action_do_conv_hanler(action_do_conv_hanler)

    MainWindow.show()
    sys.exit(app.exec_()) 

def action_do_conv_hanler(uiobj,*args):
    print('action_do_conv_hanler')
    print(args)
    from semantic_labelme2voc import sem_l2v
    try:
        r=sem_l2v(args)
        uiobj.log('sem_l2v success')
    except Exception as e:
        uiobj.log('sem_l2v failed')
        print(e)
        import traceback
        info = traceback.format_exc()
        print(info)
    #lable_cn_pathstr
#lable_cnen_pathstr
#inputdir_pathstr
#outputdir_pathstr


if __name__ == '__main__': 
    main()