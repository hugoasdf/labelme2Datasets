# VOC转COCO
import argparse
import os
import xmltodict
import json
from collections import OrderedDict


def voc_xml2coco_json(root_dir, xml_files, json_file):
    """
    将VOC格式的XML转换为COCO格式的JSON
    :param root_dir: voc dataset annotation dir, usually 'Annotations'
    :param xml_files: xml list need to convert
    :param json_file: output json file name
    :return:
    """
    attr_dict = dict()
    # categories info
    # (add manually for now. If label num is large, you can write a script to generate this with class_names.txt)
    attr_dict["categories"] = [{"supercategory": "defect", "id": 1, "name": "BuDaoDian"},
                               {"supercategory": "defect", "id": 2, "name": "CaHua"},
                               {"supercategory": "defect", "id": 3, "name": "JiaoWeiLouDi"},
                               {"supercategory": "defect", "id": 4, "name": "JuPi"},
                               {"supercategory": "defect", "id": 5, "name": "LouDi"},
                               {"supercategory": "defect", "id": 6, "name": "PengLiu"},
                               {"supercategory": "defect", "id": 7, "name": "QiPao"},
                               {"supercategory": "defect", "id": 8, "name": "QiKeng"},
                               {"supercategory": "defect", "id": 9, "name": "ZaSe"},
                               {"supercategory": "defect", "id": 10, "name": "ZangDian"}]
    # image list
    images = list()
    # annotation list
    annotations = list()
    for root, dirs, files in os.walk(root_dir):
        image_id = 0
        for file in xml_files:
            image_id = image_id + 1  # define image id by plus 1, in case of duplicate
            if file in files:
                # xml path
                annotation_path = os.path.abspath(os.path.join(root, file))
                # image info
                image = dict()
                # read xml info
                doc = xmltodict.parse(open(annotation_path).read())
                image['file_name'] = str(doc['annotation']['filename'])
                image['height'] = int(doc['annotation']['size']['height'])
                image['width'] = int(doc['annotation']['size']['width'])
                image['id'] = image_id
                # use this when use oversampling
                # if file[0] == 'n':
                #     image['file_name'] = 'n_' + str(doc['annotation']['filename'])

                images.append(image)
                print("File Name: {} and image_id {}".format(file, image_id))

                # annotation ID
                id1 = 1
                if 'object' in doc['annotation']:
                    objects = doc['annotation']['object']
                    if isinstance(objects, OrderedDict):
                        obj = objects
                        objects = list()
                        objects.append(obj)

                    for obj in objects:
                        for value in attr_dict["categories"]:
                            annotation = dict()
                            if str(obj['name']) == value["name"]:
                                # annotation["segmentation"] = []
                                annotation["iscrowd"] = 0
                                annotation["image_id"] = image_id
                                x = int(obj["bndbox"]["xmin"])
                                y = int(obj["bndbox"]["ymin"])
                                w = int(obj["bndbox"]["xmax"]) - x + 1
                                h = int(obj["bndbox"]["ymax"]) - y + 1
                                annotation["bbox"] = [x, y, w, h]
                                annotation["area"] = float(w * h)
                                annotation["category_id"] = value["id"]
                                annotation["ignore"] = 0
                                annotation["segmentation"] = [
                                    [x, y, x, (y + h - 1), (x + w - 1), (y + h - 1), (x + w - 1), y]]
                                annotation["id"] = id1
                                id1 += 1

                                annotations.append(annotation)
                else:
                    print("File: {} doesn't have any object".format(file))
            else:
                print("File: {} not found".format(file))
    # COCO images part
    attr_dict["images"] = images
    # COCO annotations part
    attr_dict["annotations"] = annotations
    # COCO type part
    attr_dict["type"] = "instances"

    # convert dict to json format
    json_string = json.dumps(attr_dict)

    # save to file
    with open(json_file, "w") as f:
        f.write(json_string)
    print("Completed. ")

def voc2coco(imgset_file,anno_dir,outputjson_file):
    print('sem_l2v')
    args1={
    'imgset_file':imgset_file,
    'anno_dir':anno_dir,
    'json_file':outputjson_file}
    from argparse import Namespace
    ns = Namespace(**args1)
    return voc2coco_main(ns)

def voc2coco_main(args):
#if __name__ == '__main__':
    #parser = argparse.ArgumentParser(
    #    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # voc image-set file
    #parser.add_argument('imgset_file', help='voc image set to convert')
    # directory where contains labelme annotated json files
    #parser.add_argument('anno_dir', help='voc dataset annotations directory')
    # output directory for dataset
    #parser.add_argument('json_file', help='output coco json file')
    #args = parser.parse_args()

    # get xml list
    xml_list = list()
    with open(args.imgset_file, "r", encoding='UTF-8') as f:
        for line in f:
            fileName = line.strip()
            print(fileName)
            print(fileName)
            xml_list.append(fileName + ".xml")
    # auto-remove file when it exist
    if os.path.exists(args.json_file):
        os.remove(args.json_file)

    # begin convert
    voc_xml2coco_json(args.anno_dir, xml_list, args.json_file)
