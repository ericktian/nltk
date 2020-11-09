# 1. Determine the number of
#   A. scrabble proper words in the dictionary
#   B. of length 3 or more, 4 or more
# 2. Determine the number of distinct 3 letter prefixes for all scrabble proper words of letter 3 or more
# 3. Same as 2 except 4 instead of 3

import re
# use re.search, not .match

wordss = open('wordss.txt', 'r').read().split('\n')

# print(re.search(r'^jjskdfls$', 'asdf', re.I)) # re.I re.S re.M put | between for multiple
                                     # returns none if no match, re object otherwise

# 1.
print('1.\n\tA.\n') # A.
print(len([i for i in wordss if re.search(r"(?=^[a-z]*$)(?=.{3,})(?=.*[aeiouy]|cwm|crwth)", i)]))
print('\n\tB.\n') # B.
print(len([i for i in wordss if re.search(r"(?=^[a-z]*$)(?=.{4,})(?=.*[aeiouy]|cwm|crwth)", i)]))
# 2.
print('\n2.\n')
print(len(set(k[:3] for k in [i for i in wordss if re.search(r"(?=^[a-z]*$)(?=.{3,})(?=.*[aeiouy]|cwm|crwth)", i)])))
# 3.
print('\n3.\n')
print(len(set(k[:4] for k in [i for i in wordss if re.search(r"(?=^[a-z]*$)(?=.{4,})(?=.*[aeiouy]|cwm|crwth)", i)])))