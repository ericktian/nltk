#
# Erick Tian

# currently displays the hamiltonian cycle from 1-38


import time
import networkx as nx
# import matplotlib as mpl
# mpl.use('Agg')
import matplotlib.pyplot as plt
starttime = time.time()
# file = open("romEdges.txt", "r")
# edges = file.read().split("\n")
file = open("KAD.txt", "r")
nodes = file.read().split("\n")

nodesDict = {}
# print(nodes)
for i in range(1,len(nodes)-1):
    templist = nodes[i].split(' ')
    # print(i)
    # print(templist)
    nodesDict[i] = (float(templist[0])/1000.0, float(templist[1])/1000.0)

G = nx.Graph()
G.add_nodes_from(nodesDict)
# G.add_edge('1','2')
# nx.draw(G, nodesDict, with_labels=True)
# plt.savefig("graph.png")
# exit()
#
# for i in range(1,len(nodes)-1):
#     dict = {}
#     # print(nodesDict[i])
#     dict['pos'] = nodesDict[i]
#     # print(nodesDict[i])
#     G.add_node(nodes[i][0], pos=nodesDict[i])

edgesDict = {}
for i in range(1,len(nodes)-1):
    edgesDict[i] = []
    for j in range(1,len(nodes)-1):
        if j!=i: edgesDict[i].append(j)

# print(edgesDict)
# exit()

# def calcEdge(s1, s2):
#     return ((nodesDict[s1][0]-nodesDict[s2][0])**2 + (nodesDict[s1][1]-nodesDict[s2][1])**2)**.5
#
# Torbert, 22 Sept 2014
# White (ed), 5 Oct 2016
#
from math import pi , acos , sin , cos
#
def calcd(y1,x1, y2,x2):
   #
   # y1 = lat1, x1 = long1
   # y2 = lat2, x2 = long2
   # all assumed to be in decimal degrees

   # if (and only if) the input is strings
   # use the following conversions

   y1  = float(y1)
   x1  = float(x1)
   y2  = float(y2)
   x2  = float(x2)
   #
   R   = 6371#3958.76 # miles = 6371 km
   #
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   #
   # approximate great circle distance with law of cosines
   #
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R
   #
#
# end of file
#
# print(edgesDict)
# exit()
totaldistance = 0
# for i in range(1,len(edgesDict)):
#     for j in edgesDict[i]:#range(1,len(edgesDict)):
#         # print('i',i)
#         # print(nodesDict[i])
#         # print('j',j)
#         # print(nodesDict[j])
#         totaldistance += calcd(nodesDict[i][0], nodesDict[i][1], nodesDict[j][0], nodesDict[j][1])

# for i in edges:
#     G.add_edge(i[0], i[2])
#     totaldistance += calcd(nodesDict[i[0]][1], nodesDict[i[0]][0], nodesDict[i[2]][1], nodesDict[i[2]][0])


positions = nx.get_node_attributes(G, 'pos')
nodesDict1 = {}
for i in range(1,len(nodesDict)+1):
    nodesDict1[str(i)] = nodesDict[i]
# nodesDict1['4'] = (9, 42)
# print(nodesDict1)

# cf = plt.figure(1, figsize=(10,10))
# ax = cf.add_axes((0,0,1,1))


for i in range(1,len(nodesDict)):
    G.add_edge(i,i+1)
    totaldistance += calcd(nodesDict[i][1], nodesDict[i][0], nodesDict[i+1][1], nodesDict[i+1][0])
totaldistance += calcd(nodesDict[len(nodesDict)][1],nodesDict[len(nodesDict)][0],nodesDict[1][1],nodesDict[1][0])
print(totaldistance, "km")

G.add_edge(len(nodesDict),1)
# G.add_edge(1,2)


nx.draw(G, nodesDict, with_labels=True)
# nx.draw(G, pos=nodesDict1, with_labels=True)
#nx.draw_networkx_labels(G, nodesDict, namesDict)

# plt.ion()
# plt.draw()
plt.draw()
import msvcrt
def kbfunc():
   x = msvcrt.kbhit()
   if x:
      ret = ord(msvcrt.getch())
   else:
      ret = 0
   return ret
while True:
    plt.pause(.01)
    if kbfunc():
        break

plt.savefig("graph.png")