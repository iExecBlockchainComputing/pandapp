# This script allows to generate tracks from many individuals on a square map of geohashes
# The code has not been tested

import Geohash
import numpy as np
import sys
import pickle
from Individu import Individu

def map( clo,cla, level, size ):
   # generate a grid of geohash
   # returns in a list in row oriented format (Row-major order)
    if size%3 != 0:
        raise ValueError("grid size not allowed, must be a multiple of 3" )
    if  level != 9:
        raise ValueError("level 9 geohash only supported " )

    #mandatory n mod 3 == 0, n min 6
    point=Geohash.encode(cla, clo, level)
    tmp=Geohash.decode(point)
    width=4.291534423828125e-05
    height=4.291534423828125e-05

    _map = ["0"] *size*size

    for i in range(0,size,3):
         for j in range(0,size,3):

              _cla = cla - (i*height)
              _clo = clo + (j*width)

              center=Geohash.encode(_cla, _clo, level )
              nw = Geohash.encode( _cla + height, _clo - width, level )
              n  = Geohash.encode( _cla + height, _clo,         level )
              ne = Geohash.encode( _cla + height, _clo + width, level )
              w  = Geohash.encode( _cla,          _clo - width, level )
              e  = Geohash.encode( _cla,          _clo + width, level )
              sw = Geohash.encode( _cla - height, _clo - width, level )
              s  = Geohash.encode( _cla - height, _clo,         level )
              se = Geohash.encode( _cla - height, _clo + width, level )

#               print(" i ", i ," j ", j)
#               print("_clo",_clo,"_cla",_cla)
#               print("nw", _cla + height, _clo - width, nw)
#               print("n ", _cla + height, _clo, n, Geohash.decode(n))
#               print("ne", _cla + height, _clo + width, ne)
#               print("w ", _cla,              _clo - width, w)
#               print("ce", _cla,              _clo, center)
#               print("e ", _cla,          _clo + width, e)
#               print("sw",_cla - height, _clo - width, sw)
#               print("s ", _cla - height, _clo, s)
#               print("se", _cla - height, _clo + width, se)

              _map[i * size    + j     ] = nw
              _map[i * size    + (j+1) ] = n
              _map[i * size    + (j+2) ] = ne
              _map[(i+1)* size + j     ] = w
              _map[(i+1)* size + (j+1) ] = center
              _map[(i+1)* size + (j+2) ] = e
              _map[(i+2)* size + j     ] = sw
              _map[(i+2)* size + (j+1) ] = s
              _map[(i+2)* size + (j+2) ] = se
    return _map


if __name__ == '__main__':

    clo=float(45.724947)
    cla=float(4.874956)
    level=9
    sizemap=6
    grid=map(cla, clo, level, sizemap)

    dataset_app1=[]
    dataset_app2=[]

    nbstep =6

#   Individu A not moving

    _geohashes1 = [0 for x in range(0, nbstep)]
    for x in range(0, nbstep):
        _geohashes1[x] = (x,grid[3*sizemap + 3])
    A=Individu(1, _geohashes1)
    dataset_app1.append(A)
    dataset_app2.append(A)

#   Individu B moving
    _geohashes2 = [0 for x in range(0, nbstep)]
    for x in range(0, nbstep):
        _geohashes2[x] = (x,grid[3*sizemap + x])
    B=Individu(0, _geohashes2)
    dataset_app1.append(B)
    dataset_app2.append(B)

#   Individu C moving
    _geohashes3 = [0 for x in range(0, nbstep)]

    for x in range(0, nbstep):
        _geohashes3[x] = (x,grid[x*sizemap + 1])
    C=Individu(1, _geohashes3)
    dataset_app1.append(C)
    dataset_app2.append(C)

    print("the map is")
    for i in range (0,sizemap):
         print( grid[(i)*sizemap: (i+1)*sizemap])

    print ("...generates tracks for heatmap app : tracks_heatmap.data")
    for ind in dataset_app1:
        print(ind)
    with open("tracks_heatmap.data", 'wb') as filehandle:
        # store the data as binary data stream
        pickle.dump(dataset_app1, filehandle)

    print ("...generates tracks for social distance app : tracks_socialdistance.data")
    for ind in dataset_app2:
        print(ind)
    with open("tracks_socialdistance.data", 'wb') as filehandle:
        # store the data as binary data stream
        pickle.dump(dataset_app2, filehandle)

