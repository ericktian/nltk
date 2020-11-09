#
# Erick Tian

# Cleaned version with permutations, untangle, etc.

# calcd(y1,x1,y2,x2)
# importFile( )
# calcAllDistances( )
# pathLen( )
# normalize( ) - displays right path
# greedyPath( )
# unscramble( )
# allPerm( ) - or itertools
# permDistance( )
# permute( )

import time
import networkx as nx
import matplotlib.pyplot as plt

import msvcrt                                   # used in kbfunc
from math import pi , acos , sin , cos          # used in calcd
from itertools import permutations              # used in permute
from pynput.keyboard import Key, Controller     # used in altTab

### METHODS ###
def importFile(filename):
    file = open(filename, "r")
    nodes = file.read().split("\n")
    return nodes
def kbfunc():
   x = msvcrt.kbhit()
   if x:
      ret = ord(msvcrt.getch())
   else:
      ret = 0
   return ret
def calcd(y1,x1, y2,x2):
   y1  = float(y1)
   x1  = float(x1)
   y2  = float(y2)
   x2  = float(x2)
   R   = 6371#3958.76 # miles = 6371 km
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R
def ccw(A,B,C):
    return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
def reverse(i2,j,edgeD):
    newEdgeD = edgeD[:]
    for x in range(i2,j+1):
        newEdgeD[x]=edgeD[j-(x-i2)]
    return newEdgeD
def edgeSum(j,n,edgeD):
    return sum([calcd(nodesDict[edgeD[i%len(edgeD)]][1],nodesDict[edgeD[i%len(edgeD)]][0],nodesDict[edgeD[(i+1)%len(edgeD)]][1],nodesDict[edgeD[(i+1)%len(edgeD)]][0]) for i in range(j,j+n)])
def calcAllDistances(edgeD):
    return sum([calcd(nodesDict[edgeD[i]][1], nodesDict[edgeD[i]][0], nodesDict[edgeD[(i+1)%(len(edgeD))]][1],nodesDict[edgeD[(i+1)%(len(edgeD))]][0]) for i in range(len(edgeD))])
def greedyPath(edgeD):
    newEdgeD = []
    edgeD2 = edgeD[:]
    newEdgeD.append(edgeD2[0])
    edgeD2.remove(edgeD2[0])
    while edgeD2:
        tempD = calcd(nodesDict[edgeD2[0]][1],nodesDict[edgeD2[0]][0],nodesDict[newEdgeD[-1]][1],nodesDict[newEdgeD[-1]][0])
        tempBest = edgeD2[0]
        for i in edgeD2[1:]:
            newD = calcd(nodesDict[i][1],nodesDict[i][0],nodesDict[newEdgeD[-1]][1],nodesDict[newEdgeD[-1]][0])
            if newD < tempD:
                tempBest = i
                tempD = newD
        newEdgeD.append(tempBest)
        edgeD2.remove(tempBest)
    return newEdgeD
def untangleInefficient(edgeD):
    intersects = True
    while intersects:
        numIntersects = 0
        timetobreak = False
        for i in range(len(edgeD)):
            edge1x1,edge1y1,edge1x2,edge1y2 = nodesDict[edgeD[i]][0],nodesDict[edgeD[i]][1],nodesDict[edgeD[(i + 1) % (len(edgeD))]][0],nodesDict[edgeD[(i + 1) % (len(edgeD))]][1]
            i2 = (i+1)%(len(edgeD)-1)
            for j in range(len(edgeD)):
                if j != i and j != i2 and (j+1)%(len(edgeD))!=i:
                    edge2x1,edge2y1,edge2x2,edge2y2 = nodesDict[edgeD[j]][0],nodesDict[edgeD[j]][1],nodesDict[edgeD[(j + 1) % (len(edgeD))]][0],nodesDict[edgeD[(j + 1) % (len(edgeD))]][1]
                    if intersect((edge1x1, edge1y1), (edge1x2, edge1y2), (edge2x1, edge2y1), (edge2x2, edge2y2)):
                        numIntersects += 1
                        if i2 < j: edgeD = reverse(i2, j, edgeD)
                        else: edgeD = reverse(j, i2, edgeD)
                        timetobreak = True
                        break
            if timetobreak: break
        if not numIntersects: intersects = False
    return edgeD
def untangle(edgeD,distanceDict):
    intersects = True
    while intersects:
        numIntersects = 0
        timetobreak = False
        for i in range(len(edgeD)):
            i2 = (i + 1) % (len(edgeD) - 1)
            for j in range(len(edgeD)):
                j2 = (j + 1) % (len(edgeD))
                if j != i and j != i2 and j2 != i and i2 != j2:
                    if distanceDict[edgeD[i]][edgeD[i2]]+distanceDict[edgeD[j]][edgeD[j2]] > distanceDict[edgeD[i]][edgeD[j]]+distanceDict[edgeD[i2]][edgeD[j2]]:#calcd(A[1], A[0], B[1], B[0]) + calcd(C[1], C[0], D[1], D[0]) > calcd(A[1], A[0], C[1],C[0]) + calcd(B[1], B[0],D[1], D[0]):
                        numIntersects += 1
                        if i2 < j:edgeD = reverse(i2, j, edgeD)
                        else:edgeD = reverse(j, i2, edgeD)
                        timetobreak = True
                        break
            if timetobreak: break
        if not numIntersects: intersects = False
    return edgeD
def permute(edgeD,n):
    for j in range(len(edgeD)):
        currd = calcAllDistances(
            edgeD)
        for k in permutations(edgeD[j:j+n], n):
            newED = edgeD[:j] + list(k)+edgeD[j + n:]
            newd = calcAllDistances(newED)
            if newd < currd:
                edgeD = newED
    return edgeD
def altTab():
    plt.draw()
    # SIMULATE KEYPRESS
    keyboard = Controller()
    plt.pause(.01)
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt)
def update(edgeD,starttime):
    edgePath = []
    for i in range(len(edgeD)):
        if edgeD[i] == 0:
            edgePath.extend([edgeD[k] for k in range(i, len(edgeD))])
            edgePath.extend([edgeD[l] for l in range(0, i)])
    if edgePath[len(edgePath) - 1] < edgePath[1]:
        edgePath = reverse(1, len(edgePath) - 1, edgePath)
    print('Path:', edgePath)
    edgeD = edgePath
    totaldistance = 0
    for i in range(len(edgeD) - 1):
        G.add_edge(edgeD[i], edgeD[i + 1])
        totaldistance += calcd(nodesDict[edgeD[i]][1], nodesDict[edgeD[i]][0], nodesDict[edgeD[i + 1]][1],nodesDict[edgeD[i + 1]][0])
    totaldistance += calcd(nodesDict[edgeD[len(edgeD) - 1]][1], nodesDict[edgeD[len(edgeD) - 1]][0],nodesDict[edgeD[0]][1], nodesDict[edgeD[0]][0])
    print('Distance:', totaldistance, "km")
    G.add_edge(edgeD[len(edgeD) - 1], edgeD[0])
    nx.draw(G, nodesDict, node_size=0, with_labels=True)
    print('Time:', time.time() - starttime)
def display():
    plt.draw()
    while True:
        plt.pause(.01)
        if kbfunc():
            break
    plt.clf()
    G.clear()
    print('')
def setup(G,nodesDict,edgeD,distanceDict):
    plt.figure(figsize=(10, 6))
    for i in range(len(nodes) - 2):
        templist = nodes[i + 1].split(' ')
        nodesDict[i] = (float(templist[0]) / 1000.0, float(templist[1]) / 1000.0)
    G.add_nodes_from(nodesDict)
    for i in range(len(nodesDict)):
        edgeD.append(i)
    for i in range(len(edgeD) - 1):
        G.add_edge(edgeD[i], edgeD[i + 1])
    G.add_edge(edgeD[len(edgeD) - 1], edgeD[0])
    for i in range(len(edgeD)):
        distanceDict[i] = {}
        for j in range(len(edgeD)):
            if i != j:
                distanceDict[i][j] = calcd(nodesDict[edgeD[i]][1], nodesDict[edgeD[i]][0], nodesDict[edgeD[j]][1],nodesDict[edgeD[j]][0])

### MAIN ###

# setup
nodes = importFile("DAU.txt")
starttime = time.time()
G,nodesDict,edgesDict,edgeD,distanceDict = nx.Graph(),{},{},[],{}
setup(G,nodesDict,edgeD,distanceDict)

# original
print('Original')
update(edgeD,starttime)
altTab()
display()

# greedy paths
print('Greedy')
starttimeGreed = time.time()
edgeD = greedyPath(edgeD)
update(edgeD,starttimeGreed)
display()

# untangleInefficient
print('Untangle Inefficient')
starttimeInef = time.time()
edgeD = untangleInefficient(edgeD)
update(edgeD,starttimeInef)
display()

# # untangle
# print('Untangle')
# starttime4 = time.time()
# edgeD = untangle(edgeD,distanceDict)
# update(edgeD,starttime4)
# display()

# permute
print('Permute')
starttimePermute = time.time()
edgeD = permute(edgeD,4)
update(edgeD,starttimePermute)
display()

# untangle
print('Untangle 2')
starttime4 = time.time()
edgeD = untangle(edgeD,distanceDict)
update(edgeD,starttime4)
display()