from tkinter import *

#create main window object
root = Tk()

def myClick():
    myLabel = Label(root,text='Button was clicked!')
    myLabel.pack()
#Creating a diffrent shiz
myLabel1 = Label(root, text='Hello World!')
myLabel2 = Label(root, text='This is a shutdowner',padx=50)
myButton = Button(root,text = 'Click Me!',command=myClick,fg='red')

#Putting shiz in screen to root window grid
# myLabel1.grid(row = 0, column = 0)
# myLabel2.grid(row = 1, column = 5) we cant use grid and pack in same program.
myLabel1.pack()
myLabel2.pack()

myButton.pack()



#loop the window so it doesnt close
root.mainloop()