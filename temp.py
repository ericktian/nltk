# # # # # # # # # # import sys, json, re
# # # # # # # # # #
# # # # # # # # # # # read input buffer
# # # # # # # # # # out = 'asdf'
# # # # # # # # # #
# # # # # # # # # # if re.match('^[a-zA-Z]*$', out):
# # # # # # # # # #     out = 'ur input needs to be ALL characters smh'
# # # # # # # # # # elif len(out)>7:
# # # # # # # # # #     out = 'ur input needs to be <= 7 characters'
# # # # # # # # # # else:
# # # # # # # # # #     out= 'nice it works'
# # # # # # # # # #
# # # # # # # # # # print(out)
# # # # # # # # #
# # # # # # # # # dict = {'apple': 'good'}
# # # # # # # # # # dict.update({'apple': 'bad'})
# # # # # # # # # dict['apple']('bad')
# # # # # # # # # print(dict)
# # # # # # # #
# # # # # # # # import sys
# # # # # # # # if "is erick cool?" in sys.argv[1]:
# # # # # # # #     print('yes')
# # # # # # # # else:
# # # # # # # #     print('no')
# # # # # # #
# # # # # # # # import re
# # # # # # # # wordss = [i.lower() for i in open('scrabble.txt', 'r').read().split('\n') if re.search(r"^[a-zA-Z]*$", i)]
# # # # # # # # # for i in wordss:
# # # # # # # # #     open('scrabble-lower.txt','w').write(i)
# # # # # # # # print(wordss[0])
# # # # # # #
# # # # # # # from itertools import permutations
# # # # # # # import itertools, re, sys
# # # # # # # perms = [''.join(p) for p in permutations('stack',3)]
# # # # # # # # print(perms)
# # # # # # #
# # # # # # # # my_list = ['a','s','d','f']
# # # # # # # # print([''.join(i) for i in itertools.permutations(my_list, 3)])
# # # # # # #
# # # # # # # # def posWords(inp, length, words):
# # # # # # # #     perms = [''.join(i) for i in permutations(inp,length)]
# # # # # # # #     outwords = []
# # # # # # # #     for i in perms:
# # # # # # # #         if i in words[len(i)]:
# # # # # # # #             outwords.append(i)
# # # # # # # #     return outwords
# # # # # # #
# # # # # # # out = 'asd 2'
# # # # # # # inputlist = out.split(' ')
# # # # # # #
# # # # # # # # if len(out) == 1 or not re.match('^[0-9]*$', out[1]):
# # # # # # # #     perms = [''.join(i) for i in permutations(inputlist[0])]
# # # # # # # # # else:
# # # # # # # # #     perms = [''.join(i) for i in permutations(inputlist[0], int(out[1]))]
# # # # # # # #
# # # # # # # # elif re.match('^[a-z]*$', inputlist[1].lower()) and len(inputlist) >= 3 and re.match('^[0-9]*$', inputlist[2].lower()):
# # # # # # # # perms = [''.join(i) for i in permutations(inputlist[0], int(inputlist[1])) if
# # # # # # # #          i[int(inputlist[2])] == inputlist[1]]
# # # # # # # # perms = [''.join(i) for i in permutations(inputlist[0]) if i[int(inputlist[2])] == inputlist[1]]
# # # # # # # #
# # # # # # #
# # # # # # # i = 'asdf__'
# # # # # # # if '_' in i:
# # # # # # #     pos_ = []
# # # # # # #     for j in range(97,123):
# # # # # # #         ilist = list(i)
# # # # # # #         ilist[i.index('_')] = chr(j)
# # # # # # #         newi = ''.join(ilist)
# # # # # # #         if '_' in newi:
# # # # # # #             for k in range(97, 123):
# # # # # # #                 newilist = list(newi)
# # # # # # #                 newilist[newi.index('_')] = chr(k)
# # # # # # #                 pos_.append(''.join(newilist))
# # # # # # #         else: pos_.append(newi)
# # # # # # #     print(pos_)
# # # # # # #
# # # # # # # inputlist = out.split(' ')
# # # # # # #
# # # # # # # if len(inputlist) == 1 or re.match('^[^0-9a-z]*$', inputlist[1].lower()):
# # # # # # #     perms = [''.join(i).lower() for i in permutations(inputlist[0])]
# # # # # # # elif re.match('^[0-9]*$', inputlist[1]):
# # # # # # #     perms = [''.join(i).lower() for i in permutations(inputlist[0], int(inputlist[1]))]
# # # # # # # elif re.match('^[a-z]*$', inputlist[1].lower()) and len(inputlist) >= 3 and re.match('^[0-9]*$', inputlist[2].lower()):
# # # # # # #     # sys.stdout.write('match: ' + ', '.join(inputlist))
# # # # # # #     perms = [''.join(i).lower() for i in permutations(inputlist[0]) if i[int(inputlist[2])] == inputlist[1]]
# # # # # # # else:
# # # # # # #     perms = [''.join(i).lower() for i in permutations(inputlist[0])]
# # # # # # #
# # # # # # # wordss = [i.lower() for i in open('/web/user/2019etian/public/python/scrabble.txt', 'r').read().split(
# # # # # # #     '\n')]  # if re.search(r"^[a-zA-Z]*$", i)]
# # # # # # # # for i in wordss:
# # # # # # # #     for j in range(len(i)):
# # # # # # # #         prefixes[j+1].add(i[0:j+1])
# # # # # # # words = [set() for i in range(30)]
# # # # # # # for i in wordss:
# # # # # # #     words[len(i)].add(i)
# # # # # # #
# # # # # # # sys.stdout.write('here')
# # # # # # #
# # # # # # # newperms = []
# # # # # # # if '_' in inputlist[0]:
# # # # # # #     sys.stdout.write('here2')
# # # # # # #     for i in perms:
# # # # # # #         if '_' in i:
# # # # # # #             # pos_ = []
# # # # # # #             for j in range(97, 123):
# # # # # # #                 ilist = list(i)
# # # # # # #                 ilist[i.index('_')] = chr(j)
# # # # # # #                 newi = ''.join(ilist)
# # # # # # #                 if '_' in newi:
# # # # # # #                     for k in range(97, 123):
# # # # # # #                         newilist = list(newi)
# # # # # # #                         newilist[newi.index('_')] = chr(k)
# # # # # # #                         newperms.append(''.join(newilist))
# # # # # # #                 else:
# # # # # # #                     newperms.append(newi)
# # # # # # #
# # # # # # #     if len(inputlist)==1 or re.match('^[^0-9a-z]*$',inputlist[1].lower()): perms = [''.join(i).lower() for j in range(len(inputlist[0])) for i in permutations(inputlist[0],j)]
# # # # # # #
# # # # # # # i = [[3,4],[1,2]]
# # # # # # # if [1,2] in i:
# # # # # # #     print('here1')
# # # # # # # if [2,1] in i:
# # # # # # #     print('here1.5')
# # # # # # # for j in i:
# # # # # # #     if 1 in j and 2 in j:
# # # # # # #         print('here2')
# # # # # # # print('here3')
# # # # # # #
# # # # # # # perms = [''.join(i).lower() for j in range(len(inputlist[0])) for i in permutations(inputlist[0], j) if
# # # # # # #          i[int(inputlist[2])] == inputlist[1]]
# # # # # # #
# # # # # from itertools import permutations
# # # # # import re
# # # # # # inputlist = ['asdf','d','2']
# # # # # # if re.match('^[a-z]$', inputlist[1].lower()) and len(inputlist) >= 3 and re.match('^[0-9]*$', inputlist[2].lower()):
# # # # # #     # # sys.stdout.write('match: ' + ', '.join(inputlist))
# # # # # #     perms = [''.join(i).lower() for j in range(1,len(inputlist[0])) for i in permutations(inputlist[0], j) if int(inputlist[2])<len(i) and i[int(inputlist[2])] == inputlist[1]]
# # # # # #     # perms = []
# # # # # #     # for j in range(1,len(inputlist[0])):
# # # # # #     #     for i in permutations(inputlist[0],j):
# # # # # #     #         # print('i',i)
# # # # # #     #         # print('j',j)
# # # # # #     #         if int(inputlist[2])<len(i) and i[int(inputlist[2])] == inputlist[1]:
# # # # # #     #             perms.append(''.join(i).lower())
# # # # # #     print(perms)
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #     newperms = []
# # # # # #     if '_' in inputlist[0]:
# # # # # #         for i in perms:
# # # # # #             if '_' in i:
# # # # # #                 for j in range(97, 123):
# # # # # #                     ilist = list(i)
# # # # # #                     ilist[i.index('_')] = chr(j)
# # # # # #                     newi = ''.join(ilist)
# # # # # #                     if '_' in newi:
# # # # # #                         for k in range(97, 123):
# # # # # #                             newilist = list(newi)
# # # # # #                             newilist[newi.index('_')] = chr(k)
# # # # # #                             newperms.append(''.join(newilist))
# # # # # #                     else:
# # # # # #                         newperms.append(newi)
# # # # # #     else:
# # # # # #         newperms = perms[:]
# # # # # #
# # # # # #     # out= 'valid input'
# # # # # #     inputlist = out.split(' ')
# # # # # #     if len(inputlist) == 1 or re.match('^[^0-9a-z]*$', inputlist[1].lower()):
# # # # # #         perms = [''.join(i).lower() for j in range(len(inputlist[0])) for i in permutations(inputlist[0], j)]
# # # # # #     elif re.match('^[0-9]*$', inputlist[1]):
# # # # # #         perms = [''.join(i).lower() for i in permutations(inputlist[0], int(inputlist[1]))]
# # # # # #     elif re.match('^[a-z]$', inputlist[1].lower()) and len(inputlist) >= 3 and re.match('^[0-9]*$',inputlist[2].lower()):
# # # # # #         index = int(inputlist[2])
# # # # # #         perms = [''.join(i).lower() for j in range(1, len(inputlist[0]) + 1) for i in permutations(inputlist[0], j)
# # # # # #                  if index < len(i) and (i[index] == inputlist[1] or (i[index] == '_') and ''.join(i)[:index]+inputlist[1]+''.join(i)[index+1:] in words[len(inputlist[0])])]
# # # # # #     else:
# # # # # #         perms = [''.join(i).lower() for j in range(len(inputlist[0])) for i in permutations(inputlist[0], j)]
# # # # # #     wordss = [i.lower() for i in open('/web/user/2019etian/public/python/enable1.txt', 'r').read().split('\n')]  # if re.search(r"^[a-zA-Z]*$", i)]
# # # # # #     words = [set() for i in range(30)]
# # # # # #     for i in wordss:
# # # # # #         words[len(i)].add(i)
# # # # # #     newperms = []
# # # # # #     if '_' in inputlist[0]:
# # # # # #         for i in perms:
# # # # # #             if '_' in i:
# # # # # #                 for j in range(97, 123):
# # # # # #                     ilist = list(i)
# # # # # #                     ilist[i.index('_')] = chr(j)
# # # # # #                     newi = ''.join(ilist)
# # # # # #                     if '_' in newi:
# # # # # #                         for k in range(97, 123):
# # # # # #                             newilist = list(newi)
# # # # # #                             newilist[newi.index('_')] = chr(k)
# # # # # #                             newperms.append(''.join(newilist))
# # # # # #                     else:
# # # # # #                         newperms.append(newi)
# # # # # #     else:
# # # # # #         newperms = perms[:]
# # # # # #
# # # # # # ####
# # # # # #
# # # # # # inputlist[0][:index]+inputlist[1]+inputlist[0][index:]
# # # # # # index = 2
# # # # # # i = ['f','o','_','o','d']
# # # # # # newone = ''.join(i)[:index]+'0'+''.join(i)[index+1:]
# # # # # # print(newone)
# # # # #
# # # # # out = 'b__fw a 1'
# # # # # wordss = [i.lower() for i in open('scrabble.txt', 'r').read().split('\n')]# if re.search(r"^[a-zA-Z]*$", i)]
# # # # # words = [set() for i in range(30)]
# # # # # for i in wordss:
# # # # #     words[len(i)].add(i)
# # # # #
# # # # # if False:
# # # # #     print('asdf')
# # # # #
# # # # # else:
# # # # #     inputlist = out.split(' ')
# # # # #     permsPreWild = [''.join(i).lower() for j in range(1,len(inputlist[0])+1) for i in permutations(inputlist[0], j)]
# # # # #     allperms = []
# # # # #     if '_' in inputlist[0]:
# # # # #         for i in permsPreWild:
# # # # #             if '_' in i:
# # # # #                 for j in range(97, 123):
# # # # #                     ilist = list(i)
# # # # #                     ilist[i.index('_')] = chr(j)
# # # # #                     newi = ''.join(ilist)
# # # # #                     if '_' in newi:
# # # # #                         for k in range(97, 123):
# # # # #                             newilist = list(newi)
# # # # #                             newilist[newi.index('_')] = chr(k)
# # # # #                             allperms.append(''.join(newilist))
# # # # #                     else:
# # # # #                         allperms.append(newi)
# # # # #             else:
# # # # #                 allperms.append(i)
# # # # #     else:
# # # # #         allperms = permsPreWild[:]
# # # # #     # print(allperms)
# # # # #     # exit()
# # # # #
# # # # #     if len(inputlist) == 1 or re.match('^[^0-9a-z]*$', inputlist[1].lower()):
# # # # #         perms = allperms[:]
# # # # #     elif re.match('^[0-9]*$', inputlist[1]):
# # # # #         perms = [''.join(i).lower() for i in permutations(inputlist[0], int(inputlist[1]))]
# # # # #     elif re.match('^[a-z]$', inputlist[1].lower()) and len(inputlist) >= 3 and re.match('^[0-9]*$',inputlist[2].lower()):
# # # # #         index = int(inputlist[2])
# # # # #         perms = []
# # # # #         # for j in range(1, len(inputlist[0]) + 1):
# # # # #         #     for i in permutations(inputlist[0], j):
# # # # #         #         if index < len(i):
# # # # #         #             # replace_ = ''.join(i)[:index] + inputlist[1] + ''.join(i)[index + 1:]
# # # # #         #             # print(replace_)
# # # # #         #             if i[index] == inputlist[1]:# or ((i[index] == '_') and replace_ in words[len(i)]):
# # # # #         #                 # perms.append(replace_)
# # # # #         #                 perms.append()
# # # # #         for i in allperms:
# # # # #             # print('i',i,'index',index)
# # # # #             if index < len(i) and i[index]==inputlist[1]:
# # # # #                 perms.append(i)
# # # # #     else:
# # # # #         perms = allperms[:]
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #     outwords = set()
# # # # #     for i in perms:
# # # # #         if i in words[len(i)]:
# # # # #             outwords.add(i)
# # # # #     out = 'Possible words: ' + ' '.join(sorted(outwords))
# # # # #     if (len(outwords) == 0): out = 'No possible words with given conditions'
# # # # #     print(out)
# # # # #
# # # # #
# # # # #         # s = {'asdf','asd','asde'}
# # # # # # print(sorted(s))
# # # # #
# # # # # # def reverse(i2,j,edgeD):
# # # # # #     newEdgeD = edgeD[:]
# # # # # #     for x in range(i2,j+1):
# # # # # #         print('x',x)
# # # # # #         print('other',j-(x-i2))
# # # # # #         newEdgeD[x]=edgeD[j-(x-i2)]
# # # # # #     return newEdgeD
# # # # # # asdf = [1,2,3,4,5,6]
# # # # # # print(reverse(1,3,asdf))
# # # # import re
# # # # from itertools import permutations
# # # # out = 'asdf'
# # # #
# # # # inputlist = out.split(' ')
# # # # permsPreWild = [''.join(i).lower() for j in range(1, len(inputlist[0]) + 1) for i in permutations(inputlist[0], j)]
# # # # allperms = []
# # # # if '_' in inputlist[0]:
# # # #     for i in permsPreWild:
# # # #         if '_' in i:
# # # #             for j in range(97, 123):
# # # #                 ilist = list(i)
# # # #                 ilist[i.index('_')] = chr(j)
# # # #                 newi = ''.join(ilist)
# # # #                 if '_' in newi:
# # # #                     for k in range(97, 123):
# # # #                         newilist = list(newi)
# # # #                         newilist[newi.index('_')] = chr(k)
# # # #                         allperms.append(''.join(newilist))
# # # #                 else:
# # # #                     allperms.append(newi)
# # # #         else:
# # # #             allperms.append(i)
# # # # else:
# # # #     allperms = permsPreWild[:]
# # # #
# # # # if len(inputlist) == 1 or re.match('^[^0-9a-z]*$', inputlist[1].lower()):
# # # #     perms = allperms[:]
# # # # elif re.match('^[0-9]*$', inputlist[1]):
# # # #     perms = [''.join(i).lower() for i in permutations(inputlist[0], int(inputlist[1]))]
# # # # elif re.match('^[a-z]$', inputlist[1].lower()) and len(inputlist) >= 3 and re.match('^[0-9]*$', inputlist[2].lower()):
# # # #     index = int(inputlist[2])
# # # #     perms = []
# # # #     for i in allperms:
# # # #         # print('i',i,'index',index)
# # # #         if index < len(i) and i[index] == inputlist[1]:
# # # #             perms.append(i)
# # # # else:
# # # #     perms = allperms[:]
# # # #
# # # # for i in perms:
# # # #     print(i)
# # #
# # # from pynput.keyboard import Key, Controller
# # # import time
# # #
# # # keyboard = Controller()
# # # starttime = time.time()
# # # while True:
# # #     if time.time()-starttime > 2:
# # #         # keyboard.press(Key.alt)
# # #         # keyboard.press(Key.tab)
# # #         # keyboard.release(Key.alt)
# # #         # keyboard.release(Key.tab)
# # #         keyboard.press()
# # #         break
# #
# # from itertools import permutations
# # print(list(permutations([12,34])))
# #
# # edgeD = [1,2,3,4,5]
# # n = 2
# # j = 1
# # k = list(permutations(edgeD[j:j+n],n))[1]
# # # print(k)
# # # print([1,2,3,4,5]+[6,7])
# # newED = edgeD[:j]+list(k)+edgeD[j + n:]
# # print(newED)
#
#                 # A = (edge1x1, edge1y1)
#                 # B = (edge1x2, edge1y2)
#                 # C = (edge2x1, edge2y1)
#                 # D = (edge2x2, edge2y2)
#                 # normalD = calcd(A[1],A[0],B[1],B[0])+calcd(C[1],C[0],D[1],D[0])
#                 # cross1 = calcd(A[1],A[0],C[1],C[0])+calcd(B[1],B[0],D[1],D[0])
#                 # cross2 = calcd(A[1],A[0],D[1],D[0])+calcd(B[1],B[0],C[1],C[0])
#                 # if normalD>cross1 and normalD>cross2:#intersect(A,B,C,D):
#                 #     numIntersects += 1
#                 #     if i2<j: edgeD = reverse(i2,j,edgeD)
#                 #     else: edgeD = reverse(j,i2,edgeD)
#                 #     break
#
# from pynput.keyboard import Key, Controller
# import time
#
# keyboard = Controller()
# starttime = time.time()
# while True:
#     if time.time()-starttime > 5:
#         # # keyboard.press(Key.alt)
#         # # keyboard.press(Key.tab)
#         # # keyboard.release(Key.alt)
#         # # keyboard.release(Key.tab)
#         # s = '''Aesop was one of the great Greek writers. He is best known for his fables, stories that have a moral. They teach us something about how we should live our lives. Aesop wrote thousands of these stories. Here are a few.
#         # The Wolf in Sheep's clothing
#         # Once upon a time, a Wolf decided to disguise the way he looked. He thought it would help him get food more easily. He put on the skin of a sheep, then he went out with the flock into the pasture. Even the shepherd was fooled by his clever costume. In the evening, the shepherd put him in with the rest of the sheep. He closed the gate and made sure it was secure before he went to bed. In the middle of the night, he came back to the fold to get some meat for the next day. Instead of killing a sheep, though, he grabbed the Wolf, killing him instantly.
#         # Those who look to harm others will be harmed themselves.
#         # The Bad and the Weasel
#         # A Bat fell on the ground and was caught by a Weasel. It begged the Weasel to spare its life, but the Weasel refused. It told the Bat that birds, by nature, were its enemy. The Bat assured him that it was not a bird, it was a mouse. The Weasel thought a moment, then set it free. A while later, the Bat fell again to the ground, and it was caught by another Weasel. It begged this Weasel not to eat him, either. The Weasel, though, said it did not like mice at all and would eat it. The Bat told the Weasel that it was not a mouse, but a bat. The second Weasel had no good answer, so he let it go.
#         # The Bat knew it is always wise to turn events to your advantage.
#         # The Lion and the Mouse
#         # A sleeping Lion was woken up by a Mouse running over his face. He got up angrily and caught the scared little Mouse. He was about to kill the Mouse, but it said in its squeaky little voice, "If you would only spare my life, I would be sure to repay your kindness." The Lion laughed at such nonsense, but he let him go. A short time later, though, the Lion was caught by some hunters. They bound him by ropes to the ground. The Mouse recognized his roar, and he rushed over and gnawed the rope with his teeth, setting the Lion free. The Mouse said "You laughed at the idea of my ever being able to help you. Now you know that it is possible for even a small little Mouse to help a great big Lion."'''
#         # for i in range(len(s)):
#         #     keyboard.press(s[i])
#         #     keyboard.release(s[i])
#         # break
#         tS = time.time()
#         # while time.time()-tS<1:
#         #     # keyboard.press(Key.right)
#         break

# import msvcrt
# while(True):
#     print('asdf')
#     if msvcrt.kbhit():
#         break

def dosmth(arr):
    arr[0] = 5
arra = [3,1,5]
dosmth(arra)
print(arra)