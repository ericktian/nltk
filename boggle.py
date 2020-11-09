import sys, re, time
board = sys.argv[1]
side = int(len(board)**.5)
print('\n'.join([board[i*side:i*side+side] for i in range(side)]))
print()
wordss = [i.lower() for i in open('scrabble.txt', 'r').read().split('\n') if re.search(r"^[A-Z]*$", i)]
start = time.time()

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