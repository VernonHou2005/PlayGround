from tkinter import *

top = Tk()
top.geometry('200x50')
helloLabel = Label(top,text = 'hello world', font = 'Helvetica -14 bold')
helloLabel.pack(fill = Y)
scale = Scale(top,from_ = 10, to = 40, command = helloLabel.resize)
quitButton = Button(top, text = 'quit', command = top.quit)
quitButton.pack(fill = X)
mainloop()
