function convertIssues() {
  const spreadsheet = SpreadsheetApp.getActive()
  Logger.log(typeof spreadsheet)
  const sheet: any = spreadsheet.getSheetByName('シート2')

  const credential_data: string[][] = sheet.getSheetValues(
    2,
    sheet.getLastColumn() - 2,
    1,
    3
  )
  const username: string = credential_data[0][0]
  const repository: string = credential_data[0][1]
  const token: string = credential_data[0][2]
  const url: string =
    'https://api.github.com/repos/' +
    username +
    '/' +
    repository +
    '/issues?access_token=' +
    token

  // set range for import
  const first_row: number = 2 // 1 <= first_row <= sheet.getLastRow()
  const last_row: number = 2 // first_row <= last_row <= sheet.getLastRow()

  const values: string[][] = sheet.getSheetValues(
    first_row,
    1,
    last_row + 1 - first_row,
    sheet.getLastColumn()
  )
  for (let i = 0; i < values.length; i++) {
    const payload: { [key: string]: any } = {
      title: values[i][3],
      body: `## 概要\n\n${values[i][5]}\n\n## タスク\n\n${
        values[i][6]
      }\n\n## 備考\n\n${values[i][7]}`
    }

    if (values[i][8] != '') {
      mergePayload(payload, { assignees: values[i][8].split(',') })
    }
    if (values[i][9] != '') {
      mergePayload(payload, { labels: values[i][9].split(',') })
    }
    if (values[i][12] != '') {
      mergePayload(payload, { milestone: values[i][12] })
    } else {
      Logger.log(values[i][12])
    }

    sendToGithub(url, payload)
    Logger.log(payload)
  }
}

function sendToGithub(url: string, payload: { [key: string]: string }) {
  const options: { [key: string]: string } = {
    method: 'post',
    payload: JSON.stringify(payload)
  }
  return UrlFetchApp.fetch(url, options)
}

function mergePayload(
  obj1: { [key: string]: any },
  obj2: { [key: string]: any }
) {
  if (!obj2) {
    obj2 = {}
  }
  for (const attribute in obj2) {
    if (obj2.hasOwnProperty(attribute)) {
      obj1[attribute] = obj2[attribute]
    }
  }
}
