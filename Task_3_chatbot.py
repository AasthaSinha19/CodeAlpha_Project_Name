import nltk
import json
import pickle
import numpy as np
import random
from nltk.corpus import stopwords
from nltk.chat.util import Chat, reflections
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from tkinter import *
root = Tk()
root.title("Chatbot")
def send():
    send = "You -> "+e.get()
    txt.insert(END, "n"+send)
    user = e.get().lower()
    if(user == "hello"):
        txt.insert(END, "n" + "Bot -> Hi")
    elif(user == "hi" or user == "hii" or user == "hiiii"):
        txt.insert(END, "n" + "Bot -> Hello")
    elif(e.get() == "how are you"):
        txt.insert(END, "n" + "Bot -> fine! and you")
    elif(user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END, "n" + "Bot -> Great! how can I help you.")
    else:
        txt.insert(END, "n" + "Bot -> Sorry! I dind't got you")
    e.delete(0, END)
txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
e.grid(row=1, column=0)
send = Button(root, text="Send", command=send).grid(row=1, column=1)
root.mainloop()
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name ?",
        ["I am a bot created by Analytics Vidhya. you can call me crazy!",]
    ],
    [
        r"how are you ?",
        ["I'm doing goodnHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dudenSeriously you are asking me this?",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["Raghav created me using Python's NLTK library ","top secret ;)",]
    ],
    [
       r"(.*) (location|city) ?",
       ['Indore, Madhya Pradesh',]
   ],
   [
       r"how is weather in (.*)?",
       ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
   ],
   [
       r"i work in (.*)?",
       ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
   ],
   [
       r"(.*)raining in (.*)",
       ["No rain since last week here in %2","Damn its raining too much here in %2"]
   ],
   [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Crazy_Tech has many great articles with each step explanation along with code, you can explore"]
    ],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]
def chat():
    print("Hi! I am a chatbot for your service")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()
data_file = open('intents.json').read()

intents = json.loads(data_file)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Sample data
data = [
    "The quick brown fox jumps over the lazy dog",
    "A bird in the hand is worth two in the bush",
    "Actions speak louder than words"
]

# Tokenize, lemmatize, and remove stopwords
tokenized_data = []
for sentence in data:
    tokens = nltk.word_tokenize(sentence.lower())  # Tokenize and convert to lowercase
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]  # Lemmatize tokens
    filtered_tokens = [token for token in lemmatized_tokens if token not in stop_words]  # Remove stop words
    tokenized_data.append(filtered_tokens)

# Remove duplicate words
for i in range(len(tokenized_data)):
    tokenized_data[i] = list(set(tokenized_data[i]))
print(tokenized_data)
# Create training data

training = []
output_empty = [0] * len(classes)
for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    for w in words:

        bag.append(1) if w in pattern_words else bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

# Shuffle and convert to numpy array

random.shuffle(training)

training = np.array(training)

# Separate features and labels

train_x = list(training[:,0])
train_y = list(training[:,1])
model = Sequential()

model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))

model.add(Dropout(0.5))

model.add(Dense(64, activation='relu'))

model.add(Dropout(0.5))

model.add(Dense(len(train_y[0]), activation='softmax'))

# Compile the model

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Train the model

model.fit(np.array(train_x), np.array(train_y),epochs=200, batch_size=5, verbose=1)
def predict_class(sentence, model):

    p = bow(sentence, words, show_details=False)

    res = model.predict(np.array([p]))[0]

    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)

    return_list = []

    for r in results:

        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})

    return return_list
# GUI with Tkinter

import tkinter

from tkinter import *

# Function to send message and get response

def send():

    msg = EntryBox.get("1.0",'end-1c').strip()

    EntryBox.delete("0.0",END)

    if msg != '':

        ChatLog.config(state=NORMAL)

        ChatLog.insert(END, "You: " + msg + '\n\n')

        ChatLog.config(foreground="#442265", font=("Verdana", 12))
        res = chatbot_response(msg)

        ChatLog.insert(END, "Bot: " + res + '\n\n')

        ChatLog.config(state=DISABLED)

        ChatLog.yview(END)

# GUI setup

base = Tk()

base.title("Chatbot")

base.geometry("400x500")

base.resizable(width=FALSE, height=FALSE)

ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial")
ChatLog.config(state=DISABLED)

scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")

ChatLog['yscrollcommand'] = scrollbar.set

SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5, bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff', command= send )

EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")

scrollbar.place(x=376,y=6, height=386)

ChatLog.place(x=6,y=6, height=386, width=370)

EntryBox.place(x=128, y=401, height=90, width=265)

SendButton.place(x=6, y=401, height=90)

base.mainloop()   