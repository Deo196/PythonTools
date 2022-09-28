from pdf2image import convert_from_path
from PyPDF2 import PdfFileMerger
import os
import natsort

outputDir = "jpg/"

def convert(file, outputDir):
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    pages = convert_from_path(file,500,poppler_path=r'C:\Users\lcchu\Downloads\poppler-0.67.0\bin')
    counter = 1
    for page in pages:
        myfile = outputDir + 'i' + str(counter) + ".jpg"
        counter = counter + 1 
        page.save(myfile,"JPEG")
        print(counter)

inputDir = 'out/'
files = os.listdir(inputDir)
file = 'result.pdf'

files = natsort.natsorted(files)

print(files)

merger = PdfFileMerger()

for pdf in files:
    merger.append('out/'+pdf)
    #print(pdf)

merger.write('result.pdf')
merger.close





#convert(file,outputDir)