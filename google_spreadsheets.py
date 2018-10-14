from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# If modifying these scopes, delete the file token.json.
scopes = 'https://www.googleapis.com/auth/spreadsheets.readonly'


def main():
    store = file.Storage('token.json')
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', scopes)
        credentials = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=credentials.authorize(Http()))

    # Call the Sheets API
    spreadsheet_id = os.environ.get('SPREADSHEET_ID')
    range_of_sheet = 'A1:F20'
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id,
                                                range=range_of_sheet).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            print(row)


if __name__ == '__main__':
    main()
