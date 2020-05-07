import csv
import sys
import time
import os
import pickle
from geohash2kml import KmlMaker
from Individu import Individu

if __name__ == '__main__':

    start_time = time.time()

    #   Find the dataset
    if os.path.isdir("/scone/") :
        input_file = "/iexec_in/tracks_heatmap.data"
        tmpfile = "/scone/tempfile.csv"
        output_root = "/scone/output_heatmap"
    else:
        input_file = "tracks_heatmap.data"
        tmpfile = "tempfile.csv"
        output_root = "output_heatmap"
    
    print ("Filename for dataset is " + input_file)
    print ("heatmap in csv format saved in " + tmpfile)
    print ("output file is " + output_root)

    tracks= pickle.load(open(input_file, 'rb'))

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

    #Save the intermediary file before the post processing function which generates the kml file.
    w = csv.writer(open(tmpfile, "w"), delimiter= '\t')
    for key, val in heatmap.items():
        w.writerow([key.lower(), val])

    kml = KmlMaker(tmpfile)
    kml.loadLocations()
    kml.simple_kml_output(output_filename=output_root + "_simple.kml")
    kml.advanced_kml_output(output_filename=output_root + ".kml", color_ramp=[2,5,8], polygon_height=5000)

    et = time.time() - start_time
    print('Total execution time: ' + str(et) + ' seconds\n')
