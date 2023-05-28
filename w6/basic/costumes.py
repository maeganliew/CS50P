import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)    #image files are cl arguments
    images.append(image)   #add opened image to the "images" list


#costumes.gif is the output file, save_all to save all frames passsed through
#append_image is to add another image after images[0] to create a "moving" motion
#duration set to 200 milliseconds, time=0 means continue for infinite number of time
images[0].save (
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, time=0
)

