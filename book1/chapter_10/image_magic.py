import os
import glob

seperator = '\n#########\n'
image_path = '/Users/ross/projects/realpython/book1-exercises-src/Course materials/Chapter 10/Practice files/images'

for file_name in os.listdir(image_path):
    print "{}".format(os.path.join(image_path, file_name))

print seperator 

pngs = os.path.join(image_path, '*.png')
for png in glob.glob(pngs):
    print "{}".format(os.path.join(image_path, png))

print seperator 

for current_folder, _, _ in os.walk(image_path):
    pngs = os.path.join(current_folder, '*.jpg')
    for png in glob.glob(pngs):
        print "{}".format(os.path.join(image_path, png))

print seperator 

for current_folder, subfolders, file_names in os.walk(image_path):
    pngs = os.path.join(current_folder, '*.png')
    for png in glob.glob(pngs):
        jpg_name = png[0:len(png)-4] + ".jpg"
        print jpg_name
        os.rename(png, jpg_name)
        print os.path.exists(jpg_name)

print seperator 

for current_folder, _, _ in os.walk(image_path):
    pngs = os.path.join(current_folder, '*.jpg')
    for png in glob.glob(pngs):
        print "{}".format(os.path.join(image_path, png))
