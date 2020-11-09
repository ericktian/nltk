#
# Erick Tian

import sys, time, re, os
# 2.0 - works, is faster, minimizes words by finding dictionary of possible words that can be decrypted into,
# then finds solutions by searching through words with fewest possible choices first
input = re.sub('[^ a-zA-Z]','',' '.join(sys.argv[1:]).upper())
    #.replace(',','').replace('.','').replace(';','')
path = str(os.path.realpath(__file__))
backslash = 0
for i in range(len(path)):
    if path[i]=="\\":
        backslash = i
location = path[:backslash+1]
inputList = input.split(' ')

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

def matchCode(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    dict = {}
    word2set = set()
    for i in range(len(word1)):
        if word1[i] not in dict:
            dict[word1[i]] = i
            if word2[i] in word2set:
                return False
            word2set.add(word2[i])
        else:
            if word2[i]!=word2[dict[word1[i]]]:
                return False
    return True

inpwords = input.split(' ')
inpdict = {}
for i in inpwords:
    inpdict[i] = set()
    for j in words[len(i)]:
        if matchCode(i,j):
            inpdict[i].add(j)
# print(inpdict)
# for i in inpdict:
#     print(len(inpdict[i]))
# exit()

seen = set()
# path = str(os.path.realpath(__file__))
# backslash = 0
# for i in range(len(path)):
#     if path[i]=="\\":
#         backslash = i
# new = path[:backslash+1]
# print(new)

def isValid(newSen, ind):
    sentence = inputList
    # print(sentence)
    joinedsen = ''.join(sentence)
    joinednew = ''.join(newSen)
    # print(sentence[ind])
    for i in range(len(sentence[ind])):
        for j in [x for x in range(len(joinedsen)) if joinedsen[x]==sentence[ind][i]]:
            if re.match('[a-z]', joinednew[j]) and joinednew[j]!=newSen[ind][i]:
                return False
        for k in [x for x in range(len(joinednew)) if joinednew[x]==newSen[ind][i]]:
            if re.match('[a-z]', joinedsen[k]) and joinedsen[k]!=sentence[ind][i]:
                return False
    return True
# new1 = ['this', 'thi', 'sip', 'xcn']
# # asdf asd fdq yui
# print(isValid(new1, 2))
# exit()
# new1 = ['beak', 'GDK']
# # asdf gdk
# print(isValid(new1, 0))
# exit()

def isCompletelySolved(sentence):
    for i in sentence:
        if re.match('^[A-Z]*$', i): return False
    # print(sentence)
    return True
def allEmpties(sentence):
    toret = []
    for i in range(len(sentence)):
        if re.match('^.*[A-Z]', sentence[i]):
            toret.append(i)
    lendict = {i:len(inpdict[inputList[i]]) for i in toret}
    # print(toret)
    # print(inputList)
    # print(lendict)
    newlist = sorted(lendict.items(), key=lambda x: (x[1], x[0]), reverse=False)
    # print('newlist\n', newlist)
    sortedtoret = [i[0] for i in newlist]
    # print(sortedtoret)
    # exit()
    return sortedtoret
# print([['here', 'is', 'a', 'SENTENCE', 'noW', 'yEAh', 'yes'][i] for i in allEmpties(['here', 'is', 'a', 'SENTENCE', 'noW', 'yEAh', 'yes'])])
# exit()
def bruteForce(sentence, last):
    if not isValid(sentence, last):
        # print(sentence, last)
        # exit()
        return ''
    if isCompletelySolved(sentence): return sentence    ### checks if all words are lowercase

    emptyWds = allEmpties(sentence)        ### emptyInds are the words in a list indexes that have uppercase
    for x in emptyWds:
        for i in inpdict[sentence[x]]:                ### should bc the set of working matches
            newSen = sentence[:]
            # print('newSen', newSen,'sentence', sentence)
            newSen[x] = i
            # print('newSen', newSen)
            # if isValid(newSen, x):   ### checks if newSen matches w the original
            # print(newSen)
            bF = bruteForce(newSen, x)
            if bF: return bF
    return ''

print('\nCryptogram:', input, '\n')
starttime = time.time()
# print(inputList)
result = bruteForce(inputList, 0)
endtime = time.time()
print('Time:', endtime-starttime)
if result == '': print('No solution')
else:
    print('Solution:')
    print(' '.join([i.upper() for i in result]))