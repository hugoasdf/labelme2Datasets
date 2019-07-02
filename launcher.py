

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
    
    try:
        #import thread
        #thread.start_new_thread( sem_l2v, (args) )

        from bbox_labelme2voc import bbox_l2v
        #r=bbox_l2v(args)
        uiobj.log('bbox_labelme2voc success')

        from semantic_labelme2voc import sem_l2v
        #r=sem_l2v(args)
        uiobj.log('sem_l2v success')


        from split_dataset import split
        #r=split(args[3],0.2)
        uiobj.log('split success')
        
        from voc_xml2coco_json import voc2coco
        #def voc2coco(imgset_file,anno_dir,outputjson_file):
        imgset_file=args[3]+'/ImageSets/Main/train.txt'
        anno_dir=args[3]+'/Annotations/'
        outputjson_file='coco_out.json'
        r=voc2coco(imgset_file,anno_dir,outputjson_file)
        uiobj.log('voc2coco success')

    except Exception as e:
        uiobj.log('failed')
        #print(e)
        import traceback
        info = traceback.format_exc()
        print(info)
    #lable_cn_pathstr
#lable_cnen_pathstr
#inputdir_pathstr
#outputdir_pathstr


if __name__ == '__main__': 
    main()