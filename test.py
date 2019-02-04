from keras.models import load_model
from keras.preprocessing import image
from keras.utils import CustomObjectScope
import numpy as np
from keras.initializers import glorot_uniform

from keras.models import model_from_json

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
img = image.load_img('8.png', target_size=(img_width, img_height))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

images = np.vstack([x])
classes = model.predict_classes(images, batch_size=10)
print(classes)
output_class = {0:'Black-grass',1:'Charlock',2:'Cleavers',3:'Common Chickweed',4:'Common wheat',5:'Fat Hen',6:'Loose Silky-bent',7:'Maize',8:'Scentless Mayweed',9:'Shepherd\'s purse' ,10:'Small flowered Cranesbill',11:'Sugar beet'}
# predicting multiple images at once
# img = image.load_img('test2.jpg', target_size=(img_width, img_height))
# y = image.img_to_array(img)
# y = np.expand_dims(y, axis=0)

# # pass the list of multiple images np.vstack()
# images = np.vstack([x, y])
# classes = model.predict_classes(images, batch_size=10)

# print the classes, the images belong to
print(classes)
print(output_class[classes[0]])
