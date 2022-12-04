from math import comb
from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from jupyterlab_server import translator

def change(text = "type", src="English", dest="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text,  src=src1, dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0, END)
    textget = change(text= msg, src=s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END, textget)


root = Tk()
root.title('Translator App - By the great Mridul')
root.geometry("500x700")
root.config(bg="red")

lab_txt = Label(root, text="Translator", font=("Time New Roman", 40, "bold"), bg="magenta")
lab_txt.place(x=100, y= 40, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text="Source text", font=("Time New Roman", 20, "bold"), fg="blue", bg="magenta")
lab_txt.place(x=100, y= 100, height=20, width=300)

Sor_txt = Text(frame, font=("Time New Roman", 15),wrap=WORD)
Sor_txt.place(x=10, y= 130, height=150, width=480)

list_text = list(LANGUAGES.values())
comb_sor = ttk.Combobox(frame, values=list_text)
comb_sor.place(x=10, y= 300, height=40, width=150)
comb_sor.set("english")

button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=170, y= 300, height=40, width=150)

comb_dest = ttk.Combobox(frame, value= list_text)
comb_dest.place(x=330, y=300, height=40, width=150)
comb_dest.set("english")

lab_txt = Label(root, text="Destination text", font=("Time New Roman", 20, "bold"), fg="blue", bg="magenta")
lab_txt.place(x=100, y= 360, height=20, width=300)


dest_txt = Text(frame, font=("Time New Roman", 15),wrap=WORD)
dest_txt.place(x=10, y= 400, height=150, width=480)


root.mainloop()