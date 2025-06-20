import nltk
import random
from tkinter import *
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "hi": ["Hello!", "Hi!", "Greetings!"],
    "how are you": ["I'm doing well. How can I help you?", "All good! What about you?"],
    "i am fine": ["Great to hear that!", "Awesome! How can I help you today?"],
    "what is your name": ["I'm your friendly chatbot.", "Call me Chatster!"],
    "bye": ["Goodbye! Have a great day!", "See you soon!"],
    "default": ["I'm not sure I understand. Could you rephrase that?"]
}
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

def send():
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, f"You:\n{msg}\n\n", "user")

        bot_response = get_response(msg)
        ChatLog.insert(END, f"Bot:\n{bot_response}\n\n", "bot")

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

base = Tk()
base.title("AI Chatbot")
base.geometry("420x500")
base.resizable(width=False, height=False)
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial", wrap=WORD)
ChatLog.config(state=DISABLED)

scrollbar = Scrollbar(base, command=ChatLog.yview)
ChatLog['yscrollcommand'] = scrollbar.set

EntryBox = Text(base, bd=0, bg="white", width="29", height="4", font="Arial")
SendButton = Button(base, font=("Verdana", 12, 'bold'), text="Send", width="12", height=2,
                    bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff', command=send)


scrollbar.place(x=396, y=6, height=386)
ChatLog.place(x=6, y=6, height=386, width=390)
EntryBox.place(x=6, y=401, height=60, width=290)
SendButton.place(x=305, y=401, height=60)

ChatLog.tag_config("user", foreground="#003366", font=("Verdana", 11, "bold"))
ChatLog.tag_config("bot", foreground="#990000", font=("Verdana", 11))

base.mainloop()
