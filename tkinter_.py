# from tkinter import *

# from tkinter import messagebox

# top = Tk()

# top.geometry("100x100")

# def helloCallBack():

#     msg=messagebox.showinfo("Hello Python", "Hello World")

# B = Button(top, text ="Hello", command = helloCallBack)

# B.place(x=50,y=50)
# from tkinter import *

# from tkinter import messagebox

# top = Tk()

# top.geometry("300x200")

# def fun():

#     messagebox.showinfo("Hello", "Blue Button clicked")

# btn1 = Button(top, text = "Red", bg="red", fg="white",width=10)

# btn1.pack( side = LEFT)

# btn2 = Button(top, text = "Green", bg="green",fg="white",width=10,height=5,

# activebackground="yellow")

# btn2.pack( side = TOP)

# btn3 = Button(top, text ="Blue",bg="blue",fg="white",
# padx=10,pady=10,command=fun)

# btn3.pack( side = BOTTOM)
# top.mainloop()

# from tkinter import *

# top = Tk()

# L1 = Label(top, text="User Name")

# L1.pack( side = LEFT)

# E1 = Entry(top, bd =5)

# E1.pack(side = LEFT)

# top.mainloop()

# from tkinter import *

# top = Tk()

# top.geometry("300x200")

# enty0 = Entry(top,width="30")

# enty0.place(x=50,y=40)

# enty1 = Entry(top,bg="yellow",width="30")

# enty1.place(x=50,y=70)

# enty2 = Entry(top,fg="red",show="*")

# enty2.place(x=50,y=100)

# top.mainloop()

from tkinter import *

root = Tk()

scrollbar = Scrollbar(root)
scrollbar2 = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )
scrollbar2.pack( side = BOTTOM, fill=X )

mylist = Listbox(root, yscrollcommand = scrollbar.set ,xscrollcommand=scrollbar2.set )

for line in range(100):

    mylist.insert(END,"This is lindkjngjhdjkfkje number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )

scrollbar.config( command = mylist.yview )
scrollbar2.config( command = mylist.xview )

mainloop()