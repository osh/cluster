#!/usr/bin/env python
import itertools
import numpy

x = [];
x.append([1,0,1,1,0]);
x.append([1,1,0,1,0]);
x.append([0,0,1,1,0]);
x.append([0,1,0,1,0]);
x.append([1,0,1,0,1]);
x.append([0,1,1,0,0]);

def SMC(xi,xj):
    n11 = len(filter( lambda x: x==(1,1), zip(xi,xj)))
    n10 = len(filter( lambda x: x==(1,0), zip(xi,xj)))
    n01 = len(filter( lambda x: x==(0,1), zip(xi,xj)))
    n00 = len(filter( lambda x: x==(0,0), zip(xi,xj)))
    return (n11+n00)/(1.0*(n11+n10+n01+n00))
def JC(xi,xj):
    n11 = len(filter( lambda x: x==(1,1), zip(xi,xj)))
    n10 = len(filter( lambda x: x==(1,0), zip(xi,xj)))
    n01 = len(filter( lambda x: x==(0,1), zip(xi,xj)))
    return (n11)/(1.0*(n11+n10+n01))
def RC(xi,xj):
    n11 = len(filter( lambda x: x==(1,1), zip(xi,xj)))
    n10 = len(filter( lambda x: x==(1,0), zip(xi,xj)))
    n01 = len(filter( lambda x: x==(0,1), zip(xi,xj)))
    n00 = len(filter( lambda x: x==(0,0), zip(xi,xj)))
    return (n11)/(1.0*(n11+n10+n01+n00))

print SMC(x[0],x[1]);
print JC(x[0],x[1]);
print RC(x[0],x[1]);

def flatten(cluster):
    #print "flatten - %s"%(str(cluster))
    if(isinstance(cluster, (tuple))):
        return flatten(cluster[0]) + flatten(cluster[1])
    return [cluster];

def dm(ci,cj,dist):
    cif = flatten(ci);
    cjf = flatten(cj);
    dm = []
    for xi in cif:
        for xj in cjf:
            dm.append( dist(xi,xj) ) 
    return dm

def single(ci,cj,dist):
    return min(dm(ci,cj,dist))
def complete(ci,cj,dist):
    return max(dm(ci,cj,dist))
def group(ci,cj,dist):
    return numpy.mean(dm(ci,cj,dist))
  
#dist = RC
#gmeth = single

#dist = SMC
#gmeth = complete

dist = JC
gmeth = group

C = x;      
for gen in range(0,100):
    mindist = 100000000;
    minij = (None, None);
    for i in range(0,len(C)):
        for j in range(i+1,len(C)):
            dst = gmeth(C[i], C[j],dist);
            if(dst < mindist):
                mindist = dst;
                minij = (i,j)
            print dst,(i,j)

    (i,j) = minij;
    nc = ( C[i], C[j] )
    C.remove( nc[0] );
    C.remove( nc[1] );
    C.append( nc );
    print C
    print "gen finished"
    if(len(C)==1):
        print "finished"
        print C
        break;

