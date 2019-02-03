from os import walk
f = []

for (path, dirname, file) in walk("C:\\"):
    print("File name: ",file)
    break

#def msg ():
#    print("hello world")
#    return
#msg()

#fo = open("foo.txt", "r")
#print("Name of the file: ", fo.name)
#print(fo.read())

