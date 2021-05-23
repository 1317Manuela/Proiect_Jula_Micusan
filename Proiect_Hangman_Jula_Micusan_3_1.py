from Lista_cuvinte import *
import random
global fereastra
global fereastra2
global casuta_var
global x
global litera
global ok
global fereastra3
global litere_folosite
global cuv
global cu
global cuvant_nou
from tkinter import *
def display_img(x):
    global fereastra3
    img1 = PhotoImage(file=x)
    imagine1 = Label(fereastra3, image=img1)
    imagine1.photo = img1
    imagine1.place(x=5, y=105)
    imagine1.configure(bg="lightblue")
def gaseste(event):
    global litera
    global fereastra3
    global valoare
    global litere_folosite
    global cuv
    global cu
    global ok
    global cuvant_nou
    global nr_imagini
    valoare = str(litera.get())
    litera.delete(0, END)
    if nr_imagini!=7:
        if cu==cuvant_nou:
            ok=1
            fereastra_4()
        else:
            if valoare in litere_folosite:
                nr_imagini = nr_imagini + 1
                display_img(Imagini[nr_imagini])
            elif valoare in cuv:
                for i in range(len(cu)):
                    if cu[i] == valoare:
                        cuvant_nou=cuvant_nou[:i]+valoare+cuvant_nou[i+1:]
                litere_folosite.append(valoare)
                cv = Label(text=cuvant_nou, font="Jokerman 25", bg="lightblue", width=15)
                cv.place(x=350, y=200)
            else:
                nr_imagini = nr_imagini + 1
                display_img(Imagini[nr_imagini])
                litere_folosite.append(valoare)
            lb1 = Label(fereastra3,text='Ati folosit literele:', font="Jokerman 13", bg="lightblue")
            lb1.place(x=5, y=45)
            lb = Label(fereastra3, text=litere_folosite, font="Jokerman 13", bg="lightblue")
            lb.place(x=170, y=45)
    if nr_imagini==7:
        ok=0
        fereastra_4()
def introduce_litera():
    global litera
    litera = Entry(fereastra3, width=15)
    litera.place(x=500, y=400)
    litera.bind("<Return>", gaseste)
def fereastra_3():
    global fereastra2
    global fereastra3
    fereastra2.destroy()
    fereastra3 = Tk()
    fereastra3.title("Hangman Game")
    fereastra3.configure(bg="lightblue")
    fereastra3.geometry("700x500")
    global x
    global nr_imagini
    global litere_folosite
    global cuv
    global cu
    global cuvant_nou
    litere_folosite=[]
    cu=''
    if x == "1":
        lb = Label(text="Ati ales categoria Tari:", font="Jokerman 15", bg="lightblue")
        lb.pack(anchor=NW)
        cuv = random.choice(Tari)
        cuv = cuv.upper()
    elif x == "2":
        lb = Label(text="Ati ales categoria Orase:", font="Jokerman 15", bg="lightblue")
        lb.pack(anchor=NW)
        cuv = random.choice(Orase)
        cuv = cuv.upper()
    elif x == "3":
        lb = Label(text="Ati ales categoria Animale:", font="Jokerman 15", bg="lightblue")
        lb.pack(anchor=NW)
        cuv = random.choice(Animale)
        cuv = cuv.upper()
    elif x == "4":
        lb = Label(text="Ati ales categoria Random:", font="Jokerman 15", bg="lightblue")
        lb.pack(anchor=NW)
        cuv = random.choice(Random)
        cuv = cuv.upper()
    else:
        lb = Label(text="Vi se va atribui un cuvant Random:", font="Jokerman 15", bg="lightblue")
        lb.pack(anchor=NW)
        cuv = random.choice(Random)
        cuv = cuv.upper()
    cuvant_nou = "_ " * len(cuv)
    cuvant = Label(text=cuvant_nou, font="Jokerman 25", bg="lightblue", width=15)
    cuvant.place(x=350, y=200)
    lb1 = Label(text="Introduceti o litera de tipar:", font="Jokerman 15", bg="lightblue")
    lb1.place(x=212, y=390)
    for i in range(len(cuv)):
        cu=cu+cuv[i]+" "
    display_img(Imagini[0])
    nr_imagini=0
    introduce_litera()
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


