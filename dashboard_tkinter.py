import tkinter as tk
from tkinter import *
window=tk.Tk()
window.title('DashBoard')
#config our rows and columns
button1=Button(window,text='Button1')
button2=Button(window,text='Button2')
button3=Button(window,text="Button3")
button4=Button(window,text="Button4")
button5=Button(window,text="Button5")
button6=Button(window,text="Button6")
button7=Button(window,text="Button7")
button1.place(relx=0, rely=.08, relwidth=.06, relheight=.06)
button2.place(relx=0,rely=.16,relwidth=.06, relheight=.06)
button3.place(relx=0, rely=.24, relwidth=.06, relheight=.06)
button4.place(relx=0,rely=.32,relwidth=.06, relheight=.06)
button5.place(relx=.08,rely=0,relwidth=.06, relheight=.06)
button6.place(relx=.16, rely=0, relwidth=.06, relheight=.06)
button7.place(relx=.24,rely=0,relwidth=.06, relheight=.06)
window.geometry('1000x600')
window.mainloop()