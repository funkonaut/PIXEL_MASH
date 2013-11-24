#Perhaps program it so it actually generates a video of the manipulated frames!
#
#
import subprocess
import shlex
import csv
from PIL import Image, ImageChops
f = open("file.csv","rb")
fh = csv.reader(f, delimiter=',')
for row in fh:
    fn= row[0]
    fmash= row[1]
    frate=row[2]
    rate=row[3]
    time=row[4]
    length=row[5]
    mashstyle=row[6]
    finalname=row[7]
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
    while(i<frames):
        command2 = (['rm', 'img%05d.png'%i])
        try:
            subprocess.call(command2)
        except:
            break
        i += 1
