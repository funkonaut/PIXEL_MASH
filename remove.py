import subprocess
fnum = int(raw_input("How many files do you want to delete:"))
fn = raw_input("what are your files named:")
i=1
while(i<fnum):
    command = (['rm', '%s%05d.bmp'%(fn,i)])
    try:
        subprocess.call(command)
    except:
        break
    i+=1
