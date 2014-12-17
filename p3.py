#!/usr/bin/env python
import numpy
from sklearn import cluster, datasets


X = [ 
    [2,4],
    [3,3],[3,4],
    [5,4],[5,6],[5,8],
    [6,4],[6,5],[6,7],
    [7,3],[7,4],
    [8,2],
    [9,4],
    [10,6],[10,7],[10,8],
    [11,5],[11,8],
    [12,7],
    [13,6],[13,7],
    [14,6],
    [15,4],[15,5] ];

print len(X)

X = numpy.array(X);

dbscan = cluster.DBSCAN(eps=2, min_samples=3)
db = dbscan.fit( X );

print dir(db)


print db.core_sample_indices_
print len(db.core_sample_indices_)



