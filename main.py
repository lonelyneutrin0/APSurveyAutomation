from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

SCOPES = "https://www.googleapis.com/auth/forms.body"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

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
while(1 > 0): 
  print("Input a course name!")
  name = input()
  # Request body for creating a form
  NEW_FORM = {
      "info": {
          "title": "AP " + name + " Survey",
          "documentTitle": "AP " + name +" Survey",
      }
  }

  #Section 1 
  question1 = { 
    "title": "Where did you find this survey?", 
    "questionItem": { 
      "question": { 
        "required": True, 
        "choiceQuestion": { 
          "type": "RADIO", 
          "options": [ 
            { "value": "AP Students Discord"}, 
            {"value": "Friend/Classmate"}, 
            {"value": "AProject Website"}, 
            {"value": "Reddit"},
            {"isOther": True}, 
          ]
        }
      }
    }
  }
  question2 = { 
    "title": "Have you taken the AP " + name + " exam?", 
    "questionItem": {
      "question": {
          "required": True, 
          "choiceQuestion": { 
            "type": "RADIO", 
            "options": [ 
              {"value": "Yes", "goToSectionId": "00000006"}, 
              {"value": "Not yet, but I will this year", "goToSectionId": "00000002"},
              {"value": "No","goToSectionId": "00000003"}
            ]
          }
      }
    } 
  }
  question3 = { 
    "title": "Select all other AP courses you have taken.", 
    "questionItem": { 
      "question": {
        "required": True, 
        "choiceQuestion": { 
          "type": "CHECKBOX",
          "options": [ 
            {"value": "African American Studies"},
            {"value": "Art History"}, 
            {"value": "Biology"}, 
            {"value": "Calculus AB"}, 
            {"value": "Calculus BC"},
            {"value": "Chemistry"},
            {"value": "Chinese Language and Culture"}, 
            {"value": "Comparative Government and Politics"}, 
            {"value": "Computer Science A"}, 
            {"value": "Computer Science Principles"}, 
            {"value": "Drawing"},
            {"value": "English Language and Composition"},
            {"value": "English Literature and Composition"},
            {"value": "Environmental Science"},
            {"value": "European History"},
            {"value": "French Language and Culture"},
            {"value": "German Language and Culture"},
            {"value": "Human Geography"},
            {"value": "Italian Language and Culture"},
            {"value": "Japanese Language and Culture"},
            {"value": "Latin"},
            {"value": "Macroeconomics"},
            {"value": "Microeconomics"},
            {"value": "Music Theory"},
            {"value": "Physics 1: Algebra Based"},
            {"value": "Physics 2: Algebra Based"},
            {"value": "Physics C: Electricity and Magnetism"},
            {"value": "Physics C: Mechanics"},
            {"value": "Precalculus"},
            {"value": "Psychology"},
            {"value": "Research"},
            {"value": "Seminar"},
            {"value": "Spanish Language and Culture"},
            {"value": "Spanish Literature and Culture"},
            {"value": "Statistics"},
            {"value": "Studio Art: 2-D Design"},
            {"value": "Studio Art: 3-D Design"},
            {"value": "United States Government and Politics"},
            {"value": "United States History"},
            {"value": "World History: Modern"},
          ]
        }
      }
    }
  }

  #Section 2
  question4 = {
    "title": "See you soon!",
    "questionItem": { 
      "question": { 
        "required": True, 
        "choiceQuestion": { 
          "type": "RADIO", 
          "options": [
            {"value": "I'll be sure to update my response after taking the exam!", "goToAction": "SUBMIT_FORM"},
          ]
        }
      }
    }
  }

  #Section 3
  question5 = { 
    "title": "Have you taken (or are currently taking/self studying) the AP " + name + " course?", 
    "questionItem": {
      "question": { 
        "required": True, 
        "choiceQuestion": { 
          "type": "RADIO", 
          "options": [ 
            {"value": "Yes", "goToSectionId": "00000005"},
            {"value": "No", "goToSectionId": "00000004"},
          ]
        }
      }
    }
  }

  #Section 4
  question6 = { 
    "title": "Do you intend to take AP " + name + " in the future?", 
    "questionItem": { 
      "question": { 
      "required": True, 
      "choiceQuestion": { 
        "type": "RADIO", 
        "options": [ 
          {"value": "Yes"},
          {"value": "No"},
          {"value": "Undecided"},
        ]
      }
      }
    }
  }
  question7 = { 
    "title": "Have you taken a non AP course that's roughly equivalent to AP " + name + ", such as one at a university?", 
    "questionItem": { 
      "question": {
        "required": True, 
        "choiceQuestion": { 
          "type": "RADIO", 
          "options": [
            {"value": "Yes"}, 
            {"value": "No"}
          ]
        }
      }
    }
  }
  question8 = { 
    "title": "Add anything you'd like to mention regarding whether you'll take AP "+ name +" in the future.",
    "questionItem": { 
      "question": {
        "required": False, 
        "textQuestion": { 
          "paragraph": True
        }
      }
    }
  }

  #Section 5
  question9 = { 
    "title": "Why did you not take the AP exam?", 
    "questionItem": {
      "question": { 
        "required": True, 
        "choiceQuestion": {
          "type": "RADIO", 
          "options": [ 
            {"value": "It's too expensive"},
            {"value": "I don't/didn't think I'd score well"},
            {"value": "I don't need the college credit"},
            {"value": "I don't enjoy AP " + name},
            {"value": "My school doesn't offer it"},
            {"value": "Too much additional time and commitment"},
            {"value": "Too many other exams"},
            {"isOther": True},
          ]
        }
      }
    }
  }

  #Section 6
  question10 = { 
    "title": "How hard did you expect AP " + name + " to be before taking the class?", 
    "questionItem": { 
      "question": { 
        "required": True, 
        "scaleQuestion": { 
          "low": 0, 
          "high": 5, 
          "lowLabel": "Very Easy",
          "highLabel": "Very Hard"
        }
      }
    }
  }
  question11 = { 
    "title": "What did you think was difficult or easy about the class?", 
    "questionItem": { 
      "question": { 
        "required": False, 
        "textQuestion": { 
          "paragraph": True
        }
      }
    }
  }
  question12 = { 
    "title": "Now that you've completed the course, were those feelings accurate?", 
    "questionItem": { 
      "question": {
        "required": True, 
        "choiceQuestion": { 
          "type": "RADIO", 
          "options": [ 
            {"value": "Yes"},
            {"value": "No"}, 
            {"isOther": True}, 
          ]
        }
      }
    }
  }
  question13 = { 
    "title": "Did you underestimate/overestimate the difficulty of any part of the course?", 
    "questionItem": { 
      "question": { 
        "required": False, 
        "textQuestion": { 
          "paragraph": False
        }
      }
    }
  }

  #Section 7 
  question14 = { 
    "title": "What year did you take the exam?", 
    "questionItem": { 
      "question": { 
        "required": True, 
        "choiceQuestion": { 
          "type": "RADIO", 
          "options": [ 
            {"value": "8th Grade"},
            {"value": "Freshman"},
            {"value": "Sophomore"},
            {"value": "Junior"},
            {"value": "Senior"},
            {"isOther": True},
          ]
        }
      }
    }
  }
  question15 = { 
    "title": "List any other resources that you'd recommend.", 
    "questionItem": { 
      "question": { 
        "required": False, 
        "textQuestion": { 
          "paragraph": True
        }
      }
    }
  } 
  question16 = { 
    "title": "How well prepared did you feel for your exam",
    "questionItem": { 
      "question": { 
        "required": True, 
        "scaleQuestion": { 
          "low": 0, 
          "high": 5, 
          "lowLabel": "Ill prepared", 
          "highLabel": "Very well prepared"
        }
      }
    }
  }
  question17 = { 
    "title": "What did you feel well-prepared for?",
    "questionItem": { 
      "question": { 
        "required": False, 
        "textQuestion": { 
          "paragraph": True
        }
      }
    }
  }
  question18 = { 
    "title": "What did you feel ill-prepared for?", 
    "questionItem": { 
      "question": { 
        "required": False, 
        "textQuestion": { 
          "paragraph": True
        }
      }
    }
  }
  question19 = { 
    "title": "Did your feelings accurately reflect your abilities while taking the test?", 
    "questionItem": { 
      "question": { 
        "required": True, 
        "choiceQuestion": { 
          "type": "RADIO", 
          "options": [ 
            {"value": "Yes"},
            {"value": "No"},
          ]
        }
      }
    }
  }
  question20 = { 
    "title": "Why were those units hard?",
    "questionItem": { 
      "question": { 
        "required": True, 
        "choiceQuestion": { 
          "type": "CHECKBOX", 
          "options": [ 
            {"value": "Too abstract"},
            {"value": "Too much content"},
            {"value": "Setting up the problems"},
            {"value": "Doing the problems"},
            {"value": "The other units were just relatively easier"},
            {"value": "Didn't review it enough"},
            {"isOther": True}
          ]
        }
      }
    }
  }
  question21 = { 
    "title": "Why were those units easy?",
    "questionItem": { 
      "question": { 
        "required": True, 
        "choiceQuestion": { 
          "type": "CHECKBOX", 
          "options": [ 
            {"value": "Less abstract than others"},
            {"value": "Comparatively less much content"},
            {"value": "Setting up the problems was easier"},
            {"value": "Solving the problems was easier"},
            {"value": "The other units were just relatively harder"},
            {"value": "Spent lots of time reviewing"},
            {"isOther": True}
          ]
        }
      }
    }
  }
  question22 = { 
    "title": "How did you feel about the pace of the course?", 
    "questionItem": { 
      "question": { 
        "required": True, 
        "scaleQuestion": { 
          "low": 0, 
          "high": 5, 
          "lowLabel": "very slow", 
          "highLabel": "very high"
        }
      }
    }
  }
  question23 = { 
    "title": "How did you feel about time management during the exam?", 
    "questionItem": { 
      "question": { 
        "required": True, 
        "scaleQuestion": { 
          "low": 0, 
          "high": 5, 
          "lowLabel": "Very comfortable", 
          "highLabel": "Could not finish"
        }
      }
    }
  }
  question24 = { 
    "title": "What did you score on the AP " + name + " exam?", 
    "questionItem": { 
      "question": { 
        "required": True, 
        "scaleQuestion": { 
          "low": 1, 
          "high": 5
        }
      }
    }
  }
  question25 = { 
    "title": "If you could go back in time to the start of this year and give your past self some advice for AP "+ name+", what would you say?",
    "questionItem": { 
      "question": { 
        "required": False, 
        "textQuestion": { 
          "paragraph": True
        }
      }
    }
  }
  question26 = { 
    "title": "How did you primarily prepare for the exam?", 
    "questionItem": { 
      "question": { 
        "required": True, 
        "choiceQuestion": { 
          "type": "RADIO", 
          "options": [ 
            {"value": "Course at my high school", "goToSectionId": "00000009"},
            {"value": "Online course (with teacher)", "goToSectionId": "00000009"},
            {"value": "Self study", "goToSectionId": "00000008"},
            {"isOther": True, "goToSectionId": "00000010"}
          ]
        }
      }
    }
  }

  #Section 8
  question27 = { 
    "title": "How easy is it to self study AP "+ name +"?", 
    "questionItem": { 
      "question": { 
        "required": True, 
        "scaleQuestion": { 
          "low":0, 
          "high":5, 
          "lowLabel": "Very difficult", 
          "highLabel": "Very easy"
        }
      }
    }
  }
  question28 = { 
    "title": "What elements did you find easy, and what elements did you find difficult to self study?", 
    "questionItem": { 
      "question": { 
        "required": False, 
        "textQuestion": { 
          "paragraph": True
        }
      }
    }
  }
  question29 = { 
    "title": "How many hours a week did you dedicate to self-studying AP " + name+"(typically, not before the exam)", 
    "questionItem": { 
      "question": { 
        "required":True, 
        "textQuestion": { 
          "paragraph": False
        }
      }
    }
  }
  question30 = { 
    "title": "How many weeks did you spend reviewing (not learning) for the AP " + name+" as you self-studied?", 
    "questionItem": { 
      "question": { 
        "required": False,
        "textQuestion": { 
          "paragraph": False
        }
      }
    }
  }
  question31 = {
    "title": "If you self studied, what would your advice be for others who wish to do the same?", 
    "questionItem": { 
    "question": { 
      "required": False, 
      "textQuestion": { 
        "paragraph": False
      }
    }   
    }
  }

  #Section 9
  question32 = { 
    "title": "Rate the quality of your teacher's preparation for the exam.", 
    "questionItem": { 
      "question": { 
        "required": True, 
        "scaleQuestion": { 
          "low": 0, 
          "high": 5, 
          "lowLabel": "Very Poor", 
          "highLabel": "Excellent"
        }
      }
    }
  }
  question33 = { 
    "title": "What did your teacher prepare you well for? What could they have done a better job preparing students for?", 
    "questionItem": { 
      "question": { 
        "required": False, 
        "textQuestion": { 
          "paragraph": True
        }
      }
    }
  }
  question34 = { 
    "title": "How many weeks did you dedicate to studying for the AP " + name + " exam with a teacher?", 
    "questionItem": { 
      "question": { 
        "required": False, 
        "textQuestion": { 
          "paragraph": False
        }
      }
    } 
  }
  question35 = { 
    "title": "How many weeks did you dedicate to studying for the AP " + name + " exam outside of the classroom?", 
    "description": "We're interested in the normal course workload--not the hours you put in nearing exam day.", 
    "questionItem": { 
      "question": { 
        "required": False,  
        "textQuestion": { 
          "paragraph": False
        }
      }
    }
  }
  question36 = { 
    "title": "Did you find it necessary to seek additional help outside of your regular class time? If so, how did you access this help?", 
    "questionItem": { 
      "question": { 
        "required": False, 
        "textQuestion": { 
          "paragraph": True
        }
      }
    }
  }

  #Section 11
  question37 = { 
    "title": "Would you say this course leans more towards theory or application?", 
    "questionItem": { 
      "question": { 
        "required": True, 
        "choiceQuestion": { 
          "type": "RADIO", 
          "options": [
            {"value": "Theory"},
            {"value": "Application"},
          ]
        }
      }
    }
  }
  question38 = { 
    "title": "Would you say this exam leans more towards theory or application?", 
    "questionItem": { 
      "question": { 
        "required": True, 
        "choiceQuestion": { 
          "type": "RADIO", 
          "options": [
            {"value": "Theory"},
            {"value": "Application"},
          ]
        }
      }
    }
  }
  question39 = { 
    "title": "How hard is AP " + name+ "?", 
    "questionItem": { 
      "question": { 
        "required": True, 
        "scaleQuestion": { 
          "low": 0, 
          "high": 5, 
          "lowLabel": "Very Easy", 
          "highLabel": "Very Hard"
        }
      }
    }
  }
  question40 = { 
    "title": "Is AP "+name+ " fun? What units did you have most fun learning? What specific elements of the course appealed to you?", 
    "questionItem": { 
      "question": { 
        "required": False, 
        "textQuestion": { 
          "paragraph": True
        }
      }
    }
  }
  question41 = { 
    "title": "Do you have any additional words of wisdom to future students?", 
    "description": "(Optional). Keep it concise (just one or two points), and watch your grammar. Quality responses will be selected for the FAQ document.", 
    "questionItem": { 
      "question": { 
        "required": False, 
        "textQuestion": { 
          "paragraph": True
        }
      }
    }
  }
  question42 = { 
    "title": "Did you find group study sessions or study groups helpful in preparing for the AP exam?", 
    "questionItem": { 
      "question": { 
        "required": True, 
        "choiceQuestion": { 
          "type": "RADIO", 
          "options": [ 
            {"value": "Yes"},
            {"value": "No"},
            {"value": "I didn't use study groups/sessions"}, 
          ]
        }
      }
    }
  }
  question43 = { 
    "title": "Did you use AI as a learning tool?", 
    "questionItem": { 
      "question": { 
        "required": True, 
        "choiceQuestion": { 
          "type": "RADIO", 
          "options": [ 
            {"value": "Yes", "goToSectionId": "00000011"},
            {"value": "No", "goToSectionId": "00000012"},
          ]
        }
      }
    }
  }

  #Section 12
  question44 = { 
    "title": "Which AI model did you use?", 
    "questionItem": { 
      "question": { 
        "required": True, 
        "choiceQuestion": { 
          "type": "CHECKBOX", 
          "options": [ 
            {"value": "ChatGPT"},
            {"value": "Google Gemini/Bard"},
            {"value": "Grok"},
            {"value": "Claude"},
            {"isOther": True},
          ]
        }
      }
    }
  }
  question45 = { 
    "title": "How useful was it on a scale of 1 to 10?", 
    "questionItem": { 
      "question": { 
        "required": True, 
        "scaleQuestion": { 
          "low": 1, 
          "high": 10, 
          "lowLabel": "Not useful", 
          "highLabel": "Very useful"
        }
      }
    }
  }
  question46 = { 
    "title": "What was AI good at explaining, and where was it lackluster?", 
    "questionItem": { 
      "question": { 
        "required": False, 
        "textQuestion": { 
          "paragraph": True
        }
      }
    }
  }

  #Section 13
  question47 = { 
    "title": "Have you taken/Are you currently pursuing higher studies in a field adjacent to AP " + name + "?", 
    "questionItem": {
      "question": { 
        "required": True, 
        "choiceQuestion": { 
          "type": "RADIO", 
          "options": [ 
          {"value": "Yes", "goToSectionId": "00000013"},
          {"value": "No", "goToAction": "SUBMIT_FORM"},
        ]
        }
        
      }
    }
  }

  #Section 14
  question48 = { 
    "title": "How well did the coursework transfer to your higher studies?", 
    "questionItem": { 
      "question": { 
        "required": True, 
        "scaleQuestion": { 
          "low": 1, 
          "high": 5, 
          "lowLabel": "Very poorly", 
          "highLabel": "Extremely well"
        }
      }
    }
  }
  question49 = { 
    "title": "Explain the above response", 
    "questionItem": { 
      "question": { 
        "required": False, 
        "textQuestion": { 
          "paragraph": True
        }
      }
    }
  }
  # Request body to add a multiple-choice question
  NEW_QUESTION = {
    #Section 1
      "requests": [
        { 
          "createItem": { 
            "item": question1,
            "location": {"index": 0}
          }
        },
        { 
          "createItem": { 
            "item": question3,
            "location": {"index": 1}
          }
        },
    
    #Section 2
        { 
          "createItem": { 
              "item": {
              "title": "Update Response", 
              "itemId": "00000002",
              "description": "That's alright-thanks anyway. \n\n This survey is for people who have already taken the exam. Please return here after you take the exam so you can update your response and help future students prepare.",
              "pageBreakItem": {}, 
            }, 
            "location": {"index": 2}
          }
        },
        { 
          "createItem": { 
            "item": question4,
            "location": {"index": 3}
          }
        },
    
    #Section 3
              { 
          "createItem": { 
              "item": {
                "title": "AP " + name+ " Interest", 
                "itemId": "00000003",
              "pageBreakItem": {}
            }, 
            "location": {"index": 4}
          }
        },

    #Section 4
              { 
          "createItem": { 
              "item": {
                "title": "Course Interest", 
                "itemId": "00000004",
              "pageBreakItem": {}
            }, 
            "location": {"index": 5}
          }
        },
        { 
          "createItem": { 
            "item": question6,
            "location": {"index": 6}
          }
        },
        { 
          "createItem": { 
            "item": question7,
            "location": {"index": 7}
          }
        },
        { 
          "createItem": { 
            "item": question8,
            "location": {"index": 8}
          }
        },


    #Section 5
              { 
          "createItem": { 
              "item": {
                "title": "Exam Interest",
                  "itemId": "00000005",
              "pageBreakItem": {}
            }, 
            "location": {"index": 9}
          }
        },
        { 
          "createItem": { 
            "item": question9,
            "location": {"index": 10}
          }
        },
    
    #Section 6
              { 
          "createItem": { 
              "item": {
                "title": "Before the Course",
                  "itemId": "00000006",
              "pageBreakItem": {}
            }, 
            "location": {"index": 11}
          }
        },
        { 
          "createItem": { 
            "item": question10,
            "location": {"index": 12}
          }
        },
        { 
          "createItem": { 
            "item": question11,
            "location": {"index": 13}
          }
        },
        { 
          "createItem": { 
            "item": question12,
            "location": {"index": 14}
          }
        },
        { 
          "createItem": { 
            "item": question13,
            "location": {"index": 15}
          }
        },
        
    
    #Section 7
              { 
          "createItem": { 
              "item": {
                "title": "Preparation",
                  "itemId": "00000007",
              "pageBreakItem": {}
            }, 
            "location": {"index": 16}
          }
        },
        { 
          "createItem": { 
            "item": question14,
            "location": {"index": 17}
          }
        },
        { 
          "createItem": { 
            "item": question15,
            "location": {"index": 18}
          }
        },
        { 
          "createItem": { 
            "item": question16,
            "location": {"index": 19}
          }
        },
        { 
          "createItem": { 
            "item": question17,
            "location": {"index": 20}
          }
        },
        { 
          "createItem": { 
            "item": question18,
            "location": {"index": 21}
          }
        },
        { 
          "createItem": { 
            "item": question19,
            "location": {"index": 22}
          }
        },
        { 
          "createItem": { 
            "item": question20,
            "location": {"index": 23}
          }
        },
        { 
          "createItem": { 
            "item": question21,
            "location": {"index": 24}
          }
        },
        { 
          "createItem": { 
            "item": question22,
            "location": {"index": 25}
          }
        },
        { 
          "createItem": { 
            "item": question23,
            "location": {"index": 26}
          }
        },
        { 
          "createItem": { 
            "item": question24,
            "location": {"index": 27}
          }
        },
        { 
          "createItem": { 
            "item": question25,
            "location": {"index": 28}
          }
        },
        

    #Section 8
              { 
          "createItem": { 
              "item": {
                "title": "Self Study",
                  "itemId": "00000008",
              "pageBreakItem": {}
            }, 
            "location": {"index": 29}
          }
        },
        { 
          "createItem": { 
            "item": question27,
            "location": {"index": 30}
          }
        },
        { 
          "createItem": { 
            "item": question28,
            "location": {"index": 31}
          }
        },
        { 
          "createItem": { 
            "item": question29,
            "location": {"index": 32}
          }
        },
        { 
          "createItem": { 
            "item": question30,
            "location": {"index": 33}
          }
        },
        { 
          "createItem": { 
            "item": question31,
            "location": {"index": 34}
          }
        },

    
    #Section 9
              { 
          "createItem": { 
              "item": {
                "title": "Teacher Evaluation", 
                  "itemId": "00000009",
              "pageBreakItem": {}
            }, 
            "location": {"index": 35}
          }
        },
        { 
          "createItem": { 
            "item": question32,
            "location": {"index": 36}
          }
        },
        { 
          "createItem": { 
            "item": question33,
            "location": {"index": 37}
          }
        },
        { 
          "createItem": { 
            "item": question34,
            "location": {"index": 38}
          }
        },
        { 
          "createItem": { 
            "item": question35,
            "location": {"index": 39}
          }
        },
        { 
          "createItem": { 
            "item": question36,
            "location": {"index": 40}
          }
        },

    #Section 10
              { 
          "createItem": { 
              "item": {
                "title": "Miscellaneous Questions", 
                  "itemId": "00000010",
              "pageBreakItem": {}
            }, 
            "location": {"index": 41}
          }
        },
        { 
          "createItem": { 
            "item": question37,
            "location": {"index": 42}
          }
        },
        { 
          "createItem": { 
            "item": question38,
            "location": {"index": 43}
          }
        },
        { 
          "createItem": { 
            "item": question39,
            "location": {"index": 44}
          }
        },
        { 
          "createItem": { 
            "item": question40,
            "location": {"index": 45}
          }
        },
        {
          "createItem": { 
            "item": question41,
            "location": {"index": 46}
          }
        },
        { 
          "createItem": { 
            "item": question42,
            "location": {"index": 47}
          }
        },
        
    

    #Section 11
              { 
          "createItem": { 
              "item": {
                "title": "AI Usage",
                  "itemId": "00000011",
              "pageBreakItem": {}
            }, 
            "location": {"index": 48}
          }
        },
        { 
          "createItem": { 
            "item": question44,
            "location": {"index": 49}
          }
        },
        { 
          "createItem": { 
            "item": question45,
            "location": {"index": 50}
          }
        },
        { 
          "createItem": { 
            "item": question46,
            "location": {"index": 51}
          }
        },

    
    #Section 12 
              { 
          "createItem": { 
              "item": {
                "title": "post-AP " + name,
                  "itemId": "00000012",
              "pageBreakItem": {}
            }, 
            "location": {"index": 52}
          }
        },
        { 
          "createItem": { 
            "item": { 
              "title": "Thanks for your help!", 
              "description": "The data from this survey will be used to help future AP " + name+ " students. Please share this survey with your friends!", 
              "textItem": {}
            }, 
            "location": {"index": 53}
          }
        },
    
    #Section 13
              { 
          "createItem": { 
              "item": {
                "title": "post-AP " + name,
                  "itemId": "00000013",
              "pageBreakItem": {}
            }, 
            "location": {"index": 54}
          }
        },
        { 
          "createItem": { 
            "item": question48,
            "location": {"index": 55}
          }
        },
        { 
          "createItem": { 
            "item": question49,
            "location": {"index": 56}
          }
        },
        { 
          "createItem": { 
            "item": { 
              "title": "Thanks for your help!", 
              "description": "The data from this survey will be used to help future AP " + name+ " students. Please share this survey with your friends!", 
              "textItem": {}
            },
            "location": {"index": 57}
          }
          
        },

        #Conditional Response Questions (these require the sections to be generated for their proper functioning)
          { 
          "createItem": { 
            "item": question2,
            "location": {"index": 1}
          }
        },
        { 
          "createItem": { 
            "item": question5,
            "location": {"index": 6}
          }
        },
        { 
          "createItem": { 
            "item": question26,
            "location": {"index": 31}
          }
        },
        { 
          "createItem": { 
            "item": question43,
            "location": {"index": 51}
          }
        },
        { 
          "createItem": { 
            "item": question47,
            "location": {"index": 57}
          }
        },
          { 
            "updateFormInfo": { 
              "info": { 
                "title": "AP " + name + " Survey",
                "description": "Thank you for participating in this survey! This survey is part of a larger initiative called AProject, where we gather responses to frequently asked questions from past AP students and experienced subject helpers. Using this data, we create high-quality FAQ documents containing information on the best resources for a course, its difficulty level, compatibility with other AP courses, and more. This will greatly assist future AP students in their academic journey. Although the survey contains numerous free-response questions, most of them are optional. \n\nThis project is a massive undertaking and we are always looking for more help. For more information on how to apply, check out the TLDR page of our coda.io document [https://coda.io/d/AP-roject-Official-Information-Document_d3ClwsuYb2A/TL-DR-AP-roject-Quick-Summary-and-FAQs_su4i8#_luDJj]. Your help would be extremely beneficial for improving our productivity."
              }, 
              "updateMask": "title, description"
            }
          }
      ]
  }

  # Creates the initial form
  result = form_service.forms().create(body=NEW_FORM).execute()

  # Adds the question to the form
  question_setting = (
      form_service.forms()
      .batchUpdate(formId=result["formId"], body=NEW_QUESTION)
      .execute()
  )

  # Prints the result to show the question has been added
  get_result = form_service.forms().get(formId=result["formId"]).execute()
  print("AP " + name+ " Survey Created!")