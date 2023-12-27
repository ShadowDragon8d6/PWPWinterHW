
from sheets import importdata
from filerenamer import *
path = "/Users/caioc/Desktop/PWP2022"

filelist = getfilelist(path)

newnamelist = newnames(filelist)

unduplicatedlist = unduplicate(newnamelist)



renamefiles(path,filelist,unduplicatedlist)

importdata(filelist,"PWP Winter HW",0,1,"Original Names")
importdata(unduplicatedlist,"PWP Winter HW",0,2,"New Names")