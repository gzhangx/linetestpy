import numpy as np

from PIL import Image

im = Image.open('../dove.jpg') # Can be many different formats.
#im.show()
pix = im.load()
print(im.size)  # Get the width and hight of the image for iterating over
#print(pix[x,y])  # Get the RGBA Value of the a pixel of an image
#pix[x,y] = value  # Set the RGBA Value of the image (tuple)

source = im.split()
(R,G,B)= (0,1,2)
mask = source[R].point(lambda i: i < 200 and 255)

for c in (0,1,2):
    out = source[c].point(lambda i: 0)
    source[c].paste(out, None, mask)
im = Image.merge(im.mode, source)
im.save('out.png')  # 

im = Image.open('out.png')
#im.show()

im = Image.open('out.bmp')
pix = im.load()
out = im.point(lambda x:0)

outpix = out.load()
(w,h) = im.size

links = np.full((int(w/2),int(h/2)),0)
start = (227,291)
for x in range(0,w):
  for y in range(0,h): 
     if pix[x,y] ==0:
         outpix[x,y] = 1


out.show() 