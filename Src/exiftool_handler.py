import exiftool
import pandas as pd
import os
from pyfiglet import Figlet




def banner(txt):
    f = Figlet(font='slant')
    print(f.renderText(txt))



def exiftoolAll(img_path):

    exiftool = exiftool.ExifTool(r'./exiftool.exe')

    metadata={}

    with exiftool.ExifToolHelper() as et:

        try:
            metadata = et.get_metadata(img_path) 

        except:
            print("Error file not found!!")
            return 0

    
    return metadata


def exifExtractAll(img_path):

    #print(img_path)
    #img_path = img_path if img_path[-1] in ['\\', '/'] else img_path+"\\" #os.path.abspath(img_path)

    metadata={}

    with exiftool.ExifToolHelper() as et:
        print(img_path)
        try:
            #for file in img_path:
            #    img = file['SourceFile']
            metadata = et.get_metadata(img_path)
            #print(metadata)

        except Exception as e:
            print(e)
            #return 0

    it = 1
    for item in metadata:
        print()
        print('------------------------------------------------------------')
        print('Metadata of file:   ',it)
        print('------------------------------------------------------------')
        print()
        it +=1
        for subitem in item:
            print(subitem,":    ",item[subitem])
    
    return metadata



def exifConvertToCsv(img_path, csv_path='metadata.csv'):
    metadata  = exifExtractAll(img_path)
    data_frame = pd.DataFrame.from_dict(metadata)
    data_frame.to_csv(csv_path)


