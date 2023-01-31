import codecs
import os
import re
from unittest import result

print("Input News ID :")
newsId = input()

text = open('test.txt', 'r',encoding='utf-8').read()

text = text.replace("\n","<br/>")

imgCount = text.count("<img>") + 1

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

print(find_between(text,'<a>',"</a>"))

print(imgCount+1)

for count in range(imgCount):
    print(count)
    if count != 0 : 
        text = text.replace("<img>", "<img class=\\\"w-50\\\" src=\\\"../img/news/news" + str(newsId) + '_' + str(count) +".jpg\\\">" , 1)

new = open('data.txt' , "w" ,encoding='utf-8');

text = new.write(text)

os.startfile(r'data.txt')