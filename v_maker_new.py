import subprocess
import shlex
import sys
from PIL import Image, ImageChops
fn = raw_input("What is your file name, make sure its in the same folder you are in!: ")
fmash = int(raw_input("How many frames do you want to mash?: "))
frate = int(raw_input("What rate do you want to grab frames to mash at: "))
rate = int(raw_input("At what rate do you want your movie to play a (24 is a normal rate): "))
time = raw_input("What time in the movie would you like to start hh:mm:ss: ")
length = int(raw_input("How long do you want your video to be: "))
#mashstyle = int(raw_input("What mash style plese(1-diff,2-superimpose,3-invertblend,4-blend): "))
finalname = raw_input("What do you want your final movie name to be: ")
frames = rate*length+fmash
#do frame check make sure fmash
command = ("ffmpeg -i %s -ss %s -vframes %d -r %s pic%%05d.bmp"%(fn, time, frames, frate))
#command to make video from input files
#get final file name from user input and create log for variables.......
command2 = ("ffmpeg -qscale 1 -r %d -sameq -i img%%05d.bmp %s" %(rate,finalname))
#get frames
subprocess.call(shlex.split(command))
imglist = []
processed = []
for i in range(frames):
    if(not(i == 0)):
        im = Image.open("pic%05d.bmp"%(i))
        im = im.copy()
        imglist.append(im)
    
x = 0
i = 0
y = 0
for ims in imglist:
    try:
        im = processed[x]
        x += 1                                 #update for next processed image..
        im1 = imglist[x+1]     #make sure this is right and not off by 1
        im = ImageChops.difference(im,im1)
        processed.append(im)
    except:
        while(i<fmash):
            im1 = imglist[i]
            im = imglist[i+1]
            im = ImageChops.difference(im,im1)
            i+=1
            processed.append(im)
    im.save("img%05d.bmp"%y,"BMP")
    y += 1
subprocess.call(shlex.split(command2))
i=1
while(i<frames):
    command = (['rm', 'pic%05d.bmp'%i])
    try:
        subprocess.call(command)
    except:
        break
    i+=1
i=1
while(i<frames-1):
    command = (['rm', 'img%05d.bmp'%i])
    try:
        subprocess.call(command)
    except:
        break
    i += 1
sys.exit(0)
