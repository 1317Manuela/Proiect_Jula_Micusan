from Lista_cuvinte import *
import random
global fereastra
global fereastra2
global casuta_var
global x
global fereastra4
global litera
global ok
global fereastra3
global fereastra0
global litere_folosite
global cuv
global cuvinte_folosite
global cu
global cuvant_nou
global ct
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
    global fereastra
    global valoare
    global litere_folosite
    global fereastra3
    global fereastra
    global cuv
    global cu
    global ok
    global cuvant_nou
    global nr_imagini
    global ct
    global fereastra4
    valoare =str(litera.get())
    valoare=valoare.upper()
    litera.delete(0, END)
    if nr_imagini!=7:
        if cu==cuvant_nou:
            ok=1
            fereastra3.destroy()
            if ct==3:
                fereastra0.destroy()
                ct=2
            else:
                fereastra4.destroy()
        else:
            if valoare in litere_folosite:
                nr_imagini = nr_imagini + 1
                display_img(Imagini[nr_imagini])
            elif valoare in cuv:
                for i in range(len(cu)):
                    if cu[i] == valoare:
                        cuvant_nou=cuvant_nou[:i]+valoare+cuvant_nou[i+1:]
                litere_folosite.append(valoare)
                cv = Label(fereastra3,text=cuvant_nou, font="Jokerman 20", bg="lightblue", width=20)
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
        fereastra3.destroy()
        if ct==3:
            fereastra0.destroy()
            ct=2
        else:
            fereastra4.destroy()
def introduce_litera():
    global litera
    litera = Entry(fereastra3, width=15)
    litera.place(x=500, y=400)
    litera.bind("<Return>", gaseste)
def fereastra_3():
    global fereastra2
    global fereastra3
    fereastra2.destroy()
    fereastra3 = Toplevel()
    fereastra3.title("Hangman Game")
    fereastra3.configure(bg="lightblue")
    fereastra3.geometry("700x500")
    global x
    global nr_imagini
    global litere_folosite
    global cuv
    global cu
    global cuvinte_folosite
    global cuvant_nou
    litere_folosite=[]
    cu=''
    if x == "1":
        lb = Label(fereastra3,text="Ati ales categoria Tari:", font="Jokerman 15", bg="lightblue")
        lb.pack(anchor=NW)
        cuv = random.choice(Tari)
        while cuv in cuvinte_folosite:
            cuv = random.choice(Tari)
        cuvinte_folosite.append(cuv)
        cuv = cuv.upper()
    elif x == "2":
        lb = Label(fereastra3,text="Ati ales categoria Orase:", font="Jokerman 15", bg="lightblue")
        lb.pack(anchor=NW)
        cuv = random.choice(Orase)
        while cuv in cuvinte_folosite:
            cuv = random.choice(Orase)
        cuvinte_folosite.append(cuv)
        cuv = cuv.upper()
    elif x == "3":
        lb = Label(fereastra3,text="Ati ales categoria Animale:", font="Jokerman 15", bg="lightblue")
        lb.pack(anchor=NW)
        cuv = random.choice(Animale)
        while cuv in cuvinte_folosite:
            cuv = random.choice(Animale)
        cuvinte_folosite.append(cuv)
        cuv = cuv.upper()
    elif x == "4":
        lb = Label(fereastra3,text="Ati ales categoria Random:", font="Jokerman 15", bg="lightblue")
        lb.pack(anchor=NW)
        cuv = random.choice(Random)
        while cuv in cuvinte_folosite:
            cuv = random.choice(Random)
        cuvinte_folosite.append(cuv)
        cuv = cuv.upper()
    else:
        lb = Label(fereastra3,text="Vi se va atribui un cuvant Random:", font="Jokerman 15", bg="lightblue")
        lb.pack(anchor=NW)
        cuv = random.choice(Random)
        while cuv in cuvinte_folosite:
            cuv = random.choice(Random)
        cuvinte_folosite.append(cuv)
        cuv = cuv.upper()
    cuvant_nou = "_ " * len(cuv)
    cuvant = Label(fereastra3,text=cuvant_nou, font="Jokerman 20", bg="lightblue", width=20)
    cuvant.place(x=350, y=200)
    lb1 = Label(fereastra3,text="Introduceti o litera:", font="Jokerman 15", bg="lightblue")
    lb1.place(x=290, y=390)
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
    b.configure(bg="lightblue", activebackground="gray")
def fereastra_2():
    global fereastra
    global fereastra2
    global casuta_var
    fereastra.destroy()
    fereastra2 = Toplevel()
    fereastra2.title("Hangman Game")
    fereastra2.configure(bg="lightblue")
    fereastra2.geometry("700x500")
    titlu2 = Label(fereastra2, text="Alegeti categoria dorita:\n1.Tari\n2.Orase\n3.Animale\n4.Random",font="Jokerman 35", bg="lightblue")
    titlu2.pack(anchor=N)
    casuta_var = Entry(fereastra2, width=15)
    casuta_var.place(x=290, y=375)
    casuta_var.bind("<Return>",eval)
def fereastra1():
    global fereastra
    global fereastra0
    global cuvinte_folosite
    global ct
    cuvinte_folosite = []
    fereastra=Toplevel()
    fereastra.title("Hangman Game")
    fereastra.configure(bg="lightblue")
    fereastra.geometry("700x500")
    titlu=Label(fereastra,text="Hangman Game!",font="Jokerman 50",bg="lightblue")
    titlu.pack(anchor=N)
    text=Label(fereastra,text="Jula Manuela\nMicusan Roxana\n3.1",font="Jokerman 15",bg="lightblue")
    text.place(x=20,y=370)
    img=PhotoImage(file="poza7.png")
    imagine=Label(fereastra,image=img)
    imagine.photo=img
    imagine.place(x=230,y=95)
    imagine.configure(bg="lightblue")
    if ct==3:
        fereastra0.withdraw()
    b=Button(fereastra,text="Start",font="Jokerman 25",width=6,height=1,command=fereastra_2)
    b.place(x=270,y=350)
    b.configure(bg="lightblue",activebackground="gray")
def fereastra_0():
    global ct
    global fereastra0
    ct=3
    fereastra0 = Tk()
    fereastra0.title("Hangman Game")
    fereastra0.configure(bg="lightblue")
    fereastra0.geometry("700x500")
    b1= Button(fereastra0, text="Accesati jocul!", font="Jokerman 25", width=18,  command=fereastra1)
    b1.place(x=150,y=200)
    b1.configure(bg="lightblue", activebackground="gray")
    fereastra0.mainloop()
def functie_button():
    global fereastra4
    fereastra1()
    fereastra4.withdraw()
def fereastra_4():
    global ok
    global fereastra4
    global cuvinte_folosite
    fereastra4 = Tk()
    fereastra4.title("Hangman Game")
    fereastra4.configure(bg="lightblue")
    fereastra4.geometry("700x500")
    if ok==1:
        lb4 = Label(fereastra4, text="Ai castigat!", font="Jokerman 50", bg="lightblue")
        lb4.pack(anchor=N)
        b1 = Button(fereastra4, text="Retry", font="Jokerman 25", width=6, height=1, command=functie_button)
        b1.place(x=270, y=150)
        b1.configure(bg="lightblue", activebackground="gray")
    if ok==0:
        lb5=Label(fereastra4,text="Ai pierdut!",font="Jokerman 50",bg="lightblue")
        lb5.pack(anchor=N)
        b2 = Button(fereastra4, text="Retry", font="Jokerman 25", width=6, height=1, command=functie_button)
        b2.place(x=270, y=150)
        b2.configure(bg="lightblue", activebackground="gray")
    fereastra4.mainloop()
fereastra_0()
fereastra_4()