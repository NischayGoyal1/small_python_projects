# Flash App capstone project
from tkinter import *
import pandas as pd


# -------------------------reading csv--------------------#
df=pd.read_csv("data/french_words.csv").to_dict(orient="records")
n=0
# -----------------------word caraousel---------------------

def carousel():
    global n
    canva.itemconfig(c_imag,image=Imag)
    label_1["text"]="French"
    label["text"]=df[n]["French"]
    n+=1
    if n<len(df):
    
     window.after(3000,carousel)

# -----------------------on croos btn-----------

def wbtn():
    global n
    canva.itemconfig(c_imag,image=Ima)
    label_1["text"]="English"
    label["text"]=df[n-1]["English"]

# -------------on right click-----------
def rbtn():
    global n
    with open("Result.txt","a") as f:
        f.write(f"{df[n-1]} \n \n")
    label["text"]=df[n]["French"]
    n+=1

# ------------------------UI-----------------------------#


window =Tk()
window.config(bg="lightgreen")


canva=Canvas(width=900,height=560,bg="lightgreen",highlightthickness=0)
Imag=PhotoImage(file="images/card_front.png")
Ima=PhotoImage(file="images/card_back.png")
c_imag=canva.create_image(450,280,image=Imag)
canva.grid(row=0,column=0,columnspan=2)

# ---------------labels---------
label_1=Label(text="french",font=("serif",40,"bold"))
label_1.place(y=180,x=350)

label=Label(text="French",font=("serif",40,"bold"))
label.place(y=380,x=350)

# -----------button----------
cro=PhotoImage(file="images/wrong.png")
cross=Button(image=cro,bg="lightgreen",command=wbtn)
cross.grid(row=1,column=0)

ro=PhotoImage(file="images/right.png")
right=Button(image=ro,bg="lightgreen",command=rbtn)
right.grid(row=1,column=1)

carousel()

window.mainloop()

