#import functions from 
from sheets import *
from filerenamer import *

#path of the file
path = "/Users/caioc/Desktop/PWP2022"
#gets list of file names
filelist = getfilelist(path)
#edits the list of file names
newnamelist = newnames(filelist)
#fixes the list of file names
unduplicatedlist = unduplicate(newnamelist)

#renames the files

renamefiles(path,filelist,unduplicatedlist)
#imports the data
importdata(filelist,"PWP Winter HW",0,1,"Original Names")
importdata(unduplicatedlist,"PWP Winter HW",0,2,"New Names")