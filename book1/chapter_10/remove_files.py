import os
import glob

seperator = '\n#########\n'
image_path = '/Users/ross/projects/realpython/book1-exercises-src/Course materials/Chapter 10/Practice files/little pics'

def smaller_than(file_path, size):
    return os.path.getsize(file_path) < size

def is_jpg(file_path):
    return file_path.lower()[-3:] == 'jpg'

for current_folder, _, file_names in os.walk(image_path):
    for file_name in file_names:
        full_file_name = os.path.join(image_path, current_folder, file_name)
        if smaller_than(full_file_name, 2000) and is_jpg(full_file_name):
            print "To be deleted: {}".format(full_file_name)
        else:
            print "Will not be deleted: {}".format(full_file_name)
            
