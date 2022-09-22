import codecs
import os

str = open('test.txt', 'r',encoding='utf-8').read()

str = str.replace("\n","<br/>")

new = open('data.txt' , "w" ,encoding='utf-8');

str = new.write(str)

os.startfile(r'data.txt')