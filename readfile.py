# import urllib.request
# import re
# regexurl = re.compile(
#         r'^(?:http|ftp)s?://' # http:// or https://
#         r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
#         r'localhost|' #localhost...
#         r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
#         r'(?::\d+)?' # optional port
#         r'(?:/?|[/?]\S+)$', re.IGNORECASE)
# input = "https://user.tjhsst.edu/2019etian/randomstate"
# # input = 'commonwords.txt'
#
# if re.search(regexurl, input):
#     content=urllib.request.urlopen(input)
#     for line in content:
#         print (line)
# else:
#     text = open(input, 'r').read()
#     print(text)

