import os
import re


def getfilelist(path):
    filelist = os.listdir(path)
    filelist.sort()
    return filelist


def newnames(filelist):
    newnamelist = []
    for image in filelist:
        try:
            search = re.search(r'\d+\.JPG', image)
            numb = search.group(0)
            number = numb.split(".")[0]
            newname = "PWP2024_000" + number + "D_DANIEL.JPG"
            newnamelist.append(newname)
        except:
            print(image)
    return (newnamelist)


def unduplicate(newnamelist):
    oldlist = []
    unduplicatedlist = []
    for image in newnamelist:
        if image in unduplicatedlist:
            counts = oldlist.count(image)
            splitstring = image.split("_")
            splitstring[1] = "0" * counts + splitstring[1]
            newname = "_".join(splitstring)
            oldlist.append(image)
            unduplicatedlist.append(newname)
        else:
            unduplicatedlist.append(image)
            oldlist.append(image)
    return (unduplicatedlist)


def renamefiles(path, filelist, unduplicatedlist):
    for file in filelist:
        os.rename(path + "/" + file, path + "/" + unduplicatedlist[filelist.index(file)])
