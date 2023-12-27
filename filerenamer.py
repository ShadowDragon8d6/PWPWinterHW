#import needed libraries
import os
import re

#uses the path to get the list of file names and sorts them
def getfilelist(path):
    filelist = os.listdir(path)
    filelist.sort()
    return filelist

#gets the file names and modifies them
def newnames(filelist):
    newnamelist = []
    for image in filelist:
        try:
            #uses regex to search for numbers and a .JPG
            search = re.search(r'\d+\.JPG', image)
            numb = search.group(0)
            #transforms the image name and appends to new list
            number = numb.split(".")[0]
            newname = "PWP2024_000" + number + "D_DANIEL.JPG"
            newnamelist.append(newname)
        except:
            print(image)
    #returns new list of names
    return (newnamelist)

#adds extra 0's onto duplicated names
def unduplicate(newnamelist):
    oldlist = []
    unduplicatedlist = []
    for image in newnamelist:
        if image in unduplicatedlist:
            #counts how much instances of the name are behind it and adds that much 0's
            counts = oldlist.count(image)
            splitstring = image.split("_")
            splitstring[1] = "0" * counts + splitstring[1]
            newname = "_".join(splitstring)
            oldlist.append(image)
            unduplicatedlist.append(newname)
        else:
            unduplicatedlist.append(image)
            oldlist.append(image)
    #returns the fixed list
    return (unduplicatedlist)

#renames the files
def renamefiles(path, filelist, unduplicatedlist):
    for file in filelist:
        os.rename(path + "/" + file, path + "/" + unduplicatedlist[filelist.index(file)])
