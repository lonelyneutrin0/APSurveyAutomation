from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools
import random 
import sys 
import csv
sys.path.append('c:\\Users\\hkbel\\Desktop\\APSurveyAutomation')
import questionsStorage
SCOPES = ["https://www.googleapis.com/auth/forms.body", "https://www.googleapis.com/auth/documents", "https://www.googleapis.com/auth/drive"]
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"
result_dict = []
result_fields = ["name", "formId"]
filename = 'formIds.csv'
store = file.Storage("token.json")
creds = None
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
def responseBody(obj, list): 
  
  return { 
      "createItem": { 
        "item": obj, 
        "location": {"index": position(obj, list, questions)}
      }
    }
name = ''
while(name != "finish"): 
  print("Input a course name!")
  name = input()
  if(name == 'finish'): continue
  questions = questionsStorage.questionGen(name)
  for arr in questions:
    for x in arr: 
        if("questionItem" not in x): continue
        y = x["questionItem"]
        z = y["question"]
        if("textQuestion" in y["question"] and z["required"] == False): 
            x["description"] = " (Optional)" if "description" not in x else x["description"] + " (Optional)"
  
  # Request body for creating a form
  NEW_FORM = {
      "info":   
      {
          "title": "AP " + name + " Survey",
          "documentTitle": "AP " + name +" Survey",
      }
    }
  #Compiling the final response body
  i = 0
  questionBody = [] 
  for element in questions: 
    headers = [ 
    { 
    "updateFormInfo": { 
        "info": { 
        "title": "AP " + name + " Survey",
        "description": "Thank you for participating in this survey! This survey is part of a larger initiative called AProject, where we gather responses to frequently asked questions from past AP students and experienced subject helpers. Using this data, we create high-quality FAQ documents containing information on the best resources for a course, its difficulty level, compatibility with other AP courses, and more. This will greatly assist future AP students in their academic journey. Although the survey contains numerous free-response questions, most of them are optional. \n\nThis project is a massive undertaking and we are always looking for more help. For more information on how to apply, check out the TLDR page of our coda.io document [https://coda.io/d/AP-roject-Official-Information-Document_d3ClwsuYb2A/TL-DR-AP-roject-Quick-Summary-and-FAQs_su4i8#_luDJj]. Your help would be extremely beneficial for improving our productivity."
        }, 
        "updateMask": "title, description"
    }
    }, 
    { 
    "createItem": { 
        "item": {
        "title": "Update Response", 
        "itemId": "00000002",
        "description": "That's alright-thanks anyway. \n\n This survey is for people who have already taken the exam. Please return here after you take the exam so you can update your response and help future students prepare.",
        "pageBreakItem": {}, 
    }, 
    "location": {"index":  len(questionBody) -1}
    }
    },
    { 
    "createItem": { 
        "item": {
        "title": "AP " + name+ " Interest", 
        "itemId": "00000003",
        "pageBreakItem": {}
    }, 
    "location": {"index":  len(questionBody) -1}
    }
    },
    { 
    "createItem": { 
        "item": {
            "title": "Course Interest", 
            "itemId": "00000004",
        "pageBreakItem": {}
        }, 
        "location": {"index":  len(questionBody) -1}
    }
    },
    { 
    "createItem": { 
        "item": {
            "title": "Exam Interest",
            "itemId": "00000005",
        "pageBreakItem": {}
        }, 
        "location": {"index":   len(questionBody) -1}
    }
    },
    { 
    "createItem": { 
        "item": {
            "title": "Before the Course",
            "itemId": "00000006",
        "pageBreakItem": {}
        }, 
        "location": {"index":   len(questionBody) -1}
    }
    },
    { 
    "createItem": { 
        "item": {
        "title": "Preparation",
            "itemId": "00000007",
        "pageBreakItem": {}
    }, 
    "location": {"index":   len(questionBody) -1}
    }
    }, 
    { 
    "createItem": { 
        "item": {
            "title": "Self Study",
            "itemId": "00000008",
        "pageBreakItem": {}
        }, 
        "location": {"index":   len(questionBody) -1}
    }
    },   
    { 
    "createItem": { 
        "item": {
            "title": "Teacher Evaluation", 
            "itemId": "00000009",
        "pageBreakItem": {}
        }, 
        "location": {"index":   len(questionBody) -1}
    }
    },
    { 
    "createItem": { 
        "item": {
        "title": "Miscellaneous Questions", 
            "itemId": "0000001",
        "pageBreakItem": {}
    }, 
    "location": {"index":   len(questionBody) -1}
    }
    },
    { 
    "createItem": { 
        "item": {
        "title": "AI Usage",
            "itemId": "00000011",
        "pageBreakItem": {}
    }, 
    "location": {"index":  len(questionBody) -1}
    }
    },
    { 
    "createItem": { 
        "item": {
        "title": "post-AP " + name,
        "itemId": "00000012",
        "pageBreakItem": {}
    }, 
    "location": {"index":  len(questionBody) -1}
    }
    },
    { 
    "createItem": { 
        "item": {
            "title": "post-AP " + name,
            "itemId": "00000013",
        "pageBreakItem": {}
        }, 
        "location": {"index":   len(questionBody) -1}
    }
    },
  ]
    questionBody.append(headers[i]) 

    for obj in element: 
      questionBody.append(responseBody(obj, element))
    i += 1
    
  finalBody = { 
    "requests": questionBody
  }
  result = form_service.forms().create(body=NEW_FORM).execute()
  
  # Adds the question to the form
  question_setting = (
      form_service.forms()
      .batchUpdate(formId=result["formId"], body=finalBody)
      .execute()
  )
  
  # Prints the result to show the question has been added
  get_result = form_service.forms().get(formId=result["formId"]).execute()
  result_dict.append({"name": name, "formId": result["formId"]})
  
  print("AP " + name+ " Survey Created!")
with open(filename, 'w') as csvFile: 
    writer = csv.DictWriter(csvFile, fieldnames=result_fields)
    writer.writeheader()
    writer.writerows(result_dict)

