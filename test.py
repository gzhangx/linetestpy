import numpy as np

from PIL import Image

import matplotlib.cbook as cbook
import matplotlib.image as image
import matplotlib.pyplot as plt

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

linksLoc = np.full((int(w/2),int(h/2),2),(0,0))

RESOLUTION = 10

def toLinnkPos(cur):
    (x,y) = cur
    fx = int(x/RESOLUTION)
    fy = int(y/RESOLUTION)
    return (fx, fy)

def toLinkLoc(pix, pos, size):
    (x,y) = pos
    (w,h) = size
    movemax=5
    upper = y
    lower = y
    m = 0
    while upper >=0:
        if pix[x,upper] != 0:
            break
        m = m + 1
        if m >= movemax:
             break
        upper=upper - 1

    m = 0
    while lower < h:
        if pix[x,lower] != 0:
            break
        m = m + 1
        if m >= movemax:
         break
        lower = lower + 1

    return (x, int((upper + lower)/2))
    

start = (227,291)


for x in range(0,w):
  for y in range(0,h): 
     if pix[x,y] ==0:
         (fx, fy) = toLinnkPos((x,y))
         if (links[fx,fy] == 0):             
             linksLoc = toLinkLoc(pix, (x,y), (w,h))
             links[fx,fy] = 1
             outpix[linksLoc[0],linksLoc[1]] = 1
             if (x >= 360 and y >= 238 and x <= 361 and y <=240):
                     print("x=%d y=%d (%d,%d) links %d" % (x,y , fx, fy,links[fx,fy]))
                     print("upper %d lower %d" % (linksLoc[0],linksLoc[1]))


#out.show() 
out.save('out.png')  # 
fig, ax = plt.subplots()

ax.plot([[0,0],[1,1]], '-o', ms=1, alpha=0.7, mfc='orange')
ax.grid()
fig.figimage(out, 10, 10, zorder=3, alpha=.5)

plt.show()