from keras.models import load_model
from keras.preprocessing import image
from keras.utils import CustomObjectScope
import numpy as np
from keras.initializers import glorot_uniform

from keras.models import model_from_json

from tkinter import filedialog
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tkinter import *

root = 0
frame = 0
def model(fpath):
    with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
        model = load_model('my_model.h5')
    # dimensions of our images
    img_width, img_height = 96, 96

    # load the model we saved
    # model = load_model('my_model.h5')
    model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

    # predicting images
    img = image.load_img(fpath, target_size=(img_width, img_height))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict_classes(images, batch_size=10)
    
    print(classes[0])
    return classes


def welcome():
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
    btn = Button(second_frame, text="Browse",font=("Arial Bold",15),justify="center", height=15, width=30,command=clicked)
    btn.config(background='DeepSkyBlue2')
    message.pack(side=TOP)
    message1.pack(side=LEFT)
    btn.pack(side=LEFT)
    root.mainloop()

def clicked():
    file_path = filedialog.askopenfilename()
    print("\n {} \n".format(file_path))
    img=mpimg.imread(file_path)
    plt.imshow(img)
    plt.show()
    
    classes = model(file_path)
    output(classes)

    
def output(classes):
    window=Tk()
    window.title("Output")
    window.geometry('550x600')
    res = "Error getting the file"
    desc = "The file(image) could not be found or located."
    output_class = {0:'Black-grass',1:'Charlock',2:'Cleavers',3:'Common Chickweed',4:'Common wheat',5:'Fat Hen',6:'Loose Silky-bent',7:'Maize',8:'Scentless Mayweed',9:'Shepherd\'s purse' ,10:'Small flowered Cranesbill',11:'Sugar beet'}
    print(classes[0])
    print(output_class[classes[0]])
    res = output_class[classes[0]]
    desc = 'Class Number : {}'.format(classes[0])
    msg = Label(window,text=res,font=("Arial Bold",25))
    msg1 = Label(window,text=desc,font=("Arial Bold",15))
    msg.pack()
    msg1.pack()
    
if(__name__ == '__main__'):

    welcome()