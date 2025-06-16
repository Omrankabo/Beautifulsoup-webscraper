import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def sheet_writer(df):
    # connecting to google sheet
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    #openning the sheet
    sheet = client.open("Books_scraped").sheet1

    #reading files
    # df = pd.read_csv("books.csv")

    #clearing previous data
    sheet.clear()

    #sending data to google sheet
    set_with_dataframe(sheet, df)

    print("DONE SENDING DATA TO GOOGLE SHEET ✅")

# sheet_writter()