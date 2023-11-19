"""             CHATBOT WITH RULE-BASED RESPONSES
    Build a simple chatbot that responds to user inputs based on
    predefined rules. Use if-else statements or pattern matching
    techniques to identify user queries and provide appropriate
    responses. This will give you a basic understanding of natural
    language processing and conversation flow"""

from nltk.chat.util import Chat, reflections

rules = [
    [r"(hi|hey|hello)",
        ["Hello", "Hey there", "Hello sir"]
    ],
    [r"my name is (.*)",
        ["Hello %1, how are you?",]
    ],
    [r"is something new there(.*)",
        ["Yeah! It's a new day.", "Nope. Same as always :)"]
    ],
    [r"what is your name ?",
        ["I am AI bot created by Rishabh Mishra. You can call me Bhrata.", "I don't have a specific name; you can call me Bhrata :)"]
    ],
    [r"how are you ?",
        ["I'm doing good. How about you?",]
    ],
    [r"sorry(.*)",
        ["Alright", "No problem.", "It's OK, never mind",]
    ],
    [r"I am fine",
        ["Good to hear that. How can I help you?",]
    ],
    [r"i (am|feel) (.*)",
        ["Nice to hear that. How can I help you?",]
    ],
    [r"(.*) age",
        ["I don't have an age, but I was developed in November 2023.",]
    ],
    [r"what (.*) want",
        ["Make me an offer I can't refuse",]
    ],
    [r"(.*) created you",
        ["I'm an AI program developed by Rishabh Mishra", "I can't tell you that ;)"]
    ],
    [r"where were you developed",
        ['Bhopal, Madhya Pradesh', 'Somewhere on this Earth ;)']
    ],
    [r"when were you born",
        ["I was programmed in November 2023", "I was programmed, dude.", "I don't have any birthday."]
    ],
    [r"i work in (.*)",
        ["%1 is an amazing company. I have heard that they provide free internships to college students.",]
    ],
    [r"can you give me codsoft website",
        ["Sure! It's https://www.codsoft.in/", "Why not. It's https://www.codsoft.in/"]
    ],
    [r"(quit|bye)",
        ["Bye bye sir", "It was nice talking to you. See you soon :)"]
    ],
]

def chatBOT():
    print("Hi! I am BHRATA, a chatbot created by Rishabh Mishra.")
    chatbot = Chat(rules, reflections)
    chatbot.converse()

# Initiating chatBOT 
if __name__ == "__main__":
    chatBOT()
    print("If you have any more questions, feel free to ask!")
