#Perhaps program it so it actually generates a video of the manipulated frames!
#
#
import subprocess
import shlex
from PIL import Image, ImageChops

fn = raw_input("What is your file name, make sure its in the same folder you are in!: ")
fmash = int(raw_input("How many frames do you want to mash?: "))
frate = int(raw_input("What rate do you want to grab frames to mash at: "))
rate = int(raw_input("At what rate do you want your movie to play a (24 is a normal rate): "))
time = raw_input("What time in the movie would you like to start hh:mm:ss: ")
length = int(raw_input("How long do you want your video to be: "))
mashstyle = int(raw_input("What mash style plese(1-diff,2-superimpose,3-invertblend,4-blend): "))
finalname = raw_input("What do you want your final movie name to be: ")
frames = rate*length+fmash
#do frame check make sure fmash
command = ("ffmpeg -i %(file)s -ss %(time)s -vframes %(frames)d -r %(rate)s pic%%05d.png"%({"file": fn, "time": time,"frames": frames ,"rate": frate}))
#experiment with video bit rate and qscale and what not...
#get final file name from user input and create log for variables.......
command2 = ("ffmpeg -qscale 1 -r %d -sameq -i img%%05d.png %s" %(rate,finalname))
subprocess.call(shlex.split(command))
i = 1
x = 1
#
#Mash those frames and save em sequentially....
#
#
#
#
while(x<frames):
    while(i<fmash):
        if (not(i==1)):
            try:
                im1 = Image.open("pic%05d.png" %(i+x))
            except:
                break
         #experiment with different combinations perhaps
        # im1 = ImageChops.offset(5,0)
            if(mashstyle == 1):
                im = ImageChops.difference(im,im1)
            elif(mashstyle == 2):
                im = ImageChops.screen(im,im1)
            elif(mashstyle == 3):
                if((i & 1)== 1):               #makes sure that this works....
                    im = ImageChops.invert(im1)
                    im = ImageChops.blend(im,im1,.5)
                else:
                    im = ImageChops.blend(im,im1,.5)
            elif(mashstyle == 4):
                    im = ImageChops.blend(im,im1,.5)
        else:
            im=Image.open("pic%05d.png"%(i+x))
        i += 1
    if(not(x%(frames/4))):
        print ("you are %%d done")%((100*(x/frames)))
    im.save("img%05d.png"%x,"PNG")
    i = 1
    x += 1
#
#delete those frames after processing yo
i=1
while(i<frames):
    command = (['rm', 'pic%05d.png'%i]) 
    try:
        subprocess.call(command)
    except:
        break
    i+=1
#
#call video maker!
#
subprocess.call(shlex.split(command2))
#
#delete pics/manipuated images now... maybe include in other while loop?
#
i=1
while(i<frames-10):
    command2 = (['rm', 'img%05d.png'%i])
    try:
        subprocess.call(command2)
    except:
        break
    i += 1
