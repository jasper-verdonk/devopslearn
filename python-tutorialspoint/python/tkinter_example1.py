from tkinter import *

root = Tk()

label1 = Label(root, text = 'Name')
label2 = Label(root, text = 'Email Address')

label1.grid(row = 0, column = 0, sticky = W, pady = 5)
label2.grid(row = 1, column = 0, sticky = W, pady = 5)

entry1 = Entry(root)
entry2 = Entry(root)

entry1.grid(row = 0, column = 1, pady = 5)
entry2.grid(row = 1, column = 1, pady = 5)

check1 = Checkbutton(root, text = "Download")
check1.grid(row = 2, column = 0, sticky = W, columnspan=2)

img = PhotoImage(file = r"C:\Users\everjas\Red Bee Media Limited\Galileo and Security Programmes - Connectivity Transformation - Detailed Design Phase\Documents\Courses\Pictures\Python.PNG")
img1 = img.subsample(2, 2)

Label(root, image = img1).grid(row = 0, column = 2, 
                               columnspan = 2, rowspan = 2, padx = 5, pady = 5)

button1 = Button(root, text = "Zoom In")
button2 = Button(root, text = "Zoom Out")

button1.grid(row = 2, column = 2, sticky = E)
button2.grid(row = 2, column = 3, sticky = E)

root.mainloop()