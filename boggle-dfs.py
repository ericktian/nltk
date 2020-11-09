import sys, re, time
board = sys.argv[1]
#code for th, sh, etc
side = int(len(board)**.5)
print('\n'.join([board[i*side:i*side+side] for i in range(side)]))
print()
wordss = [i for i in open('wordss.txt', 'r').read().split('\n') if re.search(r"^[a-z]*$", i)]
start = time.time()

# lookup = [[0]]
# if side==2: lookup = [[1,2,3], [0,2,3], [0,1,3], [0,1,2]]
# elif side==3: lookup = [[1, 3], [0, 2, 4], [1, 5], [0, 4, 6], [1, 3, 5, 7], [2, 5, 8], [3, 7], [4, 6, 8], [5, 7]]
# elif side==4: lookup = [[1,4], [0,2,5], [1,3,6], [2,7], [0,5,8], [1,4,6,9], [2,5,7,10], [3,6,11], [4,9,12], [5,8,10,13], [6,9,11,14],
#           [7,10,15], [8,13], [9,12,14], [10,13,15], [11,14]]
lookup = [[] for x in range(len(board))]
for i in range(len(board)):
    if i%side!=0: lookup[i].append(i-1)
    if (i+1)%side!=0: lookup[i].append(i+1)
    if i>=side:
        lookup[i].append(i-side)
        if i%side!=0:
            lookup[i].append(i-1-side)
        if (i+1)%side!=0:
            lookup[i].append(i+1-side)
    if i<side**2-side:
        lookup[i].append(i+side)
        if i%side!=0:
            lookup[i].append(i-1+side)
        if (i+1)%side!=0:
            lookup[i].append(i+1+side)

posWords = set()
dictAlreadySeen = set()
paths = 0
for root in range(len(board)):
    parseMe = [[root]]
    # dictAlreadySeen = set()

    while len(parseMe) > 0:
        node = parseMe.pop(0)
        gapindex = node[-1]
        for i in lookup[gapindex]:
            if i not in node:
                newnode = node[:]
                newnode.append(i)
                newword = ''.join([board[int(i)] for i in newnode])
                if ','.join([str(i) for i in newnode]) not in dictAlreadySeen:
                    parseMe.append(newnode)
                    dictAlreadySeen.add(','.join([str(i) for i in newnode]))
                    if(newword in wordss):
                        # print(newword)
                        posWords.add(newword)
                        paths += 1

print('words:', ', '.join([i for i in posWords]))
print(len(posWords), 'possible words')
print(paths, 'possible paths to words')
print('time:', time.time()-start)