from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools
import random 
import sys 
import csv
import json
sys.path.append('c:\\Users\\hkbel\\Desktop\\APSurveyAutomation')
import questionsStorage
SCOPES = ["https://www.googleapis.com/auth/forms.body", "https://www.googleapis.com/auth/documents", "https://www.googleapis.com/auth/drive"]
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"
result_dict = []
result_fields = ["name", "formId"]
filename = 'formIds.csv'
store = file.Storage("token.json")
creds = store.get()
if not creds or creds.invalid:
  flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
  creds = tools.run_flow(flow, store)

form_service = discovery.build(
    "forms",
    "v1",
    http=creds.authorize(Http()),
    discoveryServiceUrl=DISCOVERY_DOC,
    static_discovery=False,
)
#Utility Functions
def position(obj, list, matrix): 
  pos = 0
  for i in range(matrix.index(list)): 
    pos += len(matrix[i]) + 1
  pos += matrix[matrix.index(list)].index(obj)
  return pos 

with open("formIds.csv", 'r') as data:
    name = ''
    questionBody = []
    questionBody.append({
              "deleteItem": { 
                 "location": {"index": 53}
              }
           })
    for line in csv.DictReader(data):
        i = 0
        finalBody = { 
            "requests": questionBody
        }
        with open('data.json', 'w') as f:
            json.dump(questionBody, f)
        
        question_setting = (
                form_service.forms()
                .batchUpdate(formId=line['formId'], body=finalBody)
                .execute()
            )
print("Done!")