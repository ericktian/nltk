import re
from itertools import permutations
out = 'asdf'

inputlist = out.split(' ')
permsPreWild = [''.join(i).lower() for j in range(1, len(inputlist[0]) + 1) for i in permutations(inputlist[0], j)]
allperms = []
if '_' in inputlist[0]:
    for i in permsPreWild:
        if '_' in i:
            for j in range(97, 123):
                ilist = list(i)
                ilist[i.index('_')] = chr(j)
                newi = ''.join(ilist)
                if '_' in newi:
                    for k in range(97, 123):
                        newilist = list(newi)
                        newilist[newi.index('_')] = chr(k)
                        allperms.append(''.join(newilist))
                else:
                    allperms.append(newi)
        else:
            allperms.append(i)
else:
    allperms = permsPreWild[:]

if len(inputlist) == 1 or re.match('^[^0-9a-z]*$', inputlist[1].lower()):
    perms = allperms[:]
elif re.match('^[0-9]*$', inputlist[1]):
    perms = [''.join(i).lower() for i in permutations(inputlist[0], int(inputlist[1]))]
elif re.match('^[a-z]$', inputlist[1].lower()) and len(inputlist) >= 3 and re.match('^[0-9]*$', inputlist[2].lower()):
    index = int(inputlist[2])
    perms = []
    for i in allperms:
        # print('i',i,'index',index)
        if index < len(i) and i[index] == inputlist[1]:
            perms.append(i)
else:
    perms = allperms[:]

for i in perms:
    print(i)