"""
Select annotated images from the original images
"""
import os
import preparation_lib

cwd = os.getcwd()
folder = '/dataset/'
# files = ['/test.csv', '/train.csv']
input_files = ['train.csv']

image_x = 1280
image_y = 720

dataset = preparation_lib.get_annotation_info(cwd, folder, input_files, image_x, image_y)

preparation_lib.select_images(cwd, folder, dataset)
