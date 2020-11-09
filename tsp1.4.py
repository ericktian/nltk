#
# Erick Tian

# untangle - works completely for second assignment
# change node_size and plt.figure to change sizes
# fixed intersect
# cleaned up


import time
import networkx as nx
import matplotlib.pyplot as plt
starttime = time.time()
file = open("KAD.txt", "r")
nodes = file.read().split("\n")

import msvcrt
def kbfunc():
   x = msvcrt.kbhit()
   if x:
      ret = ord(msvcrt.getch())
   else:
      ret = 0
   return ret

plt.figure(figsize=(10,6))

nodesDict = {}
for i in range(len(nodes)-2):
    templist = nodes[i+1].split(' ')
    nodesDict[i] = (float(templist[0])/1000.0, float(templist[1])/1000.0)

G = nx.Graph()
G.add_nodes_from(nodesDict)

edgesDict = {}
for i in range(1,len(nodes)-1):
    edgesDict[i] = []
    for j in range(1,len(nodes)-1):
        if j!=i: edgesDict[i].append(j)
from math import pi , acos , sin , cos
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
totaldistance = 0
positions = nx.get_node_attributes(G, 'pos')
nodesDict1 = {}
for i in range(len(nodesDict)):
    nodesDict1[str(i)] = nodesDict[i]
edgeD = []
for i in range(len(nodesDict)):
    edgeD.append(i)

for i in range(len(edgeD) - 1):
    G.add_edge(edgeD[i], edgeD[i + 1])
G.add_edge(edgeD[len(edgeD) - 1], edgeD[0])
nx.draw(G, nodesDict, node_size=0, with_labels=True)
plt.draw()
print('Original path:',edgeD)
ogdistance = 0
for i in range(len(edgeD)-1):
    ogdistance += calcd(nodesDict[edgeD[i]][1],nodesDict[edgeD[i]][0],nodesDict[edgeD[i+1]][1],nodesDict[edgeD[i+1]][0])
ogdistance += calcd(nodesDict[edgeD[len(edgeD)-1]][1],nodesDict[edgeD[len(edgeD)-1]][0],nodesDict[edgeD[0]][1],nodesDict[edgeD[0]][0])
print('Original distance:',ogdistance, "km")
print('Time:', time.time()-starttime,'\n')

############ SIMULATE KEYPRESS
from pynput.keyboard import Key, Controller
keyboard = Controller()
plt.pause(.01)
keyboard.press(Key.alt)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.release(Key.alt)

while True:
    plt.pause(.01)
    if kbfunc():
        break
plt.clf()
G.clear()

starttime2 = time.time()
# UNTANGLE
def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])
def intersect(A,B,C,D):#Return true if line segments AB and CD intersect
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
def reverse(i2,j,edgeD):
    newEdgeD = edgeD[:]
    for x in range(i2,j+1):
        newEdgeD[x]=edgeD[j-(x-i2)]
    return newEdgeD
newEdgeD = []
intersects = True
count = 0
while intersects:
    numIntersects = 0
    timetobreak = False
    for i in range(len(edgeD)):
        edge1x1 = nodesDict[edgeD[i]][0]
        edge1y1 = nodesDict[edgeD[i]][1]
        if i!=len(edgeD)-1:
            edge1x2 = nodesDict[edgeD[i+1]][0]
            edge1y2 = nodesDict[edgeD[i+1]][1]
            i2 = i+1
        else:
            edge1x2 = nodesDict[edgeD[0]][0]
            edge1y2 = nodesDict[edgeD[0]][1]
            i2 = 0
        for j in range(len(edgeD)-1):
            if j!=i and j!=i2 and j!=i-1:
                edge2x1 = nodesDict[edgeD[j]][0]
                edge2y1 = nodesDict[edgeD[j]][1]
                if j != len(edgeD) - 1:
                    edge2x2 = nodesDict[edgeD[j+1]][0]
                    edge2y2 = nodesDict[edgeD[j+1]][1]
                    j2 = j+1
                else:
                    edge2x2 = nodesDict[edgeD[0]][0]
                    edge2y2 = nodesDict[edgeD[0]][1]
                    j2 = 0
                A = (edge1x1, edge1y1)
                B = (edge1x2, edge1y2)
                C = (edge2x1, edge2y1)
                D = (edge2x2, edge2y2)
                normalD = calcd(A[1],A[0],B[1],B[0])+calcd(C[1],C[0],D[1],D[0])
                cross = calcd(A[1],A[0],C[1],C[0])+calcd(B[1],B[0],D[1],D[0])
                if normalD>cross:
                    numIntersects += 1
                    if i2<j: edgeD = reverse(i2,j,edgeD)
                    else: edgeD = reverse(j,i2,edgeD)
                    timetobreak = True
                    break
        if timetobreak:
            # timetobreak = False
            break
    if not numIntersects:
        intersects = False

edgePath = []
for i in range(len(edgeD)):
    if edgeD[i]==0:
        edgePath.extend([edgeD[k] for k in range(i,len(edgeD))])
        edgePath.extend([edgeD[l] for l in range(0,i)])
if edgePath[len(edgePath)-1]<edgePath[1]:
    edgePath = reverse(1,len(edgePath)-1,edgePath)
print('Path:',edgePath)

for i in range(len(edgeD)-1):
    G.add_edge(edgeD[i],edgeD[i+1])
    totaldistance += calcd(nodesDict[edgeD[i]][1],nodesDict[edgeD[i]][0],nodesDict[edgeD[i+1]][1],nodesDict[edgeD[i+1]][0])
totaldistance += calcd(nodesDict[edgeD[len(edgeD)-1]][1],nodesDict[edgeD[len(edgeD)-1]][0],nodesDict[edgeD[0]][1],nodesDict[edgeD[0]][0])
print('Distance:',totaldistance, "km")
G.add_edge(edgeD[len(edgeD)-1],edgeD[0])

nx.draw(G, nodesDict, node_size=0, with_labels=True)

plt.draw()

print('Time:',time.time()-starttime2)
while True:
    plt.pause(.01)
    if kbfunc():
        break

plt.savefig("graph.png")