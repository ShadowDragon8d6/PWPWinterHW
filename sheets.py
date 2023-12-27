import pygsheets
import pandas as pd

def importdata(list,sheet,sheetnum,column,title):
  authorize = pygsheets.authorize(service_file='/Users/caioc/Downloads/creds.json')
  data = pd.DataFrame()
  data[title] = list
  sheet = authorize.open(sheet)
  actualsheet = sheet[sheetnum]
  actualsheet.set_dataframe(data,(1,column))

