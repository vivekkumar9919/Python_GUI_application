

from tkinter import *

root=Tk()
root.title('Calculator')
root.geometry('370x600')
root.config(bg="#66ffe0")


def click(event):
    # print('helo')
    global scvalue
    val=event.widget.cget("text")
    # print(val)
    if val=="=":
        if scvalue.get().isdigit():
            ans=int(scvalue.get())
        else:
            try:
                ans=eval(screen.get())
            except Exception as e:
                print(e)
                ans='Error'

        scvalue.set(ans)
        screen.update()
    elif val=="c":
        scvalue.set("")
    else:
        scvalue.set(scvalue.get()+val)
        screen.update()

# Entry widget
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font='lucide 30 bold',borderwidth=7 ,bg='#ffffb3')
screen.pack(fill=X,ipady=6,padx=10,pady=10)


frame1=Frame(root,bg='#4da6ff',borderwidth=5,relief=RAISED)
frame1.pack(pady=5)
bt9=Button(frame1,text="9",pady=20,padx=20,font='lucide 17 bold',fg='red',bg='#ffffb3')
bt9.pack(side='left',padx=6,pady=6)
bt9.bind("<Button-1>",click)
bt9=Button(frame1,text="8",pady=20,padx=20,font='lucide 17 bold',fg='red',bg='#ffffb3')
bt9.pack(side='left',padx=6,pady=6)
bt9.bind("<Button-1>",click)
bt9=Button(frame1,text="7",pady=20,padx=20,font='lucide 17 bold',fg='red',bg='#ffffb3')
bt9.pack(side='left',padx=6,pady=6)
bt9.bind("<Button-1>",click)
bt9=Button(frame1,text='+',pady=20,padx=20,font='lucide 17 bold',fg='#ff00bf',bg='#ffffb3')
bt9.pack(side='left',padx=6,pady=6)
bt9.bind("<Button-1>",click)


frame1=Frame(root,bg='#4da6ff',borderwidth=5,relief=RAISED)
frame1.pack(pady=5)
bt9=Button(frame1,text="6",pady=20,padx=20,font='lucide 17 bold',fg='red',bg='#ffffb3')
bt9.pack(side='left',padx=6,pady=6)
bt9.bind("<Button-1>",click)
bt9=Button(frame1,text="5",pady=20,padx=20,font='lucide 17 bold',fg='red',bg='#ffffb3')
bt9.pack(side='left',padx=6,pady=6)
bt9.bind("<Button-1>",click)
bt9=Button(frame1,text="4",pady=20,padx=20,font='lucide 17 bold',fg='red',bg='#ffffb3')
bt9.pack(side='left',padx=6,pady=6)
bt9.bind("<Button-1>",click)
bt9=Button(frame1,text='-',pady=20,padx=20,font='lucide 17 bold',fg='#ff00bf',bg='#ffffb3')
bt9.pack(side='left',padx=6,pady=6)
bt9.bind("<Button-1>",click)



frame1=Frame(root,bg='#4da6ff',borderwidth=5,relief=RAISED)
frame1.pack(pady=5)
bt9=Button(frame1,text="3",pady=20,padx=20,font='lucide 17 bold',fg='red',bg='#ffffb3')
bt9.pack(side='left',padx=6,pady=6)
bt9.bind("<Button-1>",click)
bt9=Button(frame1,text="2",pady=20,padx=20,font='lucide 17 bold',fg='red',bg='#ffffb3')
bt9.pack(side='left',padx=6,pady=6)
bt9.bind("<Button-1>",click)
bt9=Button(frame1,text="1",pady=20,padx=20,font='lucide 17 bold',fg='red',bg='#ffffb3')
bt9.pack(side='left',padx=6,pady=6)
bt9.bind("<Button-1>",click)
bt9=Button(frame1,text='*',pady=20,padx=20,font='lucide 17 bold',fg='#ff00bf',bg='#ffffb3')
bt9.pack(side='left',padx=6,pady=6)
bt9.bind("<Button-1>",click)


frame1=Frame(root,bg='#4da6ff',borderwidth=5,relief=RAISED)
frame1.pack(pady=5)
bt9=Button(frame1,text="/",pady=20,padx=20,font='lucide 17 bold',fg='#ff00bf',bg='#ffffb3')
bt9.pack(side='left',padx=6,pady=6)
bt9.bind("<Button-1>",click)
bt9=Button(frame1,text="%",pady=20,padx=20,font='lucide 17 bold',fg='#ff00bf',bg='#ffffb3')
bt9.pack(side='left',padx=6,pady=6)
bt9.bind("<Button-1>",click)
bt9=Button(frame1,text="c",pady=20,padx=20,font='lucide 17 bold',fg='#008000',bg='#ffffb3')
bt9.pack(side='left',padx=6,pady=6)
bt9.bind("<Button-1>",click)
bt9=Button(frame1,text='=',pady=20,padx=20,font='lucide 17 bold',fg='red',bg='#ffffb3')
bt9.pack(side='left',padx=6,pady=6)
bt9.bind("<Button-1>",click)




root.mainloop()