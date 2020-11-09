import random
numVert = 100000
avgDeg = 5
nodes = [[] for i in range(numVert)]
for j in range(numVert*avgDeg//2):
    rand1 = random.randrange(numVert)
    rand2 = random.randrange(numVert)
    while rand2==rand1 and rand2 not in nodes[rand1]: rand2 = random.randrange(100)
    nodes[rand1].append(rand2)
    nodes[rand2].append(rand1)
maxDeg = max([len(a) for a in nodes])
# print(maxDeg)
dictDegree = {k:0 for k in range(maxDeg+1)}
# print(dictDegree)
for x in nodes:
    dictDegree[len(x)]+=1
# print(dictDegree)
print(sum(i*dictDegree[i] for i in range(maxDeg+1)))
for b in range(len(dictDegree)):
    print(str(b)+'\t'+str(dictDegree[b]))