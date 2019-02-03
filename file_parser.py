#use glob to parse directory by file type
import os
import glob
def parse_dir(path) :
    files = []
    for file in glob.glob(path +"\\*.html"):
        print(os.path.basename(file))
    

parse_dir("C:\\Users\\Faizan")

