import sys
import time
import os
import pickle
from Individu import Individu

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print ("Usage: python app_socialdistance.py hash")
        sys.exit(-1)

    hashid=int(sys.argv[1])

    start_time = time.time()

#   Find the dataset
    if os.path.isdir("/scone/") :
        filename= "/iexec_in/tracks_socialdistance.data"
    else:
        filename= "tracks_socialdistance.data"

    print ("Filename for dataset is " + filename)

    tracks= pickle.load(open(filename, 'rb'))

    #  Find with the hash in input; not implemented used id for the moment

    target = tracks[hashid]
#    print("target ", target)

    tracks.remove(target)
    for track in tracks:
        print(track)

    print("target ", target)
    meet_safe=0
    meet_ill=0
    for (t, point) in target.geohashes:
        print ("target ", t, point)
        for tr in tracks:
           if (t,point) in tr.geohashes:
               if tr.status == 0:
                   meet_safe +=1
               else:
                   meet_ill +=1
    print("*************RESULT***************")
    print(" you have met ", meet_ill, " person(s) declared ill")
    print(" and ", meet_safe,  " person(s) not declared")

    et = time.time() - start_time
    print('Total execution time: ' + str(et) + ' seconds\n')
