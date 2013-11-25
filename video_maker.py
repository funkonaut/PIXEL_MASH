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
mashstyle = int(raw_input("What mash style plese(1-diff,2-superimpose,3-invertblend,4-blend): ")) - 1
finalname = raw_input("What do you want your final movie name to be: ")
frames = rate * length + fmash
#do frame check make sure fmash
command = ("ffmpeg -i %(file)s -ss %(time)s -vframes %(frames)d -r %(rate)s pic%%05d.png"%({"file": fn, "time": time,"frames": frames ,"rate": frate}))
#experiment with video bit rate and qscale and what not...
#get final file name from user input and create log for variables.......
command2 = ("ffmpeg -r %d -i img%%05d.png %s" %(rate, finalname))
subprocess.call (shlex.split (command))

#Mash those frames and save em sequentially....
fns = [ImageChops.difference, \
       ImageChops.screen, \
       lambda x, y: ImageChops.blend (x, ImageChops.invert (y), .5), \
       lambda x, y: ImageChops.blend (x, y, .5)]

names = ["pic" + str (x).zfill (5) + ".png" for x in range (1, frames + 1)]
f_names = ["img" + str (x).zfill (5) + ".png" for x in range (0, frames)]
pngs = [Image.open (name) for name in names]

for x in range (0, frames):
    reduce (fns[mashstyle], pngs [x : x + fmash]).save (f_names[x])

#call video maker!
subprocess.call(shlex.split(command2))
#delete pics/manipuated images
for name in names + f_names:
    subprocess.call (['rm', name])
