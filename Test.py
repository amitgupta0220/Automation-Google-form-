import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from file_utils import write_csv
data = []
def getMail():
        scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('WEBAPP-07c5da9a07a4.json',scope)
        gc = gspread.authorize(credentials)
        sheet = gc.open("Results").sheet1
        email = sheet.col_values(2)
        #name = sheet.col_values(3)
        limit=0
        for j in range(1,sheet.row_count):
                limit = limit+1
                if sheet.cell(row=j,col = 3).value == '':
                        break
        limit = limit-1

        for i in range(1,limit):
                data.append({email[i]})
                write_csv(data)



