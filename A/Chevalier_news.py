import codecs
import os

newsId = input()

text = open('test.txt', 'r',encoding='utf-8').read()

text = text.replace("\n","<br/>")

imgCount = text.count("<img>") + 1



print(imgCount+1)

for count in range(imgCount):
    
    if count != 0 : 
        text = text.replace("<img>", "<img style=\\\"width:100%\\\" src=\\\"../../images/news/news" + str(newsId) + '_' + str(count) +".jpg\\\">" , 1)

new = open('data.txt' , "w" ,encoding='utf-8');

text = new.write(text)

os.startfile(r'data.txt')