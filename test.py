#Perhaps program it so it actually generates a video of the manipulated frames!
#
#
import subprocess
import shlex
rate=2
command2 = ("ffmpeg -qscale 2 -r %d -b 20,000 -i img%04d.png movie.mp4" %(rate))
subprocess.call(shlex.split(command2))
