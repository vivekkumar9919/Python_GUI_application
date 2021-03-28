

from tkinter import *
from tkinter import colorchooser

def clr():
    val=colorchooser.askcolor(title='Select color')
    # print(f" rgb value and hex value are respectivily {val}")
    # print(f'Hex value is {val[1]}')
    print(val[1])
    root.config(bg=val[1])
    # val2=root.configure(bg=val[1])
    # print(type(val2))

root=Tk()
root.geometry('500x500')
root.title('Color Picker')

btn=Button(root,text='Change Color',command=clr)
btn.pack()


root.mainloop()