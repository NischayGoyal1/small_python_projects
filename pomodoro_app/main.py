from tkinter import *
from turtle import bgcolor
from urllib import response

from matplotlib import image
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
tim=NONE
# ---------------------------- TIMER RESET ------------------------------- # 
def reseter():
    window.after_cancel(tim)
    reps=0
    tlabel["text"]="Timer"
    canva.itemconfig(timer,text="00:00")
#---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_mech():
    global reps
    reps+=1
    if reps%8==0:
        count_down(LONG_BREAK_MIN*60)
        tlabel["text"]="LONG BREAK"
    elif reps%2==0:
        count_down(SHORT_BREAK_MIN*60)
        tlabel["text"]="SHORT BREAk"

    else:
        count_down(WORK_MIN*60)
        tlabel["text"]="WORK"
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes=count//60
    seconds=count%60
    if minutes<10:
        minutes=f"0{minutes}"
    canva.itemconfig(timer,text=f"{minutes}:{seconds}")
    if count>0:
        global tim
        tim=window.after(1000,count_down,count-1)
    else:
        timer_mech()

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.config(padx=40,pady=40,bg=YELLOW)
canva=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
# canva.config(padx=30,pady=30)
bimag=PhotoImage(file="tomato.png")
canva.create_image(100,112,image=bimag)
timer=canva.create_text(103,120,text="00:00",font=(FONT_NAME,25,"bold"),fill="white")
canva.grid(row=1,column=1)
start_btn=Button(text="Start")
start_btn.grid(row=2,column=0)
reset_btn=Button(text="Reset",command=reseter)
reset_btn.grid(row=2,column=3)
tlabel=Label(text="Timer",font=(FONT_NAME,20,"bold"))
tlabel.config(pady=20)
tlabel.grid(row=0,column=1)

# timer_mech(1)
timer_mech()
















window.mainloop()