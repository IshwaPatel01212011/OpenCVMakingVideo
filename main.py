import os
import cv2
from PIL import Image

print(os.getcwd())
path = "Lesson 6/images"
dir = os.getcwd()
path = dir + '/' + path 

# change directory 
os.chdir(path)
print(os.getcwd())
images = os.listdir('.')
print(images)
mean_width = 0 
mean_height = 0 
number_of_images = len(images)
sum_w = 0
sum_h = 0 

for i in images:
    if i.endswith('.jpg'):
        img = Image.open(os.path.join(path,i))
        w,h = img.size
        sum_w  += w
        sum_h += h

mean_width = sum_w//number_of_images
mean_height = sum_h//number_of_images

for image in images:
    if image.endswith('.jpg'):
        img = Image.open(path +'/'+ image)
        imgResize = img.resize((mean_width, mean_height))
        imgResize.save(image,'JPEG', quality = 95)

video_name = "scenery.avi"
frame = cv2.imread(os.path.join(path,images[0]))
video = cv2.VideoWriter(video_name, 0, 0.5, (mean_width,mean_height))
for image in images:
    video.write(cv2.imread(os.path.join(path,image)))
video.release()