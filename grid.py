from tkinter import *

root = Tk()

# Creating a label widget
a = Label(root,text="Hello World!\n")
b = Label(root,text="My name is Abdus Sami")

#Showing it onto the screen
a.grid(row=0,column=0)
b.grid(row=1,column=1)


root.mainloop()
