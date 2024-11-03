import tkinter
import webbrowser
from tkinter import messagebox

w=tkinter.Tk()
w.geometry ("400x400")
w.title("BROWSER")
w.configure(bg="light blue")

#-------------------------------------------------------------------------
def display():
    webbrowser.open_new("https://www.facebook.com/",)

#--------------------------------------------------------------------------
btn=tkinter.Button(w,text="open",command=display)
btn.place(x=240,y=220)
#---------------------------------------------------------------------------

label=tkinter.Label(w,text="ENTER THE LINK            : ")
label.place(x=50,y=150)
label=tkinter.Entry(w,bd=5)
label.place(x=200,y=147)




w.mainloop()
