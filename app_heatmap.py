import csv
import sys
import time
import os
import pickle
from Individu import Individu

if __name__ == '__main__':

    if os.path.isdir("/scone/") :
        output_file="/scone/output_heatmap.csv"
    else:
        output_file="output_heatmap.csv"

    #   Find the dataset
    start_time = time.time()
    if 'IEXEC_DATASET_FILENAME' in os.environ:
        filename= "/iexec_in/tracks_heatmap.data"
    elif 'IEXEC_INPUT_FILE_NAME_1' in os.environ:
        filename= "/iexec_in/tracks_heatmap.data"
    else:
        filename= "tracks_heatmap.data"

    print ("Filename for dataset is " + filename)
    print ("output file is " + output_file)

    tracks= pickle.load(open(filename, 'rb'))

# generate heat map
    heatmap={}
    for i in tracks:
        if (i.status == 1):
            for (i,j) in i.geohashes:
                # better with get method?
                try:
                    heatmap[j] += 1
                except KeyError:
                    heatmap[j] = 1

    #Save the result in file for post processing function generating the kml file.
    w = csv.writer(open(output_file, "w"),delimiter= '\t')
    for key, val in heatmap.items():
        w.writerow([key.lower(), val])
    et = time.time() - start_time
    print('Total execution time: ' + str(et) + ' seconds\n')
