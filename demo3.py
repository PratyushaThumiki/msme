from tkinter import *
window=Tk()
window.title("Welcome to App")
lb=Label(window,text="Hello",font=("Times New Roman",50))
lb.grid(column=0, row=0)
bt=Button(window,text="Browse")

bt.pack()
window.mainloop()
