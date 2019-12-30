import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os

# Get envrionment varibles from .env file
load_dotenv()


def data_found(worksheet, value):
    """
    Function to determine if a cell is found or not in Google Sheets

    Parameters:
    worksheet (object): A Google sheet object that is to be searched
    value (str): A string that will be searched for in the Google Sheet

    Returns:
    bool: Returns True or False if a cell is found that contains the value string
    """

    try: 
        worksheet.find(value)
        return True
    except: # If value is not found an exception will be raised, this should be treated as a false result
        return False


# These are the Google APIs required to retrive items from Google Sheets
scope = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

# Configure the service account from the JSON provided by Google to use OAuth2
credentials = ServiceAccountCredentials.from_json_keyfile_name(os.getenv("SERVICE_ACCOUNT_KEY"), scope)

# Authenticate to Google Sheets using the gspread module
gc = gspread.authorize(credentials)

# Open the worksheet. Some herror handling would be good here for invalid sheet name
wks = gc.open('ReBorn').sheet1

# Send the worksheet to the data_found function to return true or false
print(data_found(wks,'Tokugawa Ieyasu'))

ServiceAccountCredentials