from Lista_cuvinte import *
import random
from tkinter import *
def fereastra1():
    fereastra=Tk()
    fereastra.title("Hangman Game")
    fereastra.configure(bg="lightblue")
    fereastra.geometry("700x500")
    titlu=Label(fereastra,text="Hangman Game!",font="Jokerman 50",bg="lightblue")
    titlu.pack(anchor=N)
    text=Label(fereastra,text="Jula Manuela\nMicusan Roxana\n3.1",font="Jokerman 15",bg="lightblue")
    text.place(x=20,y=370)
    img=PhotoImage(file="6.png")
    imagine=Label(fereastra,image=img)
    imagine.place(x=552,y=81)
    imagine.configure(bg="lightblue")
    def fereastra_2():
        fereastra.destroy()
        fereastra2=Tk()
        fereastra2.title("Hangman Game")
        fereastra2.configure(bg="lightblue")
        fereastra2.geometry("700x500")
        titlu2 = Label(fereastra2, text="Alegeti categoria dorita:\n1.Tari\n2.Orase\n3.Animale\n4.Random", font="Jokerman 35", bg="lightblue")
        titlu2.pack(anchor=N)
    b=Button(fereastra,text="Start",font="Jokerman 25",width=6,height=1,command=fereastra_2)
    b.place(x=270,y=170)
    b.configure(bg="lightblue",anchor=CENTER,activebackground="skyblue")
    fereastra.mainloop()
fereastra1()

