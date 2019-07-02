import argparse
import os
from glob import glob
from sklearn.model_selection import train_test_split


def split_to_train_test(anno_dir, train_file, test_file, split_ratio=0.3):
    # in case mistakenly delete. manually confirm
    if os.path.exists(train_file):
        print('this file already exists, please confirm!!', train_file)
        quit(1)
    if os.path.exists(test_file):
        print('this file already exists, please confirm!!', test_file)
        quit(1)

    f_train = open(train_file, 'w+')
    f_test = open(test_file, 'w+')

    print('anno_dir',anno_dir)
    total_files = glob(anno_dir + "*.xml")
    total_files = [file.replace('\\', '/') for file in total_files]
    total_files = [i.split("/")[-1].split(".xml")[0] for i in total_files]
    print('total_files',total_files)
    train_files, test_files = train_test_split(total_files, test_size=split_ratio, random_state=42)

    # train
    for file in train_files:
        f_train.write(file + "\n")
    # test
    for file in test_files:
        f_test.write(file + "\n")

    f_train.close()
    f_test.close()
    print("split Completed. Number of Train Samples: {}. Number of Test Samples: {}".format(len(train_files),
                                                                                            len(test_files)))

def split(voc_dir,test_ratio=0.3):
    print('split')
    args1={
    'voc_dir':voc_dir,
    'test_ratio':test_ratio,
    }
    from argparse import Namespace
    ns = Namespace(**args1)
    return split_main(ns)

def split_main(args):
#if __name__ == '__main__':
    #parser = argparse.ArgumentParser(
    #    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # voc root dir
    #parser.add_argument('voc_dir')
    # test ratio
    #parser.add_argument('test_ratio', default=0.3)
    #args = parser.parse_args()

    # VOC dataset root dir
    VOC_dir = args.voc_dir

    # default position
    annotationXmlDir = VOC_dir + "/Annotations/"

    # default position
    outputDir = VOC_dir + "/ImageSets/Main/"

    # two split image set file name e.g. train.txt and test.txt
    train_file = outputDir + "train.txt"
    test_file = outputDir + "test.txt"

    import os.path as osp
    if not osp.exists(outputDir):
        os.makedirs(outputDir)

    # split xml to two image set file
    split_to_train_test(annotationXmlDir, train_file, test_file, split_ratio=float(args.test_ratio))
