#
# Erick Tian

# untangle - works - just need to format to have on click exit, show graph before, print path starting at 0 and going to smallest val


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
for i in range(len(nodes)-2):
    templist = nodes[i+1].split(' ')
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
for i in range(len(nodesDict)):
    nodesDict1[str(i)] = nodesDict[i]
# nodesDict1['4'] = (9, 42)
# print(nodesDict1)

# cf = plt.figure(1, figsize=(10,10))
# ax = cf.add_axes((0,0,1,1))

edgeD = []
for i in range(len(nodesDict)):
    edgeD.append(i)

    # G.add_edge(i,i+1)
    # totaldistance += calcd(nodesDict[i][1], nodesDict[i][0], nodesDict[i+1][1], nodesDict[i+1][0])
# edgeD.append([len(nodesDict)-1,0])
# totaldistance += calcd(nodesDict[len(nodesDict)-1][1],nodesDict[len(nodesDict)-1][0],nodesDict[0][1],nodesDict[0][0])
###### UNTANGLE
def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])
def intersect(A,B,C,D):#Return true if line segments AB and CD intersect
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
# print(nodesDict)

def reverse(i2,j,edgeD):
    newEdgeD = edgeD[:]
    for x in range(i2,j+1):
        newEdgeD[x]=edgeD[j-(x-i2)]
    return newEdgeD


newEdgeD = []
intersects = True
# iterations = 0
count = 0
while intersects:
    # newEdgeD = []
    # iterations += 1
    # print(iterations)
    numIntersects = 0
################################# ALSO make dict so dont have to recalculate every time
## cycle through edges in the list
## if two of them intersect, change them so that now they don't
## keep doing that
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
                # print(edgeD)
                # print(nodesDict)
                # print(j)
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
                if intersect(A,B,C,D):
                    numIntersects += 1
                    if i2<j: edgeD = reverse(i2,j,edgeD)
                    else: edgeD = reverse(j,i2,edgeD)
                    # timetobreak = True
                    break
        # if timetobreak:
        #     timetobreak = False
        #     break
    count+=1
    # print(numIntersects)
    if not numIntersects:
        intersects = False
        print(edgeD)



    # print('edgeD', edgeD)
    # print('newEdgeD', newEdgeD)
    # for i in edgeD:
    #     edge1x1 = nodesDict[i[0]][0]
    #     edge1y1 = nodesDict[i[0]][1]
    #     edge1x2 = nodesDict[i[1]][0]
    #     edge1y2 = nodesDict[i[1]][1]
    #     notIntersected = True
    #     for j in edgeD:
    #         numInt = 0
    #         if i!=j:
    #             edge2x1 = nodesDict[j[0]][0]
    #             edge2y1 = nodesDict[j[0]][1]
    #             edge2x2 = nodesDict[j[1]][0]
    #             edge2y2 = nodesDict[j[1]][1]
    #
    #             A = (edge1x1,edge1y1)
    #             B = (edge1x2, edge1y2)
    #             C = (edge2x1, edge2y1)
    #             D = (edge2x2, edge2y2)
    #             if intersect(A,B,C,D):
    #                 # numIntersects += 1
    #                 newEdgeD.append([i[0],j[0]])
    #                 newEdgeD.append([i[1],j[1]])
    #                 notIntersected = False
    #                 break
    #             # else:
    #             #     newEdgeD.append([i[0],i[1]])
    #             #     newEdgeD.append([j[0],j[1]])
    #             # print('x1',edge1x1)
    #             # print('y1',edge1y1)
    #             # print('x2',edge1x2)
    #             # print('y2',edge1y2)
    #     if notIntersected:
    #         newEdgeD.append([i[0],i[1]])
    # # if not numIntersects:
    # count+=1
    # print(count)
    # if count == 2:
    #     print('asdf')
    #     intersects = False
    # edgeD = newEdgeD[:]



for i in range(len(edgeD)-1):
    G.add_edge(edgeD[i],edgeD[i+1])
    totaldistance += calcd(nodesDict[edgeD[i]][1],nodesDict[edgeD[i]][0],nodesDict[edgeD[i+1]][1],nodesDict[edgeD[i+1]][0])
totaldistance += calcd(nodesDict[edgeD[len(edgeD)-1]][1],nodesDict[edgeD[len(edgeD)-1]][0],nodesDict[edgeD[0]][1],nodesDict[edgeD[0]][0])
print(totaldistance, "km")

G.add_edge(edgeD[len(edgeD)-1],edgeD[0])



# G.add_edge(1,2)


nx.draw(G, nodesDict, with_labels=True)
# nx.draw(G, pos=nodesDict1, with_labels=True)
#nx.draw_networkx_labels(G, nodesDict, namesDict)

# plt.ion()
# plt.draw()
plt.draw()
print('Time:',time.time()-starttime)
import msvcrt
def kbfunc():
   x = msvcrt.kbhit()
   if x:
      ret = ord(msvcrt.getch())
   else:
      ret = 0
   return ret
# plt.pause(.01)
# import SendKeys
# SendKeys('%{TAB}')
while True:
    plt.pause(.01)
    if kbfunc():
        break

plt.savefig("graph.png")