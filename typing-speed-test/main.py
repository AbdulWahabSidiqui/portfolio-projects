import random
from tkinter import *
import time


BG = "#0F172A"
PANEL = "#1E293B"
BUTTON = "#06B6D4"
BUTTON_HOVER = "#0891B2"
SUCCESS = "#22C55E"
ERROR = "#EF4444"
TEXT = "#F8FAFC"
SECONDARY_TEXT = "#CBD5E1"
INPUT_BG = "#334155"
BORDER = "#475569"

TITLE_FONT = ("Bahnschrift", 28, "bold")
HEADING_FONT = ("Bahnschrift", 18, "bold")
LABEL_FONT = ("Bahnschrift", 12)
TEXT_FONT = ("Consolas", 13)
BUTTON_FONT = ("Bahnschrift", 11, "bold")

paragraphs = [
    "Practice makes progress. Every minute you spend typing helps improve your speed and accuracy. Stay focused, keep your hands on the keyboard, and enjoy the learning process.",

    "Python is one of the most popular programming languages in the world. It is simple to learn, powerful to use, and perfect for beginners as well as professionals.",

    "Reading books every day expands your knowledge and improves your vocabulary. Even a few pages each day can make a big difference over time.",

    "A healthy lifestyle includes regular exercise, balanced meals, enough sleep, and plenty of water. Small daily habits often lead to the biggest improvements.",

    "Technology has changed the way people communicate, learn, and work. The internet allows us to connect with others and access information within seconds.",

    "Learning to type without looking at the keyboard takes patience and practice. Over time, your fingers will remember the key positions naturally.",

    "Success does not happen overnight. It is the result of consistent effort, determination, and the willingness to learn from mistakes every single day.",

    "Nature is full of beauty and wonder. A walk through a park or forest can refresh your mind, reduce stress, and improve your overall mood.",

    "Setting small goals makes large tasks easier to achieve. Completing one step at a time builds confidence and keeps you motivated throughout your journey.",

    "Time is one of the most valuable resources in life. Using it wisely allows you to achieve your goals while maintaining a healthy balance between work and rest."
]

class UI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed Test")
        self.window.state("zoomed")
        self.window.config(bg=BG)
        self.current_para = None
        self.seconds = 0
        self.timer_running = False
        self.wpm = None
        self.accuracy = None

        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)

        self.main_frame = Frame(self.window,bg=PANEL,width=1100,height=550)
        self.main_frame.grid(row=0,column=0,sticky="")
        self.main_frame.grid_propagate(False)

        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)


        self.title = Label(self.main_frame,text="TYPING SPEED TEST",bg=PANEL,fg=TEXT,font=TITLE_FONT,)
        self.title.grid(row=0,column=0,pady=(25,20),columnspan=3)

        self.sample_heading = Label(self.main_frame,text="Sample Text:",bg=PANEL,fg=TEXT,font=HEADING_FONT,wraplength=900,justify="left")
        self.sample_heading.grid(row=1,column=1,sticky="w",pady=(10,15))

        self.sample_label = Message(self.main_frame,text="",bg=PANEL,fg=TEXT,font=TEXT_FONT,justify="left",width=800)
        self.sample_label.grid(row=2,column=1,sticky="w",)
        self.random_para()

        self.input_label = Label(self.main_frame,text="Your Text:",bg=PANEL,fg=TEXT,font=HEADING_FONT,justify="left",wraplength=900,)
        self.input_label.grid(row=3,column=1,sticky="w",pady=(10,15))

        self.input_entry = Text(self.main_frame,height=8,font=TEXT_FONT,bg=INPUT_BG,fg=TEXT,insertbackground=TEXT,wrap="word",relief="flat",bd=1,highlightthickness=1,highlightcolor=BUTTON,highlightbackground=BORDER)
        self.input_entry.grid(row=4,column=1,sticky="ew",pady=10)
        self.input_entry.bind("<KeyPress>",self.start_timer)
        self.input_entry.bind("<KeyRelease>",self.speed_calc)

        self.stats_frame = Frame(self.main_frame,bg=PANEL)
        self.stats_frame.grid(row=5,column=1,sticky="ew",pady=(20,10))

        self.stats_frame.grid_columnconfigure(0,weight=1)
        self.stats_frame.grid_columnconfigure(1,weight=1)
        self.stats_frame.grid_columnconfigure(2,weight=1)

        self.time_label = Label(self.stats_frame,text="Time: 00:00",bg=PANEL,fg=TEXT,font=HEADING_FONT,justify="left")
        self.time_label.grid(row=0,column=0,sticky="w",padx=20)

        self.wpm_label = Label(self.stats_frame,text="WPM: 0",bg=PANEL,fg=TEXT,font=HEADING_FONT)
        self.wpm_label.grid(row=0,column=1,)

        self.accuracy_label = Label(self.stats_frame,text="Accuracy: 100%",bg=PANEL,fg=TEXT,font=HEADING_FONT)
        self.accuracy_label.grid(row=0,column=2,sticky="e",padx=20)

        self.new_test_button = Button(self.stats_frame,text="Start New Test",bg=PANEL,fg=BUTTON,font=BUTTON_FONT,command=self.new_test)
        self.new_test_button.grid(row=0,column=3,sticky="ew",padx=20)





        self.window.mainloop()

    def random_para(self):
        self.current_para = random.choice(paragraphs)
        self.sample_label.config(text=self.current_para)

    def speed_calc(self,event):
        typed_text = self.input_entry.get("1.0","end-1c")

        words = len(typed_text.split())
        minutes = self.seconds /60
        if minutes > 0:
            self.wpm = words / minutes
        else:
            self.wpm = 0
        correct = 0
        expected = self.current_para.split()
        typed = typed_text.split()

        for e,t in zip(expected,typed):
            if e == t:
                correct += 1

        self.accuracy = (correct/len(expected)) * 100
        self.accuracy = round(self.accuracy,2)


        if typed_text == self.current_para:
            self.timer_running = False
            self.input_entry.config(state="disabled")
            self.accuracy_label.config(text=f"Accuracy: {self.accuracy:.2f}%")
            self.wpm_label.config(text=f"WPM: {self.wpm}")



    def new_test(self):
        self.seconds = 0
        self.time_label.config(text="Time: 00:00")
        self.timer_running = False
        self.input_entry.config(state="normal")
        self.input_entry.delete("1.0",END)
        self.time_label.config(text="Time: 00:00")
        self.wpm_label.config(text="WPM: 0")
        self.accuracy_label.config(text="Accuracy: 100%")
        self.input_entry.focus_set()
        self.random_para()

    def start_timer(self,event):
        if event.keysym in (
                "Shift_L", "Shift_R",
                "Control_L", "Control_R",
                "Alt_L", "Alt_R",
                "Left", "Right", "Up", "Down"
        ):
            return
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()
    def update_timer(self):
        if self.timer_running:
            self.seconds += 1

            minutes = self.seconds //60
            seconds = self.seconds % 60

            self.time_label.config(text=f"Time: {minutes:02}:{seconds:02}")
            self.window.after(1000,self.update_timer)







ui = UI()
