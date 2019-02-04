

import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

print("\n {} \n".format(file_path))

# window = tk.Tk()
# window.title('demo')
# canvas = tk.Canvas(window,width=500,height=500)
# canvas.pack()

# my_image=tk.PhotoImage(file=file_path)

# canvas.create_image(0,0,anchor=tk.NW,image=my_image)

# canvas = tk.Canvas(root, width = 300, height = 300)
# canvas.pack()
# img = tk.PhotoImage(file=file_path)
# canvas.create_image(20,20, anchor=tk.NW, image=img)
# tk.mainloop()

img=mpimg.imread(file_path)

plt.imshow(img)
plt.show()
