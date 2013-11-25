def get_params ():
    fn = raw_input("What is your file name, make sure its in the same folder you are in!: ")
    fmash = int(raw_input("How many frames do you want to mash?: "))
    frate = int(raw_input("What rate do you want to grab frames to mash at: "))
    rate = int(raw_input("At what rate do you want your movie to play a (24 is a normal rate): "))
    time = raw_input("What time in the movie would you like to start hh:mm:ss: ")
    length = int(raw_input("How long do you want your video to be: "))
    mashstyle = int(raw_input("What mash style plese(1-diff,2-superimpose,3-invertblend,4-blend): ")) - 1
    finalname = raw_input("What do you want your final movie name to be: ")
    return (fn, fmash, frate, rate, time, length, mashstyle, finalname)
