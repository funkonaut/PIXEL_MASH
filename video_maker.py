import subprocess
import shlex
from PIL import Image, ImageChops
from vm_input import get_params
from cache import retrieve

(fn, fmash, frate, rate, time, length, mashstyle, finalname) = get_params ()
frames = rate * length + fmash

command = ("ffmpeg -i %(file)s -ss %(time)s -vframes %(frames)d -r %(rate)s pic%%05d.png"%({"file": fn, "time": time,"frames": frames ,"rate": frate}))
command2 = ("ffmpeg -r %d -i img%%05d.png %s" %(rate, finalname))

subprocess.call (shlex.split (command))

#Mash those frames and save em sequentially....
fns = [ImageChops.difference, \
       ImageChops.screen, \
       lambda x, y: ImageChops.blend (x, ImageChops.invert (y), .5), \
       lambda x, y: ImageChops.blend (x, y, .5)]

names = ["pic" + str (x).zfill (5) + ".png" for x in range (1, frames + 1)]
f_names = ["img" + str (x).zfill (5) + ".png" for x in range (0, frames)]

for x in range (0, frames):
    reduce (fns[mashstyle], map (retrieve, names [x : x + fmash])).save (f_names[x])

#call video maker!
subprocess.call(shlex.split(command2))
#delete pics/manipuated images
for name in names + f_names:
    subprocess.call (['rm', name])
