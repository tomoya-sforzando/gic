#!/usr/bin/env python3
from GoogleSpreadsheets import GoogleSpreadsheets
from GithubConverter import GithubConverter

if __name__ == '__main__':
    sheet = GoogleSpreadsheets()
    converter = GithubConverter()

    # check columns of google_spreadsheets

    # create issues
    # for issue in sheet.get_issues():
    #     title = issue['title']
    #     description = issue['description']
    #     assignees = issue['assignees']
    #     milestone = issue['milestone']
    #     label = issue['label']
    #
    #     converter.create_issue(title, description, assignees, milestone, label)
