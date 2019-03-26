from xml.etree import ElementTree as ET
import json

'''
copy and paste from http://effbot.org/zone/element-lib.htm#prettyprint
it basically walks your tree and adds spaces and newlines so the tree is
printed in a nice way
'''
def pretty_print(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            pretty_print(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def build_pascal_voc_formart(pascal_voc_data):
    try:
        '''It the structure is correct procced further'''
        pascal_voc_data = json.loads(pascal_voc_data)
        if len(pascal_voc_data):
            for each_pascal_voc in pascal_voc_data:
                get_folder = each_pascal_voc['folder']
                get_filename = each_pascal_voc['filename']
                get_path = each_pascal_voc['path']
                get_database = each_pascal_voc['source']['database']
                get_width = each_pascal_voc['size']['width']
                get_height = each_pascal_voc['size']['height']
                get_depth = each_pascal_voc['size']['depth']
                get_segmented = each_pascal_voc['segmented']
                get_object = each_pascal_voc['objects']
                try:
                    result = create_pascal_voc_file(get_folder, get_filename, get_path, get_database, get_width,get_height,get_depth, get_segmented, get_object)
                    if result:
                        print("xml file created for {} file", get_filename)
                    else:
                        print("Problem while creating xml file created for {} ", get_filename)
                except:
                    print("Problem while creating pascal voc file")


    except:
        print("Problem while reading the pascal voc data")


def create_pascal_voc_file(get_folder, get_filename, get_path, get_database, get_width,get_height,get_depth, get_segmented, get_object):
    try:
        '''Getting the basic details like folder, filename and path'''
        voc_xml = ET.Element("annotation")
        folder = ET.SubElement(voc_xml, "folder")
        folder.text = str(get_folder)
        filename = ET.SubElement(voc_xml, "filename")
        filename.text = str(get_filename)
        path = ET.SubElement(voc_xml, "path")
        path.text = str(get_path)
        source = ET.SubElement(voc_xml, "source")
        database = ET.SubElement(source, "database")
        database.text = str(get_database)
        '''Getting the image properties of width, height, depth'''
        size = ET.SubElement(voc_xml, "size")
        width = ET.SubElement(size, "width")
        width.text = str(get_height)
        height = ET.SubElement(size, "height")
        height.text = str(get_width)
        depth = ET.SubElement(size, "depth")
        depth.text = str(get_depth)
        segmented = ET.SubElement(voc_xml, "segmented")
        segmented.text = str(get_segmented)
        for each_object in get_object:
            '''Loop through each object'''
            object = ET.SubElement(voc_xml, "object")
            name = ET.SubElement(object, "name")
            name.text = str(each_object["name"])
            pose = ET.SubElement(object, "pose")
            pose.text = str(each_object["pose"])
            truncated = ET.SubElement(object, "truncated")
            truncated.text = str(each_object["truncated"])
            occluded = ET.SubElement(object, "occluded")
            occluded.text = str(each_object["occluded"])
            bndbox = ET.SubElement(object, "bndbox")
            xmin = ET.SubElement(bndbox, "xmin")
            xmin.text = str(each_object["bndbox"]["xmin"])
            xmax = ET.SubElement(bndbox, "ymin")
            xmax.text = str(each_object["bndbox"]["ymin"])
            ymin = ET.SubElement(bndbox, "xmax")
            ymin.text = str(each_object["bndbox"]["xmax"])
            ymax = ET.SubElement(bndbox, "ymax")
            ymax.text = str(each_object["bndbox"]["ymax"])

        '''Make the xml pretty look'''
        pretty_print(voc_xml)
        '''Tree xml '''
        tree = ET.ElementTree(voc_xml)
        try:
            '''Write to xml file'''
            get_xml_file_name = get_filename.split('.')[0]
        except:
            print("Please cross check your filename should be like image.png, image.jpg, image_165151.jpeg")
        tree.write(get_xml_file_name + ".xml", xml_declaration=False, encoding='utf-8', method="xml")
        return True
    except:
        '''Problem while creating xml file'''
        return  False

