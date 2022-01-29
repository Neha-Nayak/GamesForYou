import tkinter
import random
import time
from tkinter import *
from tkinter import Tk, Button, DISABLED, messagebox
from PIL import ImageTk
window=Tk()
window.title("Games For You")
window.geometry('595x385')

def Match_Maker():
    # os.system('D:\Coders_club\Games_py\games\MatchMaker.py')
    global first
    global previousx, previousy
    def show_symbol(x, y):
        global first
        global previousx, previousy
        buttons[x, y]['text'] = button_symbols[x, y]
        buttons[x, y].update_idletasks()
        if first:
            previousx = x
            previousy = y
            first = False
        elif previousx != x or previousy != y:
            if buttons[previousx, previousy]['text'] != buttons[x, y]['text']:
                time.sleep(0.5)
                buttons[previousx, previousy]['text'] = ' '
                buttons[x, y]['text'] = ' '
            else:
                buttons[previousx, previousy]['command'] = DISABLED
                buttons[x, y]['command'] = DISABLED
            first = True    
    
    win = Tk()
    win.title('Matching Game')
    win.resizable(width=False, height=False)
    first = True
    previousx = 0
    previousy = 0
    buttons = {}
    button_symbols = {}
    symbols = [u'\u2702', u'\u2705', u'\u2708', u'\u2709', u'\u270A', u'\u270B',
               u'\u270C', u'\u270F', u'\u2712', u'\u2714', u'\u2716', u'\u2728',
               u'\u2702', u'\u2705', u'\u2708', u'\u2709', u'\u270A', u'\u270B',
               u'\u270C', u'\u270F', u'\u2712', u'\u2714', u'\u2716', u'\u2728']
    random.shuffle(symbols)
    
    for x in range(6):
        for y in range(4):
            button = Button(win,command=lambda x=x, y=y: show_symbol(x, y), width=10, height=8,bg='#898bc7')
            button.grid(column=x, row=y)
            buttons[x, y] = button
            button_symbols[x, y] = symbols.pop()
            
    # flag=0
    # for x in range(6):
    #     for y in range(4):
    #         # print(buttons[x, y]['command'])
    #         if button_symbols[x, y] == symbols.pop():
    #             flag=1
    # if flag==1:
    #   messagebox.showinfo("Win","You Won") 
           
          
    # def exit1():
    #     exit()
    # def second_win():
    #     window2=Tk()
    #     window2.geometry('250x200')
    #     label_2 = Label(window2, text="YOU WON", relief='solid', font=("arial",'30','bold'),fg='white',bg='#1f1538')
    #     label_2.place(x=30, y=70)
    #     b_2 = Button(window2, text="OK", width=12, bg='brown', fg='white', command=exit1)
    #     b_2.place(x=80, y=110)  
    # b3 = Button(win, text="GOTO", width=12, bg='brown', fg='white', command=second_win)
    # b3.place(x=220, y=420)     
    win.mainloop()
    
score = 0
timeleft = 30
def color_game():
    #os.system('D:\Coders_club\Games_py\games\color_game.py')
    colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']

    def startGame(event):
        if timeleft == 30:
            countdown()
        nextColour()

    def nextColour():
        global score
        global timeleft
        if timeleft > 0:
            e.focus_set()
            if e.get().lower() == colours[1].lower():
                score += 1
            e.delete(0, tkinter.END)
            random.shuffle(colours)
            label.config(fg=str(colours[1]), text=str(colours[0]))
            scoreLabel.config(text="Score: " + str(score))

    def countdown():
        global timeleft
        if timeleft > 0:
            timeleft -= 1
            timeLabel.config(text="Time left: " + str(timeleft))
            timeLabel.after(1000, countdown)

    root = Tk()
    root.title("COLOR GAME")
    root.geometry("375x300")
    root.configure(bg='#1f1538')
    instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!",font=('Helvetica', 10),fg='white',bg='#1f1538')
    instructions.pack()
    scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 20,'bold'),fg='white',bg='#1f1538')
    scoreLabel.pack()
    timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12,'bold'),fg='white',bg='#1f1538')
    timeLabel.pack()
    label = tkinter.Label(root, font=('Helvetica', 60),fg='white',bg='#1f1538')
    label.pack()
    e = tkinter.Entry(root)
    root.bind('<Return>', startGame)
    e.pack()
    e.focus_set()
    root.mainloop()

bg = ImageTk.PhotoImage(file = r"bg_img.jpg")
label1 = Label( window, image = bg)
label1.place(x = 0, y = 0)

Headlabel = tkinter.Label(window, text="Games For You",font=('Helvetica', 60),fg='Gold',bg='#1f1538')
Headlabel.pack()
instruction = tkinter.Label(window, text="Select the Game you want to Play",font=('Helvetica', 12),fg='white',bg='#1f1538')
instruction.pack()

btn1 = Button(window, text ="Matching Game",font=('Helvetica', 12, 'bold'),fg='#201b2e', command = Match_Maker)
btn1.place(x=245,y=180)

btn2 = Button(window, text ="Color Game",font=('Helvetica', 12, 'bold'),fg='#201b2e', command = color_game)
btn2.place(x=258,y=240)

window.mainloop()

