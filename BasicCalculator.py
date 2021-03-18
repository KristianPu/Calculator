def Zbroji():
    broj1 = float(x.get())
    broj2 = float(y.get())
    br = broj1 + broj2
    Rezultat.config(text = "Zbroj je: " + str(br))

def Oduzmi():
    broj1 = float(x.get())
    broj2 = float(y.get())
    br = broj1 - broj2
    Rezultat.config(text = "Razlika je: " + str(br))

def Mnozi():
    broj1 = float(x.get())
    broj2 = float(y.get())
    br = broj1 * broj2
    Rezultat.config(text = "Umnozak je: " + str(br))

def Dijeli():
    broj1 = float(x.get())
    broj2 = float(y.get())
    br = broj1 / broj2
    Rezultat.config(text = "Produkt je: " + str(br))

from tkinter import *
from tkinter import font as tkFont

window = Tk()

x = StringVar()
y = StringVar()

'''
window.minsize(400,400)
window.maxsize(800,800)'''
window.title("Basic Calculator")

ArialBig = tkFont.Font(family = 'Arial', size = 30, weight = 'bold')

BasicCal = Label(window, text = "Basic Calculator")
BasicCal.grid(row = 0, columnspan = 12)

Unos1 = Entry(window, text = x)
Unos1.grid(row = 1, columnspan = 12)

Unos2 = Entry(window, text = y)
Unos2.grid(row = 2, columnspan = 12)

TipkaPlus = Button(window, text = "+", width = 3, font = ArialBig, command = Zbroji)
TipkaPlus.grid(row = 4, column = 0)

TipkaMinus = Button(window, text = "-", width = 3, font = ArialBig, command = Oduzmi)
TipkaMinus.grid(row = 5, column = 0)

TipkaPuta = Button(window, text = "x", width = 3, font = ArialBig, command = Mnozi)
TipkaPuta.grid(row = 4, column = 1)

TipkaDijeli = Button(window, text = "÷", width = 3, font = ArialBig, command = Dijeli)
TipkaDijeli.grid(row = 5, column = 1)

Rezultat = Label(window, text = "")
Rezultat.grid(row = 3, columnspan = 12)

window.mainloop()



