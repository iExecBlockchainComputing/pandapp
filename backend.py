import Geohash
import georaptor
import math
import time
import argparse
import csv
from clint.textui import puts, indent, colored


def in_circle_check(latitude, longitude, centre_lat, centre_lon, radius):

    x_diff = longitude - centre_lon
    y_diff = latitude - centre_lat

    if (math.pow(x_diff, 2) + math.pow(y_diff, 2) <= math.pow(radius, 2)):
        return True

    return False


def get_centroid(latitude, longitude, height, width):

    y_cen = latitude + (height / 2)
    x_cen = longitude + (width / 2)

    return (x_cen, y_cen)


def convert_to_latlon(y, x, latitude, longitude):

    pi = 3.14159265359

    r_earth = 6371000

    lat_diff = (y / r_earth) * (180 / pi)
    lon_diff = (x / r_earth) * (180 / pi) / math.cos(latitude * pi/180)

    final_lat = latitude+lat_diff
    final_lon = longitude+lon_diff

    return (final_lat, final_lon)

def unique(list1):

    # intilize a null list
    unique_list = []
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return(unique_list)

def create_circle_geohash(latitude, longitude, radius, precision, georaptor_flag=False, minlevel=1, maxlevel=12):

    x = 0.0
    y = 0.0

    points = []
    geohashes = []

    grid_width = [5009400.0, 1252300.0, 156500.0, 39100.0, 4900.0, 1200.0, 152.9, 38.2, 4.8, 1.2, 0.149, 0.0370]
    grid_height = [4992600.0, 624100.0, 156000.0, 19500.0, 4900.0, 609.4, 152.4, 19.0, 4.8, 0.595, 0.149, 0.0199]

    height = (grid_height[precision - 1])/2
    width = (grid_width[precision-1])/2

    lat_moves = int(math.ceil(radius / height)) #4
    lon_moves = int(math.ceil(radius / width)) #2

    for i in range(0, lat_moves):

        temp_lat = y + height*i

        for j in range(0,lon_moves):

            temp_lon = x + width*j

            if in_circle_check(temp_lat, temp_lon, y, x, radius):
                x_cen, y_cen = get_centroid(temp_lat, temp_lon, height, width)
                lat, lon = convert_to_latlon(y_cen, x_cen, latitude, longitude)
                points += [[lat, lon]]
                lat, lon = convert_to_latlon(-y_cen, x_cen, latitude, longitude)
                points += [[lat, lon]]
                lat, lon = convert_to_latlon(y_cen, -x_cen, latitude, longitude)
                points += [[lat, lon]]
                lat, lon = convert_to_latlon(-y_cen, -x_cen, latitude, longitude)
                points += [[lat, lon]]



    for point in points:
        geohashes += [Geohash.encode(point[0], point[1], precision)]

    geohashes=unique(geohashes)
    return geohashes

#    if georaptor_flag:
#        georaptor_out = georaptor.compress(set(geohashes), int(minlevel), int(maxlevel))
#        return ','.join(georaptor_out)
#
#    else:
#        return ','.join(set(geohashes))



    
def main():
    start_time = time.time()
    georaptor_flag = False
    minlevel = 1
    maxlevel = 12

    # Fetch input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('latitude', help='latitude of the center point')
    parser.add_argument('longitude', help='longitude of the center point')
    parser.add_argument('radius', help='radius of coverage in metres')
    parser.add_argument('precision_level', help='geohash precision level')
    parser.add_argument('--georaptor', default=False,
                        help='georaptor flag to compress the output (default: false)')
    parser.add_argument('--minlevel', default=1,
                        help='minimum level of geohash if georaptor set to true(default: 1)')
    parser.add_argument('--maxlevel', default=12,
                        help='maximum level of geohash if georaptor set to true(default: 12)')

    args = parser.parse_args()

    latitude = args.latitude
    longitude = args.longitude
    radius = args.radius
    precision_level = args.precision_level

    if 'georaptor' in args:
        georaptor_flag = args.georaptor

    if 'minlevel' in args:
        minlevel = args.minlevel

    if 'maxlevel' in args:
        maxlevel = args.maxlevel

    puts(colored.green('\nGenerating geohashes for\n'))

    puts(colored.red('latitude: ' + latitude))
    puts(colored.red('longitude: ' + longitude))
    puts(colored.red('radius: ' + radius))
    puts(colored.red('precision_level: ' + precision_level))

    if georaptor_flag:
        puts(colored.red('georaptor: ' + str(georaptor_flag)))
        puts(colored.red('minlevel: ' + str(minlevel)))
        puts(colored.red('maxlevel: ' + str(maxlevel)))

    puts('\n')
    puts(colored.red('Output:'))

    print(create_circle_geohash(float(latitude), float(longitude), float(radius), int(precision_level), georaptor_flag, int(minlevel), int(maxlevel)))

    et = time.time() - start_time

    puts(colored.green('\nTotal execution time: ' + str(et) + ' seconds\n'))

class Individu():
    def __init__(self, _id, _status, _timestamp, _geohashes):
        self.id = _id
        self.status = _status
        self.timestamp = _timestamp
        self.geohashes = _geohashes

    def __str__(self):
        return "[id %s | status %s | timestamp %s] %s" % (self.id, self.status, self.timestamp, self.geohashes)



if __name__ == '__main__':
    start_time = time.time()
    georaptor_flag = False
    minlevel = 1
    maxlevel = 12
    lists=[]
#   Create path
    clo=float(45.724947)
    cla=float(4.874956)
    level=9
    a=Individu(0, 1, 0, create_circle_geohash(clo,cla, float(50), level, False, 1, 12))
    b=Individu(1, 1, 0, create_circle_geohash(clo,cla, float(20), level, False, 1, 12))
    c=Individu(2, 1, 0, create_circle_geohash(clo,cla, float(10), level, False, 1, 12))
    d=Individu(3, 1, 0, create_circle_geohash(clo,cla, float(5), level, False, 1, 12))

    lists.append(a)
    lists.append(b)
    lists.appenf(b)
    lists.append(c)
    lists.append(c)
    lists.append(c)             
    lists.append(d)
    lists.append(d)
    lists.append(d)
    lists.append(d)

# generate heat map
    heatmap={}
    for i in lists:
        if (i.status == 1):
            print(i)
            for j in i.geohashes:
                # better with get method?
                try:
                    heatmap[j] += 1
                except KeyError:
                    heatmap[j] = 1
    print(type(heatmap))

#    pickle.dump( heatmap, open( "output", "wb" ) )
#   Csv file
    w = csv.writer(open("output", "w"),delimiter= '\t')
    for key, val in heatmap.items():
        w.writerow([key, val])
