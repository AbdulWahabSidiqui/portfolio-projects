from tkinter import *
from tkinter import filedialog
from morse import MorseCodeConverter
from PIL import Image, ImageTk
import play
import threading
import importer

DARK_BG = "#121212"
DARK_TEXT = "white"

LIGHT_BG = "white"
LIGHT_TEXT = "black"

TEXTBOX_DARK = "#1c1c1c"
TEXTBOX_LIGHT = "white"


class UI:
    def __init__(self):
        self.window = Tk()
        self.dark_mode = True
        self.mode_type1 = 'text'
        image = Image.open("assets/logo.png")
        image = image.resize((48,48))
        self.player = play.MorsePlayer()
        self.importer = importer.Importer()
        self.morse = MorseCodeConverter()


        self.logo = ImageTk.PhotoImage(image)

        self.window.title("Morse Translator")
        self.window.iconphoto(True,self.logo)

        self.window.configure(bg=DARK_BG)
        self.window.state('zoomed')
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        self.main_frame = Frame(self.window, bg=DARK_BG)
        self.main_frame.grid(row=0, column=0, sticky='nsew')
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.header = Frame(self.main_frame, bg=DARK_BG)
        self.header.grid(row=0, column=0, sticky='ew', padx=20,pady=20)

        self.logo_label = Label(self.header, image=self.logo,bg=DARK_BG)
        self.logo_label.grid(row=0,column=0, sticky='w',padx=(0,20))

        self.title = Label(self.header, text="Morse Translator", bg=DARK_BG, font=("Segoe UI", 24, "bold"), fg=LIGHT_BG)
        self.title.grid(row=0, column=1, sticky='w')

        # Theme:
        self.theme_toggle = Label(self.header,text='🌙 Dark',bg=DARK_BG,fg=LIGHT_BG,font=("Segoe UI Semibold", 12, "bold"),cursor='hand2')
        self.theme_toggle.grid(row=0, column=2, sticky='w')
        self.theme_toggle.bind("<Button-1>",self.ToggleTheme)

        self.header.grid_columnconfigure(0, weight=0)
        self.header.grid_columnconfigure(1, weight=1)
        self.header.grid_columnconfigure(2, weight=0)

        # Mode:
        self.mode_frame = Frame(self.main_frame, bg=DARK_BG)
        self.mode_frame.grid(row=1,column=0,padx=20,pady=(5,10),sticky='w')

        self.mode_label = Label(self.mode_frame,text='Mode',bg=DARK_BG,fg=LIGHT_BG,font=("Segoe UI", 18, "bold"))
        self.mode_label.grid(row=0, column=0, sticky='w')

        self.mode1 = Label(self.mode_frame,text='Text', bg=DARK_BG,fg=LIGHT_BG,font=("Segoe UI", 13, "bold"),width=12)
        self.mode1.grid(row=1, column=1, sticky='w',padx=(20,10))

        self.mode_change_button = Label(self.mode_frame,text='⇌',bg=DARK_BG,fg=LIGHT_BG,font=("Segoe UI", 18, "bold"),cursor='hand2')
        self.mode_change_button.grid(row=1, column=2, sticky='w', padx=(20,10))
        self.mode_change_button.bind("<Button-1>",self.ModeChange)

        self.mode2 = Label(self.mode_frame,text='Morse Code', bg=DARK_BG,fg=LIGHT_BG,font=("Segoe UI", 13, "bold"),width=12)
        self.mode2.grid(row=1, column=3, sticky='w',padx=(20,10))

        # Input:
        self.input_frame = Frame(self.main_frame,bg=DARK_BG)
        self.input_frame.grid(row=2, column=0,padx=20,pady=(0,10),sticky='w')

        self.input_label = Label(self.input_frame,text='Input',bg=DARK_BG,fg=LIGHT_BG,font=("Segoe UI", 18, "bold"))
        self.input_label.grid(row=0, column=0, sticky='w',pady=(0,10))

        self.input_box = Text(self.input_frame,height=5,width=50,font=("Consolas", 14),bg=TEXTBOX_DARK,wrap='word',fg=LIGHT_BG,insertbackground=LIGHT_BG,relief='solid',bd=1)

        self.scroll_bar = Scrollbar(self.input_frame,orient='vertical',command=self.input_box.yview,bg=DARK_BG,activebackground=DARK_BG,troughcolor=DARK_BG)

        self.input_box.configure(yscrollcommand=self.scroll_bar.set)
        self.input_box.grid(row=1,column=0,sticky='nsew')
        self.input_box.bind("<KeyRelease>",self.update_counter)
        self.scroll_bar.grid(row=1,column=1,sticky='ns')

        self.char_count = Label(self.input_frame,text='0/500 chars',bg=DARK_BG,fg=LIGHT_BG,font=("Consolas", 14))
        self.char_count.grid(row=2,column=0,sticky='e',pady=(5,0))

        self.input_frame.grid_columnconfigure(0, weight=1)
        self.input_frame.grid_rowconfigure(1, weight=1)

        # Output:
        self.output_frame = Frame(self.main_frame, bg=DARK_BG)
        self.output_frame.grid(row=3, column=0, padx=20, pady=(0, 10), sticky='w')

        self.output_label = Label(self.output_frame, text='Output', bg=DARK_BG, fg=LIGHT_BG, font=("Segoe UI", 18, "bold"))
        self.output_label.grid(row=0, column=0, sticky='w', pady=(0, 10))

        self.output_box = Text(self.output_frame, height=5, width=50, font=("Consolas", 14), bg=TEXTBOX_DARK, wrap='word',
                              fg=LIGHT_BG, insertbackground=LIGHT_BG, relief='solid', bd=1)

        self.scroll_bar_output = Scrollbar(self.output_frame, orient='vertical', command=self.output_box.yview, bg=DARK_BG,
                                    activebackground=DARK_BG, troughcolor=DARK_BG)

        self.output_box.configure(yscrollcommand=self.scroll_bar_output.set)
        self.output_box.grid(row=1, column=0, sticky='nsew')
        self.scroll_bar_output.grid(row=1, column=1, sticky='ns')

        self.output_frame.grid_columnconfigure(0, weight=1)
        self.output_frame.grid_rowconfigure(1, weight=1)

        # Buttons
        self.buttons_frame = Frame(self.main_frame,bg=DARK_BG)
        self.buttons_frame.grid(row=4, column=0, padx=20, pady=(0, 10), sticky='w')

        self.copy_button = Label(self.buttons_frame,text="Copy",font=("Segoe UI", 13, "bold"),cursor='hand2',bg=self.buttons_frame["bg"],bd=0,highlightthickness=0,relief='flat',borderwidth=0)
        self.copy_button.grid(row=0,column=0,sticky='nsew',padx=5)
        self.copy_button.bind("<Button-1>",self.copy)

        self.paste_button = Label(self.buttons_frame,text='Paste',font=("Segoe UI", 13, "bold"),cursor='hand2',bg=self.buttons_frame["bg"],bd=0,highlightthickness=0,relief='flat',borderwidth=0)
        self.paste_button.grid(row=0,column=1,sticky='nsew',padx=5)
        self.paste_button.bind("<Button-1>",self.paste)

        self.clear_button = Label(self.buttons_frame, text="Clear",font=("Segoe UI", 13, "bold"),cursor='hand2',bg=self.buttons_frame["bg"],bd=0,highlightthickness=0,relief='flat',borderwidth=0)
        self.clear_button.grid(row=0,column=2,sticky='nsew',padx=5)
        self.clear_button.bind("<Button-1>",self.clear)

        self.play_button = Label(self.buttons_frame, text="Play",font=("Segoe UI", 13, "bold"),cursor='hand2',bg=self.buttons_frame["bg"],bd=0,highlightthickness=0,relief='flat',borderwidth=0)
        self.play_button.grid(row=0,column=3,sticky='nsew',padx=5)
        self.play_button.bind("<Button-1>",self.play_audio)

        self.import_button = Label(self.buttons_frame, text='Import',font=("Segoe UI", 13, "bold"),cursor='hand2',bg=self.buttons_frame["bg"],bd=0,highlightthickness=0,relief='flat',borderwidth=0)
        self.import_button.grid(row=0,column=4,sticky='nsew',padx=5)
        self.import_button.bind("<Button-1>",self.import_file)

        self.export_button = Label(self.buttons_frame, text="Export",font=("Segoe UI", 13, "bold"),cursor="hand2",relief='flat',borderwidth=0,bg=self.buttons_frame["bg"],bd=0,highlightthickness=0)
        self.export_button.grid(row=0,column=5,sticky='nsew',padx=5)
        self.export_button.bind("<Button-1>",self.export_file)



        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=0)
        self.main_frame.grid_rowconfigure(2,weight=1)
        self.main_frame.grid_rowconfigure(3,weight=1)
        self.main_frame.grid_rowconfigure(4,weight=1)
        self.main_frame.grid_rowconfigure(5,weight=1)

        self.apply_theme()
        self.window.mainloop()

    def import_file(self,event=None):
        filepath = filedialog.askopenfilename(filetypes=[("Text File", "*.txt")])
        if filepath:
            text = self.importer.import_file(filepath)
            self.input_box.delete("1.0","end")
            self.input_box.insert("1.0",text)

    def export_file(self,event=None):
        text= self.output_box.get("1.0","end-1c")
        self.importer.export_file(text)

    def copy(self,event=None):
        text = self.output_box.get("1.0","end-1c")
        self.window.clipboard_clear()
        self.window.clipboard_append(text)
        self.window.update()
    def clear(self,event=None):
        self.input_box.delete("1.0","end")
        self.output_box.config(state='normal')
        self.output_box.delete("1.0","end")
        self.output_box.config(state='disabled')

    def paste(self,event=None):
        try:
            text = self.window.clipboard_get()
            self.input_box.insert('insert', text)
        except TclError:
            pass
    def play_audio(self, event=None):
        morse = self.output_box.get("1.0","end-1c")
        threading.Thread(
            target=self.player.play,
            args=(morse,),
            daemon=True
        ).start()

    def morse_to_text(self):
        text = self.input_box.get("1.0","end-1c")
        return self.morse.morse_to_text(text)

    def text_to_morse(self):
        text = self.input_box.get("1.0","end-1c")
        return self.morse.text_to_morse(text)

    def apply_theme(self):
        if self.dark_mode:
            bg = DARK_BG
            fg = DARK_TEXT
            text_box = TEXTBOX_DARK
            self.theme_toggle.config(text='🌙 Dark')

        else:
            bg = LIGHT_BG
            fg = LIGHT_TEXT
            text_box = TEXTBOX_LIGHT
            self.theme_toggle.config(text='☀ Light')

        self.window.config(bg=bg)

        self.main_frame.config(bg=bg)
        self.input_frame.config(bg=bg)
        self.output_frame.config(bg=bg)
        self.mode_frame.config(bg=bg)
        self.header.config(bg=bg)
        self.buttons_frame.config(bg=bg)

        widgets = [
            self.logo_label,
            self.title,
            self.mode_label,
            self.mode1,
            self.mode2,
            self.mode_change_button,
            self.theme_toggle,
            self.input_label,
            self.output_label,
            self.char_count,
            self.copy_button,
            self.paste_button,
            self.clear_button,
            self.play_button,
            self.import_button,
            self.export_button,
        ]

        for widget in widgets:
            widget.config(bg=bg,fg=fg)
        self.scroll_bar_output.config(bg=bg,activebackground=bg,troughcolor=bg)
        self.scroll_bar.config(bg=bg,activebackground=bg,troughcolor=bg)
        self.input_box.config(bg=text_box,fg=fg,insertbackground=fg)
        self.output_box.config(bg=text_box,fg=fg,insertbackground=fg)
        print("Frame bg:", self.buttons_frame["bg"])
        print("Copy bg :", self.copy_button["bg"])
        print("Copy fg :", self.copy_button["fg"])
    def ToggleTheme(self,event):
        self.dark_mode = not self.dark_mode
        self.apply_theme()
    def ModeChange(self,event):

        self.mode_type1 = 'morse' if self.mode_type1 == "text" else 'text'
        self.mode1.config(text="Morse Code" if  self.mode_type1 == "morse" else "Text")
        self.mode2.config(text="Text" if self.mode_type1 == "morse" else "Morse Code")
        current = self.output_box.get("1.0","end-1c")
        self.input_box.delete("1.0","end")
        self.input_box.insert("1.0",current)
        self.input_box.mark_set("insert","end")
        self.update_counter()

    def set_output(self,text):
        self.output_box.config(state='normal')
        self.output_box.delete('1.0', 'end')
        self.output_box.insert('1.0', text)
        self.output_box.config(state='disabled')

    def update_counter(self, event=False):
        text = self.input_box.get("1.0","end-1c")
        self.char_count.config(text=f"{len(text)}/500 chars")
        if len(text) > 500:
            self.input_box.delete('1.0+500c', 'end')

        if self.mode_type1 == 'text':
            result = self.text_to_morse()
        else:
            result = self.morse_to_text()
        self.set_output(result)