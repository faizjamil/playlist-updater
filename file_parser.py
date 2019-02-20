#use glob to parse directory by file type
import os
        
def parse_dir(path) :
    music_files = []
    sub_directories =[]
    #gets root (path of directory passed)
    for root, dirs, files in os.walk(path):
        #takes filenames and puts them into list if they are .mp3s or .m4a
        #files are prefixed by their absolute path
        #creates list of sub-directories
        for directory in dirs:
            if (directory != ''):
                sub_directories.append(directory)
        for name in files:
            if name.endswith('.mp3') or name.endswith('.m4a'):
                #adds path to beginning of file before appending
                music_files.append(os.path.join(root, name))
    for example in music_files:
        print(example)
    for x in sub_directories:
        print(x)
    return music_files, sub_directories

parse_dir("C:\\Users\\Faizan\\Music\\Soundtrack\\Other")