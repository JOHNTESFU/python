
from tkinter import *
import random
import time

tk = Tk()
tk.title("Bounce!")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)

canvas.pack()

tk.update()


class Ball:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

    def draw(self):
        pass


ball = Ball(canvas,"red")














'''''




















*************************************************************************


from tkinter import*
import time
root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()




canvas.create_polygon(10,10,10,60,50,35)

for i in range(0, 60):
    canvas.move(1, 5, 0)
    root.update()
    time.sleep(0.1)



*************************************************************************


canvas.create_text(150,150, text="hello there", fill= "blue", font="Calibri 30")

canvas.create_arc(10, 10, 200, 80, extent=45, style=ARC)

canvas.create_arc(10, 80, 200, 160, extent=90, style=ARC)


*************************************************************************


def randomRects(num):
    for i in range(0,num):
        x1 = random.randrange(150)
        y1 = random.randrange(150)
        x2 = x1 + random.randrange(150)
        y2 = y1 + random.randrange(150)
        canvas.create_rectangle(x1, y1, x2, y2)


randomRects(150)


*************************************************************************


canvas = Canvas(root, width=300, height=300)
canvas.pack()

def createRect(x1,y1,x2,y2):
    canvas.create_rectangle(x1, y1, x2, y2,fill="blue")


createRect(5,50,200,70)

createRect(5,5,40,200)


*************************************************************************


canvas.create_rectangle(20,20,100,270)

canvas.create_line(0,0,300,300)

canvas.create_polygon(0, 0, 5, 20, 50, 30, 40, 15)


*************************************************************************


equa = ""

equation = StringVar()

calculation = Label(root, textvariable=equation)

equation.set("enter your equation")

calculation.grid(columnspan=4)

def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)
def EqualPress():
    global equa
    total = str(eval(equa))
    equation.set(total)
    equa = ""

def clear():
    global equa
    equa=""
    equation.set("")


Button1 = Button(root, text="1", command=lambda: btnPress(1))
Button1.grid(row=1, column=0)

Button2 = Button(root, text="2", command=lambda: btnPress(2))
Button2.grid(row=1, column=1)

Button3 = Button(root, text="3", command=lambda: btnPress(3))
Button3.grid(row=1, column=2)

plus = Button(root, text="+", command=lambda: btnPress("+"))
plus.grid(row=1, column=3)

Button4 = Button(root, text="4", command=lambda: btnPress(4))
Button4.grid(row=2, column=0)

Button5 = Button(root, text="5", command=lambda: btnPress(5))
Button5.grid(row=2, column=1)

Button6 = Button(root, text="6", command=lambda: btnPress(6))
Button6.grid(row=2, column=2)

minus = Button(root, text="-", command=lambda: btnPress("-"))
minus.grid(row=2, column=3)

Button7 = Button(root, text="7", command=lambda: btnPress(7))
Button7.grid(row=3, column=0)

Button8 = Button(root, text="8", command=lambda: btnPress(8))
Button8.grid(row=3, column=1)

Button9 = Button(root, text="9", command=lambda: btnPress(9))
Button9.grid(row=3, column=2)

multiply = Button(root, text="*", command=lambda: btnPress("*"))
multiply.grid(row=3, column=3)

clear = Button(root, text="C", command=clear)
clear.grid(row=4, column=0)

Button0 = Button(root, text="0", command=lambda: btnPress(0))
Button0.grid(row=4, column=1)

equal = Button(root, text="=",command = EqualPress)
equal.grid(row=4, column=2)

divide = Button(root, text="/", command=lambda: btnPress("/"))
divide.grid(row=4, column=3)


*************************************************************************


def random():
    print("this is a statement")
mainMenu = Menu(root)

root.configure(menu = mainMenu)
subMenu = Menu(mainMenu)

mainMenu.add_cascade(label="File", menu=subMenu)

subMenu.add_command(label="random func", command=random)

subMenu.add_command(label="new file", command =random)

subMenu.add_separator()

subMenu.add_command(label="Supercalafragilistic", command=random)


*************************************************************************


import tkinter.messagebox
root = Tk()

tkinter.messagebox.showinfo("Window title","did you know that the world just blew up!")

answer =  tkinter.messagebox.askquestion("Question 1","Are you human?")

if answer == 'yes':
    tkinter.messagebox.showinfo("congrats", "Thank God its good")
elif answer == 'no':
    tkinter.messagebox.showinfo("alien",'alien')


*************************************************************************


label1 = Label(root, text="enter your expression:")
label1.pack()


def evaluate(event):
    data = e.get()
    ans.configure(text="Answer:" + str(eval(data)))


e = Entry(root)

e.bind("<Enter>", evaluate)
e.pack()

ans = Label(root)
ans.pack()


*************************************************************************


def leftClick(event):
    print("Left")
def rightClick(event):
    print("right")
def scroll(event):
    print("scroll")
def leftKey(event):
    print("left key pressed")
def rightKey(event):
    print("right key pressed")


root.geometry("500x500")

root.bind("<Button-1>",leftClick)
root.bind("<Button-2>",rightClick)
root.bind("<Button-3>",scroll)
root.bind("<Left>",leftKey)
root.bind("<Right>",rightKey)


*************************************************************************


def printName():
    print("Hello there John")


button1 = Button(root, text="Click Me!", command=printName)
button1.pack()


label1 = Label(root,text="label 1")

label2 = Label(root,text="label 2")

label3 = Label(root,text="label 3")

label1.grid(row=0, column=0)
label2.grid(row=1, column=1)
label3.grid(row=1, column=0)


Button1 = Button(None, text = "click me!", fg = "Blue")
Button1.pack()

Button2 = Button(None, text = "whoaa!", fg = "red")
Button2.pack(fill=X)


Button3 = Button(None, text = "whats up!", fg = "Purple")
Button3.pack(side=RIGHT, fill=Y)

Button4 = Button(None, text = "hello", fg = "Yellow")
Button4.pack()                 
 
 
label1 = Label(root,text="Name:")
label1.grid(row=0, column=0, sticky="E")

label2 = Label(root, text="Password:")
label2.grid(row=1, column=0, sticky="E")

entrySpace = Entry(root)
entrySpace.grid(row=0,column=1)

entrySpace2 = Entry(root)
entrySpace2.grid(row=1,column=1)

cbutton = Checkbutton(root,text = "remember Password")
cbutton.grid(columnspan=2)
 
 
*************************************************************************
 
 
 '''''
