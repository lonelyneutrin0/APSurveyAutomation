import os.path
import sys 
sys.path.append('c:\\Users\\hkbel\\Desktop\\APSurveyAutomation')
import questionsStorage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client import file
import json
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/forms.body", "https://www.googleapis.com/auth/documents", "https://www.googleapis.com/auth/drive"]

requests = [] 
headings = [ 
  {
  "insertText": { 
        "location": {"index": 1}, 
        'text':  "ABOUT\n",
        }
  },
  {
  "insertText": { 
        "location": {"index": 1}, 
        'text': "FEEDBACK\n",
        }
  },
  {
  "insertText": { 
        "location": {"index": 1}, 
        'text': "TABLE OF CONTENTS\n",
        }
  },
  {
  "insertText": { 
        "location": {"index": 1}, 
        'text': "INTRODUCTION\n",
        }
  },
  {
  "insertText": { 
        "location": {"index": 1}, 
        'text': "RESOURCES\n",
        }
  },
  {
  "insertText": { 
        "location": {"index": 1}, 
        'text': "COURSE DIFFICULTY\n",
        }
  },
  {
  "insertText": { 
        "location": {"index": 1}, 
        'text': "QUESTIONS AND ETIQUETTE\n",
        }
  },
  {
  "insertText": { 
        "location": {"index": 1}, 
        'text': "PREREQUISITES\n",
        }
  },
  {
  "insertText": { 
        "location": {"index": 1}, 
        'text': "SELF STUDYING\n",
        }
  },
  {
  "insertText": { 
        "location": {"index": 1}, 
        'text': "MISCELLANEOUS\n",
        }
  },
  {
  "insertText": { 
        "location": {"index": 1}, 
        'text': "CONCLUSION\n"
        }
  },
  {
  "insertText": { 
        "location": {"index": 1}, 
        'text': "AFTER AP\n"
        }
  },
           
]
def position(obj, list, matrix): 
      pos = 0
      for i in range(matrix.index(list)): 
        pos += len(matrix[i]) + 1
      pos += matrix[matrix.index(list)].index(obj)
      return pos 
def responseBody(obj, list): 
    return { 
    "insertText": { 
    "location": {"index": 1}, 
    'text': obj + "\n"
    }
}


def main():
  """Shows basic usage of the Docs API.cls
  Prints the title of a sample document.
  """
  store = file.Storage("token.json")
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())
  
  try:
    print("Enter a course name!")
    name = input()
    
    #Question array processing
    
    formQuestions = questionsStorage.questionGen(name)
    #map the questions to a list of their titles 
    questions = [] 
    for x in formQuestions: 
        questions.append(list(map(lambda x: x["title"], x)))
    i = 0
    for x in questions:
        requests.append(headings[i])  
        i = i+1 if i < len(headings)-1 else 0 
        for y in x: 
            requests.append(responseBody(y, x))

    
    service = build("docs", "v1", credentials=creds)
    # Retrieve the documents contents from the Docs service.
    title = 'AP ' + name + " Frequently Asked Questions"
    body = {
        'title': title, 
    }
    final_requests = requests[::-1]
    doc = service.documents() \
        .create(body=body).execute()
    print('Created document with title: {0}'.format(doc.get('title')))
    DOCUMENT_ID = doc.get('documentId')
    
    
    result = service.documents().batchUpdate(
    documentId=DOCUMENT_ID, body={'requests': final_requests}).execute()
  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()