from tkinter import *

class Program():
    answers = {"basketball":17,"badminton":5,"baseball":1,"football":2,"swimming":3,
               "money":11,"happiness":3,"immortality":3,"get a dream job":4,"girlfriend":2,"more wishes":2,
               "math":10,"art":2,"english":5,"computer":2,"science":6,"p.e.":2,
               "cat":15,"dog":10,"whale":1,"crocodile":1,"snake":1,"fish":1,"penguin":1,
               "black hole":3, "mars":2,"other galaxy":4,"sun":8,"moon":3,"pluto":3}

    def __init__(self,root):
        self.root = root
        self.P1 = 0
        self.P1_str = StringVar()
        self.P1_str.set("Team 1: 0")

        self.P2 = 0
        self.P2_str = StringVar()
        self.P2_str.set("Team 2: 0")

        self.P3 = 0
        self.P3_str = StringVar()
        self.P3_str.set("Team 3: 0")

        self.answer_state = StringVar()
        self.answer_state.set("Not Answered Yet!")

        self.current_player = "P1"

        self.change_to_P1 = Button(root,text="Team 1",command=lambda: self.change_player("P1"))
        self.change_to_P2 = Button(root,text="Team 2" ,command=lambda: self.change_player("P2"))
        self.change_to_P3 = Button(root,text ="Team 3",command=lambda: self.change_player("P3"))
        self.input_answer = Entry(root)
        self.enter = Button(root,command=self.enter)
        self.current_answer_state = Label(root,textvariable=self.answer_state)
        self.P1_points = Label(root,textvariable=self.P1_str)
        self.P2_points = Label(root, textvariable=self.P2_str)
        self.P3_points = Label(root, textvariable=self.P3_str)

        self.change_to_P1.grid(row=0,column=0)
        self.change_to_P2.grid(row=0,column=1)
        self.change_to_P3.grid(row=0,column=2)
        self.input_answer.grid(row=3,column=1)
        self.enter.grid(row=4,column=1)
        self.current_answer_state.grid(row=2,column=1)
        self.P1_points.grid(row=1,column=0)
        self.P2_points.grid(row=1,column=1)
        self.P3_points.grid(row=1,column=2)

    def enter(self):
        current_answer = self.input_answer.get()
        if current_answer in Program.answers:
            self.answer_state.set("Correct")
            if self.current_player == "P1":
                self.P1 += Program.answers[current_answer]
                self.P1_str.set("Team 1: " + str(self.P1))
            elif self.current_player == "P2":
                self.P2 += Program.answers[current_answer]
                self.P2_str.set("Team 2: " + str(self.P2))
            elif self.current_player == "P3":
                self.P3 += Program.answers[current_answer]
                self.P3_str.set("Team 3: " + str(self.P3))
        else:
            self.answer_state.set("Wrong")

    def change_player(self,player):
        self.current_player = player
    

def main():
    root = Tk()
    program = Program(root)
    root.mainloop()

main()