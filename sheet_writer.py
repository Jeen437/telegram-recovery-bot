import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def write_to_sheet(status, mood, note):
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_key("YOUR_SPREADSHEET_ID").sheet1
    today = datetime.now().strftime("%Y-%m-%d")
    day = len(sheet.get_all_values())
    sheet.append_row([today, day, status, mood, note])
