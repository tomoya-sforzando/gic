#!/usr/bin/env python3
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from configparser import ConfigParser


class GoogleSpreadsheets:

    def __init__(self):

        config = ConfigParser()
        config.read('config.ini')

        # If modifying these scopes, delete the file token.json.
        scopes = 'https://www.googleapis.com/auth/spreadsheets.readonly'

        store = file.Storage('token.json')
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', scopes)
            credentials = tools.run_flow(flow, store)
        service = build('sheets', 'v4', http=credentials.authorize(Http()))

        # Call the Sheets API
        spreadsheet_id = config.get(__class__.__name__, 'spreadsheet_id')
        range_of_sheet = config.get(__class__.__name__,'range_of_sheet')
        result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id,
                                                    range=range_of_sheet).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
        else:
            print(len(values))
            for row in values:
                print(row)


if __name__ == '__main__':
    google_spreadsheets = GoogleSpreadsheets()
