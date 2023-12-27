#imports needed libraries
import pygsheets
import pandas as pd

def importdata(list,sheet,sheetnum,column,title):
  #gets authorization
  authorize = pygsheets.authorize(service_file='/Users/caioc/Downloads/creds.json')
  #creates a dataframe
  data = pd.DataFrame()
  #creates a column with the inputed title as the title and inputed list as the data
  data[title] = list
  #opens the sheet with the given title
  sheet = authorize.open(sheet)
  #selectes the sheet number
  actualsheet = sheet[sheetnum]
  #inputs the data into the sheet
  actualsheet.set_dataframe(data,(1,column))

