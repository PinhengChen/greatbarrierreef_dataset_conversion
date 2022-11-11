import os
import re

cwd = os.getcwd()
folder_list = ['/dataset/train_images/video_0/', 
               '/dataset/train_images/video_1/', 
               '/dataset/train_images/video_2/']

# Rename Images
for folder in folder_list:
    for filename in os.listdir(cwd + folder):
        old_name = cwd + folder + filename
        numbers = re.findall(r'\d+', old_name)
        new_name = numbers[1] + '-' + numbers[2] + ".jpg"
        new_name = cwd + folder + new_name
        os.rename(old_name, new_name)

