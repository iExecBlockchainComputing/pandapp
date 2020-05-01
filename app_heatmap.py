import Geohash
import math
import argparse
import csv
import sys
import time
import os
import pickle

class Individu():
    def __init__(self, _status, _timestamp, _geohashes):
        self.status = _status
        self.timestamp = _timestamp
        self.geohashes = _geohashes

    def __str__(self):
        return "[status %s | timestamp %s] %s" % (self.status, self.timestamp, self.geohashes)

if __name__ == '__main__':


    if os.path.isdir("/scone/") :
        output_file="/scone/heatmap.csv"
    else:
        output_file="heatmap.csv"

    #   Find the dataset
    start_time = time.time()
    if 'IEXEC_DATASET_FILENAME' in os.environ:
        filename="/iexec_in/"+ os.environ['IEXEC_DATASET_FILENAME']
    elif 'IEXEC_INPUT_FILE_NAME_1' in os.environ:
        print(os.environ['IEXEC_INPUT_FILE_NAME_1'])
        filename="/iexec_in/" + os.environ['IEXEC_INPUT_FILE_NAME_1']
    else:
        filename=sys.argv[1]

    print ("Filename for dataset is " + filename)
    print ("output file is " + output_file)

    lists= pickle.load(open(filename, 'rb'))

# generate heat map
    heatmap={}
    for i in lists:
        if (i.status == 1):
            for j in i.geohashes:
                # better with get method?
                try:
                    heatmap[j] += 1
                except KeyError:
                    heatmap[j] = 1

    #Save the result in file for post processing function generating the kml file.
    w = csv.writer(open(output_file, "w"),delimiter= '\t')
    for key, val in heatmap.items():
        w.writerow([key, val])
    et = time.time() - start_time
    print('Total execution time: ' + str(et) + ' seconds\n')
