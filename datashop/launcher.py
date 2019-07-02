

from PyQt5 import QtWidgets, QtGui
import sys


from .launcher_ui_concrate import Ui_Dialog_launcher


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
    task_config=list()
    
    #task_config.append('bbox_l2v')
    #task_config.append('sem_l2v')
    #task_config.append('split')
    #task_config.append('voc2coco')
    task_config.append('labelme2coco')

    try:
        #import thread
        #thread.start_new_thread( sem_l2v, (args) )
        if 'bbox_l2v' in task_config:
            from bbox_labelme2voc import bbox_l2v
            #r=bbox_l2v(args)
            uiobj.log('bbox_labelme2voc success')

        if 'sem_l2v' in task_config:
            from .semantic_labelme2voc import sem_l2v
            r=sem_l2v(args)
            uiobj.log('sem_l2v success')

        if 'split' in task_config:
            from .split_dataset import split
            r=split(args[3],0.2)
            uiobj.log('split success')
        
        if 'voc2coco' in task_config:
            from .voc_xml2coco_json import voc2coco
            #def voc2coco(imgset_file,anno_dir,outputjson_file):
            imgset_file=args[3]+'/ImageSets/Main/train.txt'
            anno_dir=args[3]+'/Annotations/'
            outputjson_file=args[3]+'coco_out.json'
            r=voc2coco(imgset_file,anno_dir,outputjson_file)
            uiobj.log('voc2coco success')

        if 'labelme2coco' in task_config:
            from .labelme2coco import labelme2coco_main
#def labelme2coco_main(labelme_classname_to_id_file,input_labelme_data_dir,output_coco_data_dir):
            labelme_classname_to_id_file=args[0]
            input_labelme_data_dir=args[2]
            output_coco_data_dir=args[3]
            r=labelme2coco_main(labelme_classname_to_id_file,input_labelme_data_dir,output_coco_data_dir)
            uiobj.log('labelme2coco success')

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