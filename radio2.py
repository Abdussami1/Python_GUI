from tkinter import *


root=Tk()
root.title("Radio buttons in Python")


Modes=[
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mashroom","Mashroom"),
    ("Onion","Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text,mode in Modes:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)

def clicked(value):
    mylabel=Label(root,text=value)
    mylabel.pack()

mylabel=Label(root,text=pizza.get())
mylabel.pack()

mybutton=Button(root,text="Click me!",command=lambda: clicked(pizza.get()))
mybutton.pack()

root.mainloop()