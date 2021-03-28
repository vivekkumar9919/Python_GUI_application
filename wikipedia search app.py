

from tkinter import  *
import wikipedia as wi
import tkinter.font as fnt
import tkinter.ttk as ttk
import tkinter.messagebox as tsmg

def se():
    entery_val=entry_w.get()
    search_result.delete(1.0, END)
    try:
        ans_val=wi.summary(entery_val)
        search_result.insert(INSERT,ans_val)
    except:
        search_result.insert(INSERT,"Check your internet connection or input ")
        tsmg.showinfo('Error',"Check your internet connection or input ")

root=Tk()
root.geometry("700x500")
root.title("Wikipedia search app")
root.config(bg="#66ffe0")
myfont=fnt.Font(family='Helvetica',size=30)
myfont2=fnt.Font(family="Helvetica 12 bold italic",size=20,slant='italic')


# for button styling

style = ttk.Style()
style.theme_use("classic")
style.map("new.TButton",background=[('!active','red'),('pressed', 'green'),('active', '#FF6666')])


label1=Label(root,text="Wikipedia Search App",font=myfont,pady=15,bg="#66ffe0",fg='Blue')

label1.pack()

frame1=Frame(root, borderwidth = 6,relief = SUNKEN,pady=10,padx=10,bg="#ffff80")
frame1.pack(side="top",fill=X)
# setext=Label(frame1,text='Search Here',font=23)
# setext.pack(side='left',ipadx=50,pady=1)
entry_w=Entry(frame1,width=50,font=23,borderwidth=8,relief=SUNKEN)
entry_w.pack(ipady=5)
sbutton=ttk.Button(frame1,text="Search",command=se,cursor="hand2",style="new.TButton")
sbutton.pack()



frame2=Frame(root , borderwidth = 5,relief = SUNKEN,pady=8,padx=8,bg='#ff66d9')
frame2.pack()
search_result=Text(frame2,yscrollcommand=Scrollbar.set,width=72,wrap=WORD,padx=8,)
search_result.pack(side="left")
scr=Scrollbar(frame2)
scr.pack(side="right",fill=Y)
scr.config(command=search_result.yview)


frame3=Frame(root , borderwidth = 6,relief =FLAT,width=50,bg="#66ffe0")
frame3.pack(side="bottom")
lb3=Label(frame3,text="created by vivek kumar",pady=20,font=myfont2,bg='#66ffe0',fg='Blue')
# frame3['font']=fnt.Font(family='italic')
lb3.pack()


root.mainloop()
