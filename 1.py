from tkinter import filedialog
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tkinter import *


root = Tk()
root.title("Weed Detection")
root.resizable(0,0)
#root.iconbitmap('/home/srimanth/Desktop/Project/logo.ico')
root.config(background='ivory2')

frame = Frame(root)
second_frame=Frame(root)
third_frame=Frame(root)
frame.pack()
second_frame.pack()
third_frame.pack()

root.geometry('550x600')


message = Label(frame,text="Welcome to Detector",font=("Arial Bold",25))
message1 = Label(frame,text="PLease Click the Below Button to Upload Image!",font=("Arial Bold",15))

def clicked():
    file_path = filedialog.askopenfilename()
    print("\n {} \n".format(file_path))
    img=mpimg.imread(file_path)
    plt.imshow(img)
    plt.show()
    output()
    
def output():
    window=Tk()
    window.title("Output")
    window.geometry('550x600')
    dummy="this is dummy"
    dummy1="this is dummy1"

    
    msg = Label(window,text=dummy,font=("Arial Bold",25))
    msg1 = Label(window,text=dummy1,font=("Arial Bold",15))
    msg.pack()
    msg1.pack()
    
    


btn = Button(second_frame, text="Browse",font=("Arial Bold",15),justify="center", height=15, width=30,command=clicked)
btn.config(background='DeepSkyBlue2')

message.pack(side=TOP)
message1.pack(side=LEFT)
btn.pack(side=LEFT)
root.mainloop()
