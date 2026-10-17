import random
from tkinter import Tk, Label, Button, Entry, Frame

BG_COLOR = '#F8FAFC'
BOARD_COLOR = '#FFFFFF'
PRIMARY_COLOR = '#3B82F6'
X_COLOR = "#2563EB"
O_COLOR = "#EF4444"
WINNER_COLOR = "#22C55E"
TEXT_COLOR = "#1E293B"
SECONDARY_TEXT_COLOR = "#64748B"
BORDER_COLOR = "#E2E8F0"

class UI():
    def __init__(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.game_over = False
        self.x_score = 0
        self.o_score = 0
        self.winner = None
        self.game_mode = None

        self.main = Tk()
        self.main.title("Tic Tac Toe")
        self.main.state("zoomed")
        self.main.config(bg=BG_COLOR)
        self.main.resizable(width=False, height=False)

        self.menu_frame = Frame(self.main, bg=BG_COLOR)
        self.menu_frame.pack(fill="both", expand=True)

        # Center container
        self.menu_container = Frame(self.menu_frame, bg=BG_COLOR)
        self.menu_container.place(relx=0.5, rely=0.5, anchor="center")

        self.menu_heading = Label(
            self.menu_container,
            text="Tic Tac Toe",
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            font=("Segoe UI", 34, "bold")
        )
        self.menu_heading.pack(pady=(0, 40))

        self.pvp_button = Button(
            self.menu_container,
            text="Player vs Player",
            command=self.start_pvp,
            bg=PRIMARY_COLOR,
            fg="white",
            font=("Segoe UI", 12, "bold"),
            width=22,
            bd=0,
            cursor="hand2"
        )
        self.pvp_button.pack(pady=10)

        self.pvc_button = Button(
            self.menu_container,
            text="Player vs Computer",
            command=self.start_pvc,
            bg=PRIMARY_COLOR,
            fg="white",
            font=("Segoe UI", 12, "bold"),
            width=22,
            bd=0,
            cursor="hand2"
        )
        self.pvc_button.pack(pady=10)

        self.main_frame = Frame(self.main, bg=BG_COLOR, padx=30, pady=30)

        self.heading = Label(self.main_frame, text="Tic Tac Toe", bg=BG_COLOR, fg=TEXT_COLOR, font=("Segoe UI", 26, "bold"),)
        self.heading.grid(row=0, column=0,pady=(0,30),columnspan=3)

        self.mode_heading = Label(self.main_frame,text="Mode: Player vs Computer", bg=BG_COLOR,fg=TEXT_COLOR,font=("Segoe UI", 26, "bold"))
        self.mode_heading.grid(row=1,column=0,pady=(0,30),columnspan=3)

        self.player_x = Label(self.main_frame,text="Player X", bg=BG_COLOR, fg=TEXT_COLOR, font=("Segoe UI", 18, "bold"))
        self.player_x.grid(row=2, column=0,pady=(0,30))

        self.score = Label(self.main_frame, text="0 : 0",bg=BG_COLOR,fg=TEXT_COLOR,font=("Segoe UI", 18, "bold"),)
        self.score.grid(row=2, column=1,pady=(0,30))

        self.player_o = Label(self.main_frame,text="Player O",bg=BG_COLOR,fg=TEXT_COLOR,font=("Segoe UI", 18, "bold"))
        self.player_o.grid(row=2, column=2,pady=(0,30))

        self.current_turn = Label(self.main_frame,text="Current Turn: X", bg=BG_COLOR,fg=TEXT_COLOR,font=("Segoe UI", 18, "bold"),)
        self.current_turn.grid(row=3, column=0,pady=(0,30),columnspan=3)

        self.buttons_frame = Frame(self.main_frame, bg=BOARD_COLOR, padx=10, pady=10,highlightbackground=BORDER_COLOR,highlightthickness=1)
        self.buttons_frame.grid(row=4, column=0,pady=10,columnspan=3)


        for row in range(3):
            for col in range(3):
                btn = Button(self.buttons_frame,
                             text="",
                             bg=BORDER_COLOR,
                             fg=TEXT_COLOR,
                             font=("Segoe UI", 24, "bold"),
                             width=3,
                             height=1,
                             relief="flat",
                             borderwidth=1,
                             activebackground="#DBEAFE",
                             command=lambda r=row,c=col: self.play_move(r,c))
                btn.grid(row=row,column=col,padx=4,pady=4)
                self.buttons[row][col] = btn

        self.bottom_frame = Frame(self.main_frame, bg=BOARD_COLOR)
        self.bottom_frame.grid(row=5, column=0,pady=(10,20),columnspan=3)

        self.reset_button = Button(self.bottom_frame,
                                   text="New Game",
                                   bg=PRIMARY_COLOR,
                                   fg="white",
                                   font=("Segoe UI", 11, "bold"),
                                   bd=0,
                                   relief="flat",
                                   activebackground="#2563EB",
                                   activeforeground="white",
                                   cursor="hand2",
                                   command=self.new_game)
        self.reset_button.grid(row=0, column=0,padx=10,pady=20)

        self.reset_score = Button(self.bottom_frame,
                                  text="Reset Score" ,
                                  bg=PRIMARY_COLOR,
                                   fg="white",
                                   font=("Segoe UI", 11, "bold"),
                                   bd=0,
                                   relief="flat",
                                   activebackground="#2563EB",
                                   activeforeground="white",
                                   cursor="hand2",
                                  command=self.new_score)

        self.reset_score.grid(row=0, column=1,padx=10,pady=20)

        self.change_mode_button = Button(self.bottom_frame,
                                  text="Change Mode" ,
                                  bg=PRIMARY_COLOR,
                                   fg="white",
                                   font=("Segoe UI", 11, "bold"),
                                   bd=0,
                                   relief="flat",
                                   activebackground="#2563EB",
                                   activeforeground="white",
                                   cursor="hand2",
                                  command=self.change_mode)
        self.change_mode_button.grid(row=0, column=2,padx=10,pady=20)

        for i in range(3):
            self.main_frame.columnconfigure(i,weight=1)
        self.main.mainloop()


    def play_move(self,r,c):
        if self.game_over:
            return
        if self.game_mode == "PvC" and self.current_player == "O":
            return
        if self.board[r][c]!= "":
            return
        self.board[r][c] = self.current_player
        color = X_COLOR if self.current_player == "X" else O_COLOR
        self.buttons[r][c].config(text=self.current_player,fg=color)
        self.check_winner()
        if not self.game_over:
            self.switch_player()

        if self.game_mode == "PvC" and self.current_player == "O":
            self.main.after(500, self.comp_move)


    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"
        self.current_turn.config(text =f"Current Turn: {self.current_player}")

    def new_game(self):
        self.current_player = "X"
        self.game_over = False
        self.winner = None

        self.current_turn.config(text =f"Current Turn: {self.current_player}")

        for row in range(3):
            for col in range(3):
                self.board[row][col] = ""
                self.buttons[row][col].config(text="",fg=TEXT_COLOR,bg=BORDER_COLOR,state="normal")


    def new_score(self):
        self.x_score = 0
        self.o_score = 0
        self.score.config(text="0 : 0")
        self.new_game()

    def check_winner(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != "":
                self.winner = self.current_player
                self.buttons[row][0].config(bg=WINNER_COLOR)
                self.buttons[row][1].config(bg=WINNER_COLOR)
                self.buttons[row][2].config(bg=WINNER_COLOR)
                self.game_won()
                return
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                self.winner = self.current_player
                self.buttons[0][col].config(bg=WINNER_COLOR)
                self.buttons[1][col].config(bg=WINNER_COLOR)
                self.buttons[2][col].config(bg=WINNER_COLOR)
                self.game_won()
                return
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            self.winner = self.current_player
            self.buttons[0][0].config(bg=WINNER_COLOR)
            self.buttons[1][1].config(bg=WINNER_COLOR)
            self.buttons[2][2].config(bg=WINNER_COLOR)
            self.game_won()
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            self.winner = self.current_player
            self.buttons[0][2].config(bg=WINNER_COLOR)
            self.buttons[1][1].config(bg=WINNER_COLOR)
            self.buttons[2][0].config(bg=WINNER_COLOR)
            self.game_won()
            return
        if all(cell != "" for row in self.board for cell in row):
            self.game_over = True
            self.current_turn.config(text="🤝 It's a Draw!")
            for row in range(3):
                for col in range(3):
                    self.buttons[row][col].config(state="disabled")

    def game_won(self):
        self.game_over = True
        if self.winner == "X":
            self.x_score += 1
        elif self.winner == "O":
            self.o_score += 1
        self.score.config(text=f"{self.x_score} : {self.o_score}")
        self.current_turn.config(text=f"🎉 Player {self.winner} Wins!")
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state="disabled")

    def start_pvp(self):
        self.game_mode = "PvP"
        self.player_x.config(text="Player X")
        self.player_o.config(text="Player O")
        self.mode_heading.config(text="Player vs Player")
        self.menu_frame.pack_forget()
        self.main_frame.pack(fill="both",expand=True)

    def start_pvc(self):
        self.game_mode = "PvC"
        self.player_x.config(text="Player")
        self.player_o.config(text="Computer")
        self.mode_heading.config(text="Player vs Computer")
        self.menu_frame.pack_forget()
        self.main_frame.pack(fill="both",expand=True)

    def change_mode(self):
        self.new_score()
        self.game_mode = None
        self.player_x.config(text="Player X")
        self.player_o.config(text="Player O")
        self.mode_heading.config(text="Select Mode: ")
        self.main_frame.pack_forget()
        self.menu_frame.pack(fill="both",expand=True)

    def comp_move(self):
        if self.game_over:
            return
        empty = []

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    empty.append((row, col))
        if not empty:
            return
        move = self.find_winning_move("O")
        if move:
            r,c = move
            self.make_computer_move(r,c)
            return
        move = self.find_winning_move("X")
        if move:
            r,c = move
            self.make_computer_move(r,c)
            return
        if self.board[1][1] == "":
            self.make_computer_move(1, 1)
            return
        if self.board[0][0] == "":
            self.make_computer_move(0,0)
            return
        if self.board[0][2] == "":
            self.make_computer_move(0,2)
            return
        if self.board[2][2] == "":
            self.make_computer_move(2,2)
            return
        if self.board[2][0] == "":
            self.make_computer_move(2,0)
            return

        r,c = random.choice(empty)
        self.make_computer_move(r, c)

    def find_winning_move(self,player):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    self.board[row][col] = player
                    if self.is_winner(player):
                        self.board[row][col] = ""
                        return (row, col)
                    self.board[row][col] = ""
        return None
    def is_winner(self,player):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == player:
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col]== player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

        return False
    def make_computer_move(self,r,c):
        self.board[r][c] = "O"
        self.buttons[r][c].config(text="O",fg=O_COLOR)
        self.check_winner()
        if not self.game_over:
            self.switch_player()