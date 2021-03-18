def Percentage():
    y = x.get().replace(".",",")
    if "%" in y:
        t = y.find("%") + 1
        if y[t+1].isdigit():
            r = int(y[t+1:])
            x.set(y[0:t+1] + str(r/100).replace(".",",") + "%")
    integ = int(y)
    x.set(str(integ/100) + "%")

def PlusMinus():
    y = x.get()
    if int(y) > -1:
        y = "-" + y
    else:
        y = y.replace("-","")
    x.set(y)

def DeleteOne():
    y = x.get()
    x.set(y[:-1])

def DeleteAll():
    x.set("")

def Insert1(text):
    y = x.get().replace(".",",")
    br = len(y)
    if br == 0:
        entry1.insert(br,text)
    #elif y[0] == "0" and y[1] == ",":
     #   entry1.insert(br,text)
    elif y[0] == "0" and "0123456789" not in text:
        x.set(text)
    else:
        entry1.insert(br,text)
        

def Operations():
    y = x.get().replace(",",".").replace("%","")
    radnja = eval(y)
    if int(radnja) == float(radnja):
        nt = int(radnja)
        x.set((str(nt)).replace(".",","))
    else:
        fl = round(radnja,10)
        x.set((str(fl)).replace(".",","))

from tkinter import *
from tkinter import font as tkFont

window = Tk()

x = StringVar()

window.title("Calculator")

HelReg = tkFont.Font(family = 'Helvetica', size = 40)

HelBold = tkFont.Font(family = 'Helvetica', size = 40, weight = 'bold')

#window.minsize(400, 400) trenutno ne treba window size mjenjati zbog izgleda kalkulatora
entry1 = Entry(window, text = x, font = HelReg, width = 14)  

entry1.grid(row = 1, columnspan = 123)

button1 = Button(window, text = '0', width = 3, font = HelBold, command = lambda: Insert1("0"))
button1.grid(row = 6, column = 1)

button1 = Button(window, text = '1', width = 3, font = HelBold, command = lambda: Insert1("1"))
button1.grid(row = 5, column = 0)

button1 = Button(window, text = '2', width = 3, font = HelBold, command = lambda: Insert1("2"))
button1.grid(row = 5, column = 1)

button1 = Button(window, text = '3', width = 3, font = HelBold, command = lambda: Insert1("3"))
button1.grid(row = 5, column = 2)

button1 = Button(window, text = '4', width = 3, font = HelBold, command = lambda: Insert1("4"))
button1.grid(row = 4, column = 0)

button1 = Button(window, text = '5', width = 3, font = HelBold, command = lambda: Insert1("5"))
button1.grid(row = 4, column = 1)

button1 = Button(window, text = '6', width = 3, font = HelBold, command = lambda: Insert1("6"))
button1.grid(row = 4, column = 2)

button1 = Button(window, text = '7', width = 3, font = HelBold, command = lambda: Insert1("7"))
button1.grid(row = 3, column = 0)

button1 = Button(window, text = '8', width = 3, font = HelBold, command = lambda: Insert1("8"))
button1.grid(row = 3, column = 1)

button1 = Button(window, text = '9', width = 3, font = HelBold, command = lambda: Insert1("9"))
button1.grid(row = 3, column = 2)

button1 = Button(window, text = '+', width = 3, font = HelBold, command = lambda: Insert1("+"))
button1.grid(row = 5, column = 3)

button1 = Button(window, text = '-', width = 3, font = HelBold, command = lambda: Insert1("-"))
button1.grid(row = 4, column = 3)

button1 = Button(window, text = '*', width = 3, font = HelBold, command = lambda: Insert1("*"))
button1.grid(row = 3, column = 3)

button1 = Button(window, text = '/', width = 3, font = HelBold, command = lambda: Insert1("/"))
button1.grid(row = 2, column = 3)

button1 = Button(window, text = '=', width = 3, font = HelBold, command = Operations)
button1.grid(row = 6, column = 3)

button1 = Button(window, text = 'C', width = 3, font = HelBold, command = DeleteAll)
button1.grid(row = 2, column = 1)

button1 = Button(window, text = 'CE', width = 3, font = HelBold, command = DeleteOne)
button1.grid(row = 2, column = 2)

button1 = Button(window, text = ',', width = 3, font = HelBold, command = lambda: Insert1(","))
button1.grid(row = 6, column = 2)

button1 = Button(window, text = '+/-', width = 3, font = HelBold, command = PlusMinus)
button1.grid(row = 6, column = 0)

button1 = Button(window, text = '%', width = 3, font = HelBold, command = Percentage)
button1.grid(row = 2, column = 0)

window.mainloop()    
