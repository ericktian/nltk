import sys, time, re
input = ' '.join(sys.argv[1:]).upper()
wordss = [i.lower() for i in open('scrabble.txt', 'r').read().split('\n') if re.search(r"^[A-Z]*$", i)]
wordss.append('i')
wordss.append('a')
# wordss.append('afifie')
seen = set()

def pzlInvalid(sentence):
    # print(sentence)
    # if 'breres' in sentence: exit()
    for i in range(len(sentence)):
        if re.search(r"^[A-Z]$", sentence[i]): #or sentence[i] in wordss:
            return False
    # for i in range(len(sentence)):
    #     if sentence[i] not in wordss:
    #         return True
    # return False
    return True
def pzlCompletelySolved(sentence):
    print(sentence)
    # if 'bererq' in sentence: exit()
    word = sentence.split(" ")
    for i in word:
        if i.lower() not in wordss: return False
    return True
def firstEmpties(sentence):
    inds = []
    for i in range(len(sentence)):
        if re.search(r"^[A-Z]$", sentence[i]):
            inds.append(i)
            for j in range(len(sentence)):
                if sentence[i]==sentence[j] and i!=j:
                    inds.append(j)
            return inds
    return []
def bruteForce(sentence):
    # print('3', sentence)
    if pzlCompletelySolved(sentence): return sentence
    if pzlInvalid(sentence): return ''
    # print('2', sentence)

    emptyInds = firstEmpties(sentence)
    for i in range(97, 123):
        if chr(i) not in sentence:  #accounts for lowercase
            newSen = list(sentence)
            for j in emptyInds:
                newSen[j] = chr(i)
            bF = bruteForce(''.join(newSen))
            if bF: return bF
    return ''

print('\nCryptogram:', input, '\n')
starttime = time.time()
result = bruteForce(input)
endtime = time.time()
if result == '': print('No solution')
else:
    print('Solution:')
    print(result.upper())
print('Time:', endtime-starttime)