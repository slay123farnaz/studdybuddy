import tkinter as tk
from tkinter import Scrollbar, Text, Entry, Button, END, messagebox
from nltk.chat.util import Chat, reflections
import datetime

# Define chatbot responses using NLTK
pairs = [
    [
        r"(hello|hi|hey)",
        ["Hello!", "Hi there!", "Hey! How can I help you today?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you! what about you?", "I'm great, thanks for asking what about you?."]
    ],
    [
        r"i am doing well|i am fine|i am good|i am fantastic ",
        ["Good to hear it", " nice to hear it."]
    ],
    [
        r"i am not good|i am not fine|i am not doing well|i am sad ",
        ["It's okay we will get through it ", "I will help you get through it."]
    ],
    [
        r"what is your name ?",
        ["I'm a Study Buddy.", "I don't have a name, I'm just a bot."]
    ],
    [
        r"who created you ?",
        ["I was created by Farnaz.", "Farnaz created me."]
    ],
    [
        r"how were you made ?",
        ["I was created using Python.", "Python."]
    ],
    [
        r"what day is it ?",
        [datetime.datetime.now().strftime("%A"), datetime.datetime.now().strftime("%A") + "."]
    ],
    [
        r"what date is it today ?",
         [datetime.datetime.now().strftime("%d-%m-%Y"), "Today is " + datetime.datetime.now().strftime("%d %B %Y") + "."]
    ],
    [
        r"what is python ?",
        ["Python, one of the most popular programming languages in the world, has been used for various applications."]
    ],
    [
        r"write some motivation ?|give me some motivition?",
        ["Don't give up!", "YOU ARE THE BEST, YOU CAN DO IT!"]
    ],
    [
        r"how many bones are there in a human body ?|how many bones does a human have",
        ["206", "A human has 206 bones."]
    ],
    [
        r"who is the PM of Bangladesh ?",
        ["Sheikh Hasina", "The PM of Bangladesh is Sheikh Hasina."]
    ],
    [
        r"what is the capital city of Bangladesh ?",
        ["Dhaka", "Dhaka is the capital city of Bangladesh."]
    ],
    [
        r"what is the time now|what time is it now?",
        ["The current time is " + datetime.datetime.now().strftime("%H:%M:%S") + "."]
    ],
    [
        r"definition of cell ?",
        ["Cells are the smallest units of life and are often referred to as the building blocks of life."]
    ],
    [
        r"what is the national fruit of Bangladesh ?",
        ["Jackfruit", "Jackfruit is the national fruit of Bangladesh."]
    ],
     [
        r"what is science ?",
        ["Science consists of observing the world by watching, listening, observing, and recording. Science is curiosity in thoughtful action about the world and how it behaves."]
    ],
     
    [
        r"what is the capital of japan ?",
        ["Tokyo.","Tokyo is the capital of japan"]
    ],
    [
        r"who is the current principle of bcpsc ?",
        ["Masud.","Masud sir is the current principle of bcpsc"]
    ],
   
    [
        r"who is the current principle of bcpsc ?",
        ["Masud.","Masud sir is the current principle of bcpsc"]
    ],
    [
        r"who is the current principle of bcpsc ?",
        ["Masud.","Masud sir is the current principle of bcpsc"]
    ],
    [
        r"what is the national animal of bangladesh ?",
        ["Royal Bengal Tiger", "The Royal Bengal Tiger is the national animal of Bangladesh."]
    ],
    [
        r"what is the national game of Bangladesh ?",
        ["Kabaddi", "Kabaddi is the national game of Bangladesh."]
    ],
    [
        r"how many countries are there in the world ?",
        ["195", "There are 195 countries in the world."]
    ],
    [
        r"who is the first person to land on the moon ?",
        ["Neil Armstrong", "Neil Armstrong was the first person to land on the moon."]
    ],
    [
        r"what is the largest city in the world ?",
        ["Tokyo", "Tokyo is the largest city in the world."]
    ],
    [
        r"what is a thermometer ?",
        ["A thermometer is a device that can measure temperature."]
    ],
    [
        r"what is the warmest place on Earth ?",
        ["Death Valley", "Death Valley is the warmest place on Earth."]
    ],
    [
        r"how many cells are there in the human body ?",
        ["There are almost 30 to 40 trillion cells in the human body."]
    ],
    [
        r"what is a weed ?",
        ["Any unwanted plant is called a weed."]
    ],
    [
        r"what is the national fish of Bangladesh ?",
        ["Elish"]
    ],
    [
        r"what is the national flower of Bangladesh ?",
        ["Water lily"]
    ],
    [
        r"when did Bangladesh gain its freedom ?",
        ["Bangladesh gained its freedom on March 26, 1971."]
    ],
    [
        r"what is acid rain ?",
        ["Acid rain is rainwater that has been chemically changed into an acid by industrial air pollution."]
    ],
    [
        r"quiz me on math ?|ask me a math question?",
        ["Sure, let's start with a math question.", "Here's a math question: 1200 multiplied by 122 is?"]
    ],
    [
        r"quiz me on biology ?|ask me a biology question?",
        ["Sure, let's start with a biology question What is the resolution of the human eye?", "Here's a biology question: A cell membrane is______?"]
    ],
    [
        r"146400 ?",
        ["GOOD JOB BUDDY!", "YAY, YOU DID IT."]
    ],
    [
        r"10 apples|10 ?",
        ["YAY BUDDY, THAT'S RIGHT!", "YAY, YOU SOLVED IT."]
    ],
    [
        r"quiz me on science ?",
        ["Sure, here's a science question: How many bones are there in a human body?"]
    ],
    [
        r"206 bones ?",
        ["That's right, good job!"]
    ],
    [
        r"206 ?",
        ["Yes, buddy!"]
    ],
    [
        r" 576 megapixels",
        ["Yes, buddy!"]
    ],
    [
        r"  Semipermeable",
        ["Yes, buddy!"]
    ],
    [
        r"quiz me on geography ?",
        ["Alright, here's a geography question: What is the warmest place on Earth?"]
    ],
    [
        r"dead valley ?",
        ["YAY, RIGHT!"]
    ],
    [
        r"what does DNA stand for?", 
        ["DNA stands for Deoxyribonucleic acid."]
    ],
    [
        r"roughly how long does it take for the sun's light to reach Earth ?",
        ["It takes approximately 8 minutes and 20 seconds for the sun's light to reach Earth."]
    ],
    [
        r"how many teeth does an adult human have ?",
        ["An adult human has 32 teeth."]
    ],
    [
        r"what is algebra ?",
        ["Algebra is the study of mathematical symbols and the rules for manipulating these symbols."]
    ],
    [
        r"what is a flow chart ?",
        ["A flowchart is a type of diagram that represents a workflow or process."]
    ],
    [
        r"what is Study Buddy?",
        ["A Study Buddy is someone who helps you learn and study better, sharing knowledge, resources, and advice with you."]
    ],
    [
        r"what causes air pollution ?",
        ["Air pollution is caused by solid and liquid particles, as well as certain gases, suspended in the air."]
    ],
    [
        r"tell me a joke ?",
        ["What do kids play when their mom is using the phone? BORED GAMES"]
    ],
    [
        r"what are you doing ?",
        ["taliking to my friend "]
    ],
    [
        r"who is your friend ?",
        ["you buddy "]
    ],
    [
        r"what causes water pollution ?",
        ["Water pollution is caused by the contamination of water with disease-causing microorganisms and poisonous substances."]
    ],
    [
        r"what do our lungs do ?",
        ["Our lungs play a crucial role in taking in oxygen from the air and releasing carbon dioxide, as well as in vocalization and protection against harmful substances."]
    ],
    [
        r"(bye|quit|exit)",
        ["Goodbye!", "See you later!", "Bye! Have a nice day!"]
    ],
    
    
    [
        r"(.*)",
        ["I'm sorry, I am still developing.", "I am sorry.I am still learning."]
    ],
]

# Define quiz questions and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris",
        "star": 3
    },
    {
        "question": "How many continents are there?",
        "answer": "7",
        "star": 2
    },
    {
        "question": "What is 2 + 2?",
        "answer": "4",
        "star": 1
    },
    {
        "question": "what is national flower of bangladesh?",
        "answer": "water lily",
        "star": 1
    },
    {
        "question": "which country invented number 0?",
        "answer": "india",
        "star": 1
    },
     {
        "question": "how many bones does a human have?",
        "answer": "206",
        "star": 1
    },
     {
        "question": "what will water turn into if we freeze it?",
        "answer": "ice",
        "star": 1
    },
     {
        "question": "what is 129769x6493362?",
        "answer": "842637093378",
        "star": 1
    },
     {
        "question": "what is the main sport of bangladesh?",
        "answer": "kabadi",
        "star": 1
    },

     
]




# Initialize quiz variables
quiz_index = 0
score = 0


# Function to ask the next quiz question
def ask_question():
    global quiz_index, score
    if quiz_index < len(quiz_questions):
        question_label.config(text=quiz_questions[quiz_index]["question"])
        check_button.config(state=tk.NORMAL)
        entry_field.config(state=tk.NORMAL)
    else:
        show_score()

# Function to check the answer and update the score
def check_answer():
    global quiz_index, score
    user_answer = entry_field.get().strip().lower()
    correct_answer = quiz_questions[quiz_index]["answer"].lower()

    if user_answer == correct_answer:
        score += quiz_questions[quiz_index]["star"]

    quiz_index += 1
    entry_field.delete(0, tk.END)

    if quiz_index < len(quiz_questions):
        ask_question()
    else:
        # All questions answered, display "Finish Quiz" button
        check_button.config(state=tk.DISABLED)
        finish_button = Button(window, text="Finish Quiz", bg='#b0ecf8', command=finish_quiz, font='arial')
        finish_button.grid(row=3, column=1, padx=10, pady=10)

# Function to display the final score
def show_score():
    
    messagebox.showinfo("Quiz Result", f"YEAY BUDDY Your score: 12/{score} stars")

# Function to handle finishing the quiz and closing the window
def finish_quiz():
    show_score()
   

# Function to clear the conversation text
def clear_conversation():
    conversation_text.config(state=tk.NORMAL)
    conversation_text.delete(1.0, tk.END)  # Clear all text in the conversation text widget
    conversation_text.config(state=tk.DISABLED)

# Function to clear the user input field
def clear_input():
    entry_field.delete(0, tk.END)  # Clear the user input field

# Create a chatbot using the NLTK Chat class
studybuddy = Chat(pairs, reflections)

# Function to handle user input and generate responses
def send_message():
    user_message = entry_field.get()
    response = studybuddy.respond(user_message)
    conversation_text.config(state=tk.NORMAL)
    conversation_text.insert(tk.END, "You: " + user_message + "\n")
    conversation_text.insert(tk.END, "Study Buddy: " + response + "\n")
    conversation_text.config(state=tk.DISABLED)
    entry_field.delete(0, tk.END)

# Function to update the timer and stop the program after 60 minutes
def update_timer():
    remaining_time = 60 * 60 - (datetime.datetime.now() - start_time).total_seconds()
    minutes = int(remaining_time // 60)
    seconds = int(remaining_time % 60)
    timer_label.config(text=f"Time Left: {minutes:02}:{seconds:02}")
    if remaining_time <= 0:
        stop_program()
    else:
        window.after(1000, update_timer)  # Update the timer every 1 second

# Function to stop the program
def stop_program():
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("Study Buddy")
window.configure(bg='#B0E0E6')
window.configure(height=120)
window.configure(width=300)



# Create a Text widget to display the conversation
conversation_text = Text(window, wrap=tk.WORD, width=40, height=15)
conversation_text.config(state=tk.DISABLED)
conversation_text =Text(window,font='Verdana', width=40, height=15)

# Create a scrollbar for the conversation Text widget
scrollbar = Scrollbar(window, command=conversation_text.yview)
conversation_text['yscrollcommand'] = scrollbar.set

# Create an Entry widget for user input
entry_field = Entry(window, width=40)
send_button = Button(window, bg='#b0ecf8', text="Send", command=send_message, font='arial')

# Create a label to display the timer
timer_label = tk.Label(window, text="Time Left: 60:00", font='Verdana 12 bold', fg='red')

# Create the "Next Question" button
check_button = Button(window, text="Check Answer", bg='#b0ecf8', state=tk.DISABLED, command=check_answer, font='arial')

# Create a label to display the quiz questions
question_label = tk.Label(window, text="", font='Verdana 12', pady=10)

# Place widgets on the window using grid layout
conversation_text.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
scrollbar.grid(row=0, column=2, sticky='ns')
entry_field.grid(row=1, column=0, padx=10, pady=10)
send_button.grid(row=1, column=1, padx=10, pady=10)
timer_label.grid(row=2, column=0, columnspan=2, pady=10)
check_button.grid(row=3, column=0, columnspan=2, pady=10)
question_label.grid(row=4, column=0, columnspan=2, pady=10)

# Create a "Clear" button for the conversation text and user input field
clear_button = Button(window, text="Clear", bg='#b0ecf8', command=lambda: [clear_conversation(), clear_input()], font='arial')
clear_button.grid(row=1, column=2, padx=10, pady=10)

# Get the start time
start_time = datetime.datetime.now()

# Start updating the timer
update_timer()

# Initialize the first question
ask_question()

# Start the main loop
window.mainloop()