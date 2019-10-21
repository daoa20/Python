from tkinter import *

window = Tk()

t = Label(text="Calculator")
t.grid(row=0, column=0)

e = Text(window, height=1, width=20)
e.grid(row=1, columnspan=4)

a = 0
b = 0
c = 0
d = ""
ans = 0

def number7():
    if (b == 0 or b == 10):
        e.insert(END, 7)
    else:
        e.delete(1.0, END)
        e.insert(END, 7)

def number8():
    if (b == 0 or b == 10):
        e.insert(END, 8)
    else:
        e.delete(1.0, END)
        e.insert(END, 8)

def number9():
    if (b == 0 or b == 10):
        e.insert(END, 9)
    else:
        e.delete(1.0, END)
        e.insert(END, 9)

def number6():
    if (b == 0 or b == 10):
        e.insert(END, 6)
    else:
        e.delete(1.0, END)
        e.insert(END, 6)

def number5():
    if (b == 0 or b == 10):
        e.insert(END, 5)
    else:
        e.delete(1.0, END)
        e.insert(END, 5)

def number4():
    if (b == 0 or b == 10):
        e.insert(END, 4)
    else:
        e.delete(1.0, END)
        e.insert(END, 4)

def number3():
    if (b == 0 or b == 10):
        e.insert(END, 3)
    else:
        e.delete(1.0, END)
        e.insert(END, 3)

def number2():
    if (b == 0 or b == 10):
        e.insert(END, 2)
    else:
        e.delete(1.0, END)
        e.insert(END, 2)

def number1():
    if (b == 0 or b == 10):
        e.insert(END, 1)
    else:
        e.delete(1.0, END)
        e.insert(END, 1)

def number0():
    if (b == 0 or b == 10):
        e.insert(END, 0)
    else:
        e.delete(1.0, END)
        e.insert(END, 0)

def clear():
    e.delete(1.0, END)

def mod():
    global a
    a = e.get(1.0, END)
    global b
    b = 1

def times():
    global a
    a = e.get(1.0, END)
    global b
    b = 6

def exp():
    global a
    global b
    a = e.get(1.0, END)
    b = 2

def sq():
    global a
    global ans
    a = e.get(1.0, END)
    ans = float(a)**2
    e.delete(1.0, END)
    e.insert(END, ans)
    b = 10

def frac():
    global a
    global ans
    a = e.get(1.0, END)
    ans = 1/float(a)
    e.delete(1.0, END)
    e.insert(END, ans)
    b = 10

def an():
    e.delete(1.0, END)
    e.insert(END, ans)

def de():
    global d
    d = e.get(1.0, END)
    e.delete(1.0, END)
    e.insert(END, d[:-2])

def di():
    global a
    global b
    a = e.get(1.0, END)
    b = 5

def minus():
    global a
    global b
    global d
    d = e.get(1.0, END)
    if(d != ""):
        a = e.get(1.0, END)
        b = 7
    elif(d == ""):
        e.insert(1.0, "-")

def plus():
    global a
    global b
    a = e.get(1.0, END)
    b = 8

def point():
    e.insert(END, ".")

def neg():
    global d
    d = e.get(1.0)
    if (d[0] == "-"):
        e.delete(1.0)
    else:
        e.insert(1.0, "-")

def eq():
    global c
    global b
    global ans
    c = e.get(1.0, END)
    if(b == 1):
        ans = float(a) % float(c)
        e.delete(1.0, END)
        e.insert(END, ans)
        b = 10
    elif(b == 2):
        ans = float(a) ** float(c)
        e.delete(1.0, END)
        e.insert(END, ans)
        b = 10
    elif(b == 5):
        ans = float(a) / float(c)
        e.delete(1.0, END)
        e.insert(END, ans)
        b = 10
    elif(b == 6):
        ans = float(a) * float(c)
        e.delete(1.0, END)
        e.insert(END, ans)
        b = 10
    elif(b == 7):
        ans = float(a) - float(c)
        e.delete(1.0, END)
        e.insert(END, ans)
        b = 10
    elif(b == 8):
        ans = float(a) + float(c)
        e.delete(1.0, END)
        e.insert(END, ans)
        b = 10
    else:
        e.insert(END, b)


b0 = Button(window, text="%", command=mod)
b0.grid(row=2, column=0)

b1 = Button(window, text="^", command=exp)
b1.grid(row=2, column=1)

b2 = Button(window, text="x^2", command=sq)
b2.grid(row=2, column=2)

b3 = Button(window, text="1/x", command=frac)
b3.grid(row=2, column=3)

b4 = Button(window, text="ANS", command=an)
b4.grid(row=3, column=0)

b5 = Button(window, text="C", command=clear)
b5.grid(row=3, column=1)

b6 = Button(window, text="DEL", command=de)
b6.grid(row=3, column=2)

b7 = Button(window, text="/", command=di)
b7.grid(row=3, column=3)

b8 = Button(window, text="7", command=number7)
b8.grid(row=4, column=0)

b9 = Button(window, text="8", command=number8)
b9.grid(row=4, column=1)


b10 = Button(window, text="9", command=number9)
b10.grid(row=4, column=2)

b11 = Button(window, text="*", command=times)
b11.grid(row=4, column=3)

b12 = Button(window, text="4", command=number4)
b12.grid(row=5, column=0)

b13 = Button(window, text="5", command=number5)
b13.grid(row=5, column=1)

b14 = Button(window, text="6", command=number6)
b14.grid(row=5, column=2)

b15 = Button(window, text="-", command=minus)
b15.grid(row=5, column=3)

b16 = Button(window, text="1", command=number1)
b16.grid(row=6, column=0)

b17 = Button(window, text="2", command=number2)
b17.grid(row=6, column=1)

b18 = Button(window, text="3", command=number3)
b18.grid(row=6, column=2)

b19 = Button(window, text="+", command=plus)
b19.grid(row=6, column=3)

b20 = Button(window, text="+/-", command=neg)
b20.grid(row=7, column=0)

b21 = Button(window, text="0", command=number0)
b21.grid(row=7, column=1)

b22 = Button(window, text=".", command=point)
b22.grid(row=7, column=2)

b23 = Button(window, text="=", command=eq)
b23.grid(row=7, column=3)
window.mainloop()
