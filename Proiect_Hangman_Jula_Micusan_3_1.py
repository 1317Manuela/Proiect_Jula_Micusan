from Lista_cuvinte import *
import random
global fereastra
global fereastra2
global casuta_var
global x
from tkinter import *
def eval(event):
    global fereastra2
    global x
    global casuta_var
    x = str(casuta_var.get())
    b = Button(fereastra2, text="Incepe Jocul!", font="Jokerman 20", width=12, height=1, command=fereastra_3)
    b.place(x=230, y=400)
    b.configure(bg="lightblue", anchor=CENTER, activebackground="gray")
def fereastra_2():
    global fereastra
    global fereastra2
    global casuta_var
    fereastra.destroy()
    fereastra2 = Tk()
    fereastra2.title("Hangman Game")
    fereastra2.configure(bg="lightblue")
    fereastra2.geometry("700x500")
    titlu2 = Label(fereastra2, text="Alegeti categoria dorita:\n1.Tari\n2.Orase\n3.Animale\n4.Random",font="Jokerman 35", bg="lightblue")
    titlu2.pack(anchor=N)
    casuta_var = Entry(fereastra2, width=15)
    casuta_var.place(x=290, y=375)
    casuta_var.bind("<Return>",eval)
    fereastra2.mainloop()
def fereastra1():
    global fereastra
    fereastra=Tk()
    fereastra.title("Hangman Game")
    fereastra.configure(bg="lightblue")
    fereastra.geometry("700x500")
    titlu=Label(fereastra,text="Hangman Game!",font="Jokerman 50",bg="lightblue")
    titlu.pack(anchor=N)
    text=Label(fereastra,text="Jula Manuela\nMicusan Roxana\n3.1",font="Jokerman 15",bg="lightblue")
    text.place(x=20,y=370)
    img=PhotoImage(file="poza1.png")
    imagine=Label(fereastra,image=img)
    imagine.place(x=280,y=95)
    imagine.configure(bg="lightblue")
    b=Button(fereastra,text="Start",font="Jokerman 25",width=6,height=1,command=fereastra_2)
    b.place(x=270,y=350)
    b.configure(bg="lightblue",anchor=CENTER,activebackground="gray")
    fereastra.mainloop()
fereastra1()


