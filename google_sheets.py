
import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials



API_FILE = 'json файл от сервис аккаунта'
sheet_id = 'ID таблицы'


credentials = ServiceAccountCredentials.from_json_keyfile_name(
    API_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = googleapiclient.discovery.build('sheets', 'v4', http = httpAuth)

body =  {
    "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Ячейки по строкам",
             "majorDimension": "ROWS",
             "values": [["Значения", ""], ["", ""]]},
            {"range": "ячейки по колонкам",
             "majorDimension": "COLUMNS",
             "values": [["значение", ""],["", ""]]}
        ]
}

values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=sheet_id,
    body=body).execute()