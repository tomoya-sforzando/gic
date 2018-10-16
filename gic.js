function convertIssues() {
  spreadsheet = SpreadsheetApp.getActive()
  sheet = spreadsheet.getSheetByName('シート2')
  
  credential_data = sheet.getSheetValues(2, sheet.getLastColumn()-2, 1, 3)
  username = credential_data[0][0]
  repo = credential_data[0][1]
  token = credential_data[0][2]
  url = "https://api.github.com/repos/"+username+"/"+repo+"/issues?access_token="+token
  
  // set range for import
  first_row = 2 // 1 <= first_row <= sheet.getLastRow()
  last_row = 2  // first_row <= last_row <= sheet.getLastRow()
  
  values = sheet.getSheetValues(first_row, 1, last_row + 1 - first_row, sheet.getLastColumn())
  for (i=0; i < values.length; i++){
    payload = {
      title: values[i][3],
      body: '## 概要\n\n'+values[i][5]+'\n\n## タスク\n\n'+values[i][6]+'\n\n## 備考\n\n'+values[i][7],
    }
    
    if(values[i][8].split(',') != ''){
      merge(payload, {assignees: values[i][8].split(',')})
    }
    if(values[i][9].split(',') != ''){
      merge(payload, {labels: values[i][9].split(',')})
    }
    if(values[i][12] != ''){
      merge(payload, {milestone: values[i][12]})
    }
    
    sendToGithub(url, payload)
    Logger.log(payload)
  }
}

function sendToGithub(url, payload) {
  options = {
    "method": "post",
    "payload": JSON.stringify(payload)
  };
  return UrlFetchApp.fetch(url, options)
}

var merge = function (obj1, obj2) {
  if (!obj2) {
    obj2 = {}
  }
  for (var attrname in obj2) {
    if (obj2.hasOwnProperty(attrname)) {
      obj1[attrname] = obj2[attrname];
    }
  }
}