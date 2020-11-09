#
# Erick Tian

import sys, time, re, os
# 1.2 works, but slowly
input = re.sub('[^ a-zA-Z]','',' '.join(sys.argv[1:]).upper())
    #.replace(',','').replace('.','').replace(';','')
path = str(os.path.realpath(__file__))
backslash = 0
for i in range(len(path)):
    if path[i]=="\\":
        backslash = i
location = path[:backslash+1]

#gen pos words
#sort <

wordss = [i.lower() for i in open(location + 'scrabble.txt', 'r').read().split('\n') if re.search(r"^[a-zA-Z]*$", i)]
wordss.append('i')
wordss.append('a')
prefixes = [set() for i in range(16)]
for i in wordss:
    for j in range(len(i)):
        prefixes[j+1].add(i[0:j+1])
words = [set() for i in range(16)]
for i in wordss:
    words[len(i)].add(i)

seen = set()
# path = str(os.path.realpath(__file__))
# backslash = 0
# for i in range(len(path)):
#     if path[i]=="\\":
#         backslash = i
# new = path[:backslash+1]
# print(new)

def isInvalid(sentence):
    # print(sentence)
    split = sentence.split(' ')
    pref = set()
    wd = set()
    for i in split:
        tracker = ''
        for j in i:
            if ord(j) in range(65,91):
                if tracker: pref.add(tracker)
                tracker = ''
                break
            tracker += j
        if tracker: wd.add(tracker)
    for i in pref:
        if i not in prefixes[len(i)]:
            return True
    for i in wd:
        if i not in words[len(i)]:
            return True
    return False

def isCompletelySolved(sentence):
    word = sentence.split(" ")
    for i in word:
        if i not in words[len(i)]: return False
    return True
def allEmpties(sentence):
    toret = []
    for i in range(len(sentence)):
        inds = []
        if re.search(r"^[A-Z]$", sentence[i]):
            inds.append(i)
            for j in range(len(sentence)):
                if sentence[i]==sentence[j] and i!=j:
                    inds.append(j)
            toret.append(inds)
    return toret
def bruteForce(sentence):
    # print('3', sentence)
    if isInvalid(sentence): return ''
    # print('2', sentence)
    if isCompletelySolved(sentence): return sentence

    emptyInds = allEmpties(sentence)
    for x in emptyInds:
        for i in range(97, 123):
            if chr(i) not in sentence:  #accounts for lowercase
                newSen = list(sentence)
                for j in x:
                    newSen[j] = chr(i)
                # print(''.join(newSen))
                bF = bruteForce(''.join(newSen))
                if bF: return bF
    return ''

print('\nCryptogram:', input, '\n')
starttime = time.time()
result = bruteForce(input)
endtime = time.time()
print('Time:', endtime-starttime)
if result == '': print('No solution')
else:
    print('Solution:')
    print(result.upper())