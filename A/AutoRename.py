import os

i = input()

folder_path = r'./pic' # your path
os.chdir(folder_path) # make the path active
x = sorted(os.listdir(), key=os.path.getctime)  # sorted using creation time

folder = 0

oldList = []

for folder in range(len(x)):
    #print(x[folder]) # print all the foldername inside the folder_path
    oldList.append(x[folder])
    folder = +1

print(oldList)

path = '../pic'
files = os.listdir(path)

a = 0


for index in oldList:
    print(index)
    a = a+1
    print(a)
    os.rename(index , 'news'+ str(i) + '_' + str(a) + '.jpg')
    

os.startfile(r'..\pic')