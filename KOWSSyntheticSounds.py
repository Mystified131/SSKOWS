#This code imports the necessary modules.

import random
import os
from collections import defaultdict
import datetime
import shutil
from RandFunct import random_number
from RandFunct2 import random_number2

#this code retrieves the date and time from the computer, to create the timestamp

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

timer = ("".join(list))
   

#srchstr = "C:\\Users\\mysti\\Media_Files\\Sounds\\OlderSounds"

srchstr = 'G:\\OriginalAudio\\Songs'

contentdat = {}

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".wav") :

            tim = os.path.getmtime(filepath)

            contentdat[filepath] = tim

newply = []

newplyd = []

for w in sorted(contentdat, key=contentdat.get, reverse=False):
    newply.append(w)
    newplyd.append(contentdat[w])

totlen = len(newply)

totch = random_number(totlen)

fitch = newply[totch]

fich = str(newplyd[totch])

finlst = []

for ctr in range(30):
 
    sublst = []

    for elem in range(totlen):
        tesstr = newply[elem]
        testr = str(newplyd[elem])
        piv2str = testr[-10:-8]

        if piv2str in fich:
            sublst.append(tesstr)

    if len(sublst) > 1:   

        subl = len(sublst)    

        trok = random_number(subl) 

        fich = sublst[trok]

        finlst.append(fich)

    if len(sublst) <= 1:

        totch = random_number(totlen)

        fich = newply[totch]

        finlst.append(fich)

ctr = len(finlst)

playlst = []

for x in range(ctr):
    print("")
    print("Copying")
    elem = finlst[x]
    playlst.append(elem)
    outstr = 'C:\\Users\\mysti\\Coding\\SSKOWS\\Audio\\radiotrack' + str((x + 1)/100) + '.wav'
    shutil.copy(elem, outstr)

print("")
print(playlst)

oustr = "KOWS_Sample_Playlist_" + timer + ".txt"

outfile = open(oustr, "w")

for elem in playlst:
    outfile.write(elem + '\n')

outfile.close()
        
## THE GHOST OF THE SHADOW ##
