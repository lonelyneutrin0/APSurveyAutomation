def questionGen(name): 
    return [
        [
            { 
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
                        { "value": "AP(roject) Instagram"}, 
                        {"value": "AP(roject) TikTok"},
                        {"isOther": True}, 
                    ]
                    }
                }
                }
            }, 
            { 
                "title": "Have you taken the AP " + name + " exam?", 
                "questionItem": {
                "question": {
                    "required": True, 
                    "choiceQuestion": { 
                        "type": "RADIO", 
                        "options": [ 
                        {"value": "Yes"}, 
                        {"value": "Not yet, but I will this year"},
                        {"value": "No"}
                        ]
                    }
                }
                } 
            },
            { 
                "title": "Select all other AP courses you have taken in the same year as AP " + name + ".", 
                "questionItem": { 
                "question": {
                    "required": False, 
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
                },
            { 
                "title": "How easy was it to balance this course with the other APs you took?", 
                "questionItem": { 
                "question": { 
                    "required": False, 
                    "scaleQuestion": { 
                    "low": 1, 
                    "high": 10, 
                    "lowLabel": "Very easy", 
                    "highLabel": "Very difficult"
                    }
                }
                }
            },
        ],
        #Section 2
        [
            {
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
            },
        ],
        #Section 3
        [
            { 
                "title": "Have you taken (or are currently taking/self studying) the AP " + name + " course?", 
                "questionItem": {
                "question": { 
                    "required": True, 
                    "choiceQuestion": { 
                    "type": "RADIO", 
                    "options": [ 
                        {"value": "Yes",},
                        {"value": "No",},
                    ]
                    }
                }
                }
            },
        ],
        #Section 4
        [ 
            { 
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
            },
            { 
                "title": "Have you taken a non AP course equivalent to AP " + name + ", such as one at a university?", 
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
            },
            { 
                "title": "Add anything you'd like to mention regarding whether you'll take AP "+ name +" in the future.",
                "questionItem": { 
                "question": {
                    "required": False, 
                    "textQuestion": { 
                    "paragraph": True
                    }
                }
                }
            },
        ],
        #Section 5
        [
            { 
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
            },
        ],
        #Section 6
        [
            { 
                "title": "How hard did you expect AP " + name + " to be before taking the class?", 
                "questionItem": { 
                "question": { 
                    "required": True, 
                    "scaleQuestion": { 
                    "low": 1, 
                    "high": 10, 
                    "lowLabel": "Very Easy",
                    "highLabel": "Very Hard"
                    }
                }
                }
            },
            { 
                "title": "What did you think would be difficult about the class before taking it?", 
                "questionItem": { 
                "question": { 
                    "required": False, 
                    "textQuestion": { 
                    "paragraph": True
                    }
                }
                }
            },
            { 
                "title": "What did you think would be easy about the class before taking it?", 
                "questionItem": { 
                "question": { 
                    "required": False, 
                    "textQuestion": { 
                    "paragraph": True
                    }
                }
                }
            },
            { 
                "title": "Now that you've completed the course, were those feelings accurate?", 
                "questionItem": { 
                "question": {
                    "required": False, 
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
            },
            { 
                "title": "Now that you've completed the course, what parts of the course would you say you misjudged the difficulty of?", 
                "questionItem": { 
                "question": { 
                    "required": False, 
                    "textQuestion": { 
                    "paragraph": False
                    }
                }
                }
            },
        ],
        #Section 7
        [ 
            { 
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
            },
            { 
                "title": "Elaborate on the resources used (ex: which YouTube channels?), and any additional resources used not listed above. Rate the difficulty of the problems of each of these resources as compared to the AP Exam. (Rate them as harder, easier or roughly the same difficulty)", 
                "questionItem": { 
                "question": { 
                    "required": False, 
                    "textQuestion": { 
                    "paragraph": True
                    }
                }
                }
            },
            { 
                "title": "How well prepared did you feel for your exam",
                "questionItem": { 
                "question": { 
                    "required": True, 
                    "scaleQuestion": { 
                    "low": 1, 
                    "high": 10, 
                    "lowLabel": "Ill prepared", 
                    "highLabel": "Very well prepared"
                    }
                }
                }
            },
            { 
                "title": "What did you feel well-prepared for?",
                "questionItem": { 
                "question": { 
                    "required": False, 
                    "textQuestion": { 
                    "paragraph": True
                    }
                }
                }
            },
            { 
                "title": "What did you feel ill-prepared for?", 
                "questionItem": { 
                "question": { 
                    "required": False, 
                    "textQuestion": { 
                    "paragraph": True
                    }
                }
                }
            },
            { 
                "title": "Did your feelings (your responses to the previous two questions) accurately reflect your abilities while taking the test?", 
                "questionItem": { 
                "question": { 
                    "required": False, 
                    "choiceQuestion": { 
                    "type": "RADIO", 
                    "options": [ 
                        {"value": "Yes"},
                        {"value": "No"},
                    ]
                    }
                }
                }
            },
            { 
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
            },
            { 
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
            },
            { 
                "title": "Rate the quality of your teacher's teaching style. We understand that sometimes it can be subjective, and that's why if you are paying attention and reading this question carefully, you would choose '1' to prove that you are paying attention and disregard everything else in this question. Rate your teacher on a scale of 1-10. If you are self studying, then rate this question yourself.", 
                "questionItem": { 
                "question": { 
                "required": True, 
                "scaleQuestion": { 
                "low": 1, 
                "high": 10, 
            }
            }
            }
            },
            { 
                "title": "What was the pace of the course in terms of weeks per unit?", 
                "questionItem": { 
                    "question": { 
                        "required": False, 
                        "textQuestion": { 
                            "paragraph": False
                        }
                    }
                }
            },
            { 
                "title": "How did you feel about the pace of the course?", 
                "questionItem": { 
                "question": { 
                    "required": True, 
                    "scaleQuestion": { 
                    "low": 1, 
                    "high": 10, 
                    "lowLabel": "Very slow", 
                    "highLabel": "Very fast"
                    }
                }
                }
            },
            { 
                "title": "How did you feel about time management during the exam?", 
                "questionItem": { 
                "question": { 
                    "required": True, 
                    "scaleQuestion": { 
                    "low": 1, 
                    "high": 10, 
                    "highLabel": "Very comfortable", 
                    "lowLabel": "Could not finish"
                    }
                }
                }
            },
            # { 
            #     "title": "What did you score on the AP " + name + " exam?", 
            #     "questionItem": { 
            #     "question": { 
            #         "required": True, 
            #         "scaleQuestion": { 
            #         "low": 1, 
            #         "high": 10
            #         }
            #     }
            #     }
            # },
            { 
                "title": "What did you score on the AP " + name + " exam?", 
                "description": "If you haven't received your score yet, please make sure to return to this survey and edit your response when you do!",
                "questionItem": { 
                "question": { 
                    "required": True, 
                    "choiceQuestion": { 
                    "type": "RADIO", 
                    "options": [ 
                        {"value": "1"},
                        {"value": "2"},
                        {"value": "3"},
                        {"value": "4"},
                        {"value": "5"},
                        {"value": "I haven't received my score yet"},
                    ]
                    }
                }
                }
            },
            { 
                "title": "How did you primarily prepare for the exam?", 
                "questionItem": { 
                "question": { 
                    "required": True, 
                    "choiceQuestion": { 
                    "type": "RADIO", 
                    "options": [ 
                        {"value": "Course at my high school", },
                        {"value": "Online course (with teacher)", },
                        {"value": "Self study", },
                        {"isOther": True, }
                    ]
                    }
                }
                }
            },
        ],
        #Section 8
        [
            { 
                "title": "How easy is it to self study AP "+ name +"?", 
                "questionItem": { 
                "question": { 
                    "required": True, 
                    "scaleQuestion": { 
                    "low":0, 
                    "high":10, 
                    "lowLabel": "Very difficult", 
                    "highLabel": "Very easy"
                    }
                }
                }
            },
            { 
                "title": "What elements of the course did you find easy to self study? ", 
                "questionItem": { 
                "question": { 
                    "required": False, 
                    "textQuestion": { 
                    "paragraph": True
                    }
                }
                }
            },
            { 
                "title": "What elements of the course did you find difficult to self study? ", 
                "questionItem": { 
                "question": { 
                    "required": False, 
                    "textQuestion": { 
                    "paragraph": True
                    }
                }
                }
            },
            { 
                "title": "How many weeks did you spend learning for the AP " + name+ " exam?", 
                "description": "We're interested in the normal course workload--not within a few weeks of the exam day. Only include numerical values, not units.",
                "questionItem": { 
                "question": { 
                    "required": True, 
                    "textQuestion": { 
                    "paragraph": False
                    }
                }
                }
            },
            { 
                "title": "How many hours a week did you dedicate to self-studying AP " + name + "?", 
                "description": "We're interested in the normal course workload--not the hours you put in within a few weeks of the exam day. Only include numerical values, not units.",
                "questionItem": { 
                "question": { 
                    "required": True,
                    "textQuestion": { 
                    "paragraph": False
                    }
                }
                }
            },
            { 
                "title": "How many weeks did you spend reviewing (not learning) for the AP "+name+" exam as you self-studied?", 
                "description": "Only include numerical values, not units.", 
                "questionItem": { 
                "question": { 
                    "required": True,
                    "textQuestion": { 
                    "paragraph": False
                    }
                }
                }
            },
            {
                "title": "If you self studied, what would your advice be for others who wish to do the same?", 
                "questionItem": { 
                "question": { 
                "required": False, 
                "textQuestion": { 
                    "paragraph": False
                }
                }   
                }
        },
        ],
        #Section 9
        [
            { 
                "title": "Rate the quality of your teacher's preparation for the exam.", 
                "questionItem": { 
                "question": { 
                    "required": True, 
                    "scaleQuestion": { 
                    "low": 1,
                    "high": 10, 
                    "lowLabel": "Very Poor", 
                    "highLabel": "Excellent"
                    }
                }
                }
            },
            { 
                "title": "What aspects of your teacher's teaching style helped you prepare well for this course? ", 
                "questionItem": { 
                "question": { 
                    "required": False, 
                    "textQuestion": { 
                    "paragraph": True
                    }
                }
                }
            },
            { 
                "title": "What aspects of your teacher's teaching style would you say didn't contribute/contributed negatively to your preparation for this course?", 
                "questionItem": { 
                "question": { 
                    "required": False, 
                    "textQuestion": { 
                    "paragraph": True
                    }
                }
                }
            },
            { 
                "title": "How many weeks did you dedicate to studying for the AP " + name + " exam with a teacher?", 
                "description": "We're interested in the normal course workload--not within a few weeks of the exam day. Only include numerical values, not units.",
                "questionItem": { 
                "question": { 
                    "required": True, 
                    "textQuestion": { 
                    "paragraph": False
                    }
                }
                } 
            },
            { 
                "title": "How many weeks did you dedicate to studying for the AP " + name + " exam outside of the classroom?", 
                "description": "We're interested in the normal course workload--not within a few weeks of the exam day. Only include numerical values, not units.",
                "questionItem": { 
                "question": { 
                    "required": True,  
                    "textQuestion": { 
                    "paragraph": False
                    }
                }
                }
            },
            { 
                "title": "How many hours a week would you typically (not within a few weeks of the AP exam) dedicate to AP "+name+"?", 
                "description": "We're interested in the normal course workload--not within a few weeks of the exam day.  Only include numerical values, not units.",
                "questionItem": { 
                "question": { 
                    "required": True,  
                    "textQuestion": { 
                    "paragraph": False
                    }
                }
                }
            },
            { 
                "title": "Did you find it necessary to seek additional help outside of your regular class time? If so, how did you access this help?", 
                "questionItem": { 
                "question": { 
                    "required": False, 
                    "textQuestion": { 
                    "paragraph": True
                    }
                }
                }
            },
        ],
        #Section 10
        [
            { 
                "title": "How hard is AP " + name+ "?", 
                "questionItem": { 
                "question": { 
                    "required": True, 
                    "scaleQuestion": { 
                    "low": 1,
                    "high": 10, 
                    "lowLabel": "Very Easy", 
                    "highLabel": "Very Hard"
                    }
                }
                }
            },
            { 
                    "title": "Is AP " + name + " fun?", 
                    "questionItem": { 
                    "question": { 
                        "required": True, 
                        "choiceQuestion": { 
                        "type": "RADIO", 
                        "options": [ 
                        {"value": "Yes", },
                        {"value": "No", },
                    ]
                    }
                }
                }
            },
            { 
                "title": "What specific elements/units/topics appealed to you the most?", 
                "questionItem": { 
                "question": { 
                    "required": False, 
                    "textQuestion": { 
                    "paragraph": True
                    }
                }
                }
            },
            { 
                  "title": "Is AP " + name + " fun?", 
                    "questionItem": { 
                    "question": { 
                        "required": True, 
                        "choiceQuestion": { 
                        "type": "RADIO", 
                        "options": [ 
                        {"value": "Yes", },
                        {"value": "No", },
                    ]
                    }
                }
                }
              },
            { 
                "title": "Do you have any additional words of wisdom to future students?", 
                "description": "Keep it concise (just one or two points), and watch your grammar. Quality responses will be selected for the FAQ document.", 
                "questionItem": { 
                "question": { 
                    "required": False, 
                    "textQuestion": { 
                    "paragraph": True
                    }
                }
                }
            },
            { 
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
            },
            { 
                "title": "Did you use AI as a learning tool?", 
                "questionItem": { 
                "question": { 
                    "required": True, 
                    "choiceQuestion": { 
                    "type": "RADIO", 
                    "options": [ 
                        {"value": "Yes", },
                        {"value": "No",},
                    ]
                    }
                }
                }
            },
        ],
        #Section 11
        [ 
            { 
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
            },
            { 
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
            },
            { 
                "title": "What was AI good at explaining?", 
                "questionItem": { 
                "question": { 
                    "required": False, 
                    "textQuestion": { 
                    "paragraph": True
                    }
                }
                }
            },
            { 
                "title": "Where was it lackluster?", 
                "questionItem": { 
                "question": { 
                    "required": False, 
                    "textQuestion": { 
                    "paragraph": True
                    }
                }
                }
            },
        ],
        #Section 12
        [ 
            { 
                "title": "Have you taken/Are you currently pursuing higher studies in a field adjacent to AP " + name + "?", 
                "questionItem": {
                "question": { 
                    "required": True, 
                    "choiceQuestion": { 
                    "type": "RADIO", 
                    "options": [ 
                    {"value": "Yes", },
                    {"value": "No", },
                    ]
                    }
                    
                }
                }
            },
            { 
            "title": "Thanks for your help!", 
            "description": "The data from this survey will be used to help future AP " + name+ " students. Please share this survey with your friends!", 
            "textItem": {}
            }, 
        ],
        [
            #Section 14
            { 
                "title": "How well did the coursework transfer to your higher studies?", 
                "questionItem": { 
                "question": { 
                    "required": True, 
                    "scaleQuestion": { 
                    "low": 1, 
                    "high": 10, 
                    "lowLabel": "Very poorly", 
                    "highLabel": "Extremely well"
                    }
                }
                }
            },
            { 
                "title": "Explain the above response", 
                "questionItem": { 
                "question": { 
                    "required": False, 
                    "textQuestion": { 
                    "paragraph": True
                    }
                }
                }
            },
            { 
            "title": "Thanks for your help!", 
            "description": "The data from this survey will be used to help future AP " + name+ " students. Please share this survey with your friends!", 
            "textItem": {}
            }, 
        ]
        ]
    