#Perhaps program it so it actually generates a video of the manipulated frames!
#
#
import subprocess
import shlex
from PIL import Image, ImageChops
fn = raw_input("What is your file name(make sure its in the same folder you are!): ")
frames = int(raw_input("How many frames please (more than 1): "))
rate = raw_input("At what rate(1 is 1frame/sec 1/60 is 1frame/min): ")
time = raw_input("What time in the movie would you like to start hh:mm:ss: ")
command = ("ffmpeg -i %(file)s -ss %(time)s -vframes %(frames)d -r %(rate)s anniepic%%03d.png"%({"file": fn, "time": time,"frames": frames ,"rate": rate}))
subprocess.call(shlex.split(command))
i = 1
#change for support of adding more frames...
while(i<frames):
    if (not(i==1)):
        im1 = Image.open("anniepic%03d.png" %(i))
#not really combining all the images together make it so they all show through equally so the final image is not the one most apparent in the final image    
       # im1 = ImageChops.offset(5,0)
        im = ImageChops.difference(im,im1)
    else:
        im=Image.open("anniepic001.png")
#figure out how to delete image after using
    i+=1
im.save("final","PNG")
i = 1
#delete pics now... maybe include in other while loop?
while(i<=frames):
    command = (['rm', 'anniepic%03d.png'%i]) 
    subprocess.call(command)
    i+=1
