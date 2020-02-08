from tkinter import *
root=Tk()
root.geometry('350x300')
root.title("Temperature")
root.configure(bg='#f3bd1d')

textin1=StringVar()
textin2=StringVar()

text1=Entry(root,font=("Courier New",20,'bold'),textvar=textin1,width=10,bd=5)
text1.place(x=175,y=35)

text2=Entry(root,font=("Courier New",20,'bold'),textvar=textin2,width=10,bd=5)
text2.place(x=175,y=90)

def eqbutktof():
    temp=text1.get()
    temp=float(temp)
    result=str((temp-273.15)*9/5+32)
    text2.delete(0,END) 
    text2.insert(0,result)

def eqbutftok():
    temp=text1.get()
    temp=float(temp)
    result=str((temp-32)*5/9+273.15)
    text2.delete(0,END) 
    text2.insert(0,result)

def clrbut():
    global operator1
    text1.delete(0, END)
    text2.delete(0, END)

label1=Label(root,text='Temperature Conversion',font=("Courier New",19,'bold'),bg='#f8d574',fg='#e6411f')
label1.pack()

def ftok():
    label2=Label(root,text='Farenhite F ',font=("Courier New",12,'bold'),bg='#f3bd1d',fg='black')
    label2.place(x=7,y=45)

    label3=Label(root,text='Kelivin   K ',font=("Courier New",12,'bold'),bg='#f3bd1d',fg='black')
    label3.place(x=7,y=100)

    eq=Button(root,padx=60,pady=0,bd=4,command=eqbutftok,text="=",font=("Courier New",22,'bold'))
    eq.place(x=7,y=150)
    
    clr=Button(root,padx=55,pady=0,bd=4,command=clrbut,text="CE",font=("Courier New",22,'bold'))
    clr.place(x=175,y=150)

    inch=Button(root,text='↓↑',font=("Courier New",22,'bold'),command=ktof)
    inch.place(x=145,y=220)


def ktof():
    label2=Label(root,text='Kelivin   K ',font=("Courier New",12,'bold'),bg='#f3bd1d',fg='black')
    label2.place(x=7,y=45)

    label3=Label(root,text='Farenhite F ',font=("Courier New",12,'bold'),bg='#f3bd1d',fg='black')
    label3.place(x=7,y=100)

    eq=Button(root,padx=60,pady=0,bd=4,command=eqbutktof,text="=",font=("Courier New",22,'bold'))
    eq.place(x=7,y=150)
    
    clr=Button(root,padx=55,pady=0,bd=4,command=clrbut,text="CE",font=("Courier New",22,'bold'))
    clr.place(x=175,y=150)

    inch=Button(root,text='↓↑',font=("Courier New",22,'bold'),command=ftok)
    inch.place(x=145,y=220)

ktof()
root.mainloop()
root.mainloop()