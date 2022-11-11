"""
Convert the dataset from csv to yolo format
"""
import re
import os
import csv
import shutil

# cwd = os.getcwd()
# folder = '/dataset/'
# # files = ['/test.csv', '/train.csv']
# input_files = ['train.csv']

# image_x = 1280
# image_y = 720

# Read Annotations Part
def get_annotation_info(cwd, folder, input_files, image_x, image_y): 

    for file in input_files:
        dataset = []
        with open(cwd+folder+file, mode = 'r') as csvfile:
            data_reader = csv.reader(csvfile)
            for row in data_reader:
                data_dict = {}
                data_list = []
                video_id = row[0]
                image_id = row[4]
                annotations = row[5]
                numbers = re.findall(r'\d+', annotations)
                num_object = len(numbers) // 4
                for n in range (0,num_object):
                    data = {}
                    x_corner = int(numbers[0+4*n])
                    y_corner = int(numbers[1+4*n])
                    width = int(numbers[2+4*n]) / image_x
                    height = int(numbers[3+4*n]) / image_y
                    x_center = (x_corner + int(numbers[2+4*n])/2) / image_x
                    y_center = (y_corner + int(numbers[3+4*n])/2) / image_y
                    class_label = 'Starfish'
                    data.update({'class':class_label, 'x_center':x_center, 'y_center':y_center, 'width':width, 'height':height})
                    data_list.append(data)
                data_dict.update({'video_id':video_id, 'image_id':image_id, 'data_list':data_list})
                dataset.append(data_dict)
    csvfile.close()
    return dataset

# Select Annotations Part
def select_annotations(cwd, folder, dataset):

    for item in dataset:
        if not item['data_list']:
            continue
        output_file = open(cwd+folder+'yoloformat/'+item['image_id']+'.txt','w')
        for data in item['data_list']:
            write_line = data['class'] + ' ' + str(data['x_center']) + ' ' + str(data['y_center']) + ' ' + str(data['width']) + ' ' + str(data['height']) + '\n'
            output_file.writelines(write_line)
        output_file.close()
    print("Completed!")


# Select Images Part
def select_images(cwd, folder, dataset):
    dataset.pop(0) # pop out the tittle row
    for item in dataset:
        image_id = item['image_id']
        image_name = image_id + '.jpg'
        image_src_path = cwd + folder + 'images/'
        if not item['data_list']: # not exist starfish in annotation
            image_dst_path = cwd + folder + 'unselected_images/'
            image_src_path = image_src_path + image_name
            image_dst_path = image_dst_path + image_name
            image_src_path = r"{}".format(image_src_path)
            image_dst_path = r"{}".format(image_dst_path)
            shutil.copy(image_src_path, image_dst_path)
            print(image_name + ' is copied!')
        else: # exist starfish in annotation
            image_dst_path = cwd + folder + 'selected_images/'
            image_src_path = image_src_path + image_name
            image_dst_path = image_dst_path + image_name
            image_src_path = r"{}".format(image_src_path)
            image_dst_path = r"{}".format(image_dst_path)
            shutil.copy(image_src_path, image_dst_path)
            print(image_name + ' is copied!')
    print("Completed!")

