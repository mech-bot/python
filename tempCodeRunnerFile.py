from tkinter import *
from tkinter import ttk
from tkinter import messagebox as m

top = Tk()

top.geometry("500x500")

def helloCallBack():

    msg=m.showinfo("Hello Python", "Hello World")

B = Button(top, text ="Hello", fg="blue", bg="white", command = helloCallBack)

B.place(x=50,y=50)

CheckVar1 = IntVar()

CheckVar2 = IntVar()

C1 = Checkbutton(top, text = "Music", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20, )

C2 = Checkbutton(top, text = "Video", variable = CheckVar2, onvalue = 1, offvalue = 0, height=5, width = 20)

C1.pack()

C2.pack()


langs = ["C", "C++", "Java", "Python", "PHP"]

Combo = ttk.Combobox(top, values = langs)

Combo.set("Pick an Option")

Combo.pack(padx = 5, pady = 5)
top.mainloop()