import sys, time, re
input = ' '.join(sys.argv[1:]).upper()
wordss = [i.lower() for i in open('scrabble.txt', 'r').read().split('\n') if re.search(r"^[A-Z]*$", i)]
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

def pzlInvalid(sentence):
    low = ''
    for i in range(len(sentence)):
        if ord(sentence[i]) in range(65, 91):
            break
        low += sentence[i]
    if not low: return False
    for i in low.split(' '):
        if i not in prefixes[len(i)]:
            return True

    for i in range(len(low.split(' '))-1):
        if low.split(' ')[i] not in words[len(low.split(' ')[i])]:
            return True

    return False

# print(pzlInvalid('zyx here'))
# exit()

def pzlCompletelySolved(sentence):
    word = sentence.split(" ")
    for i in word:
        if i.lower() not in words[len(i)]: return False
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
    if pzlInvalid(sentence): return ''
    print('2', sentence)
    if pzlCompletelySolved(sentence): return sentence

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
if result == '': print('No solution')
else:
    print('Solution:')
    print(result.upper())
print('Time:', endtime-starttime)