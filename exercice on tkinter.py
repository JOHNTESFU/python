from tkinter import *

def register_user():
    username_info = username.get()
    password_info = password.get()

    ww_file = open("ww1.txt", "a")
    ww_file.write(username_info)
    ww_file.write(password_info)
    ww_file.close()


    username_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(screen1, text = "registration success", fg = "green", font=("Calibri", 11)).pack()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="please entr details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text = "username *").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "password *").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
    print("logi scession started")



def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text = "Notes 1.0", bg = "grey", width = 300, height = 2, font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = 2, width = 30 , command = login).pack()
    Label(text="").pack()
    Button(text = "Register", height = 2, width = 30 , command = register ).pack()
    screen.mainloop()

main_screen()

'''''
import random
import tkinter as tk
Window = tk.Tk()
# Adds a title to the window
Window.title("My App")
#Sizes the window when first appears, measured in pixels.
Window.geometry("400x400")
#functions
def phrase_generator():
    phrases = ["hello, ", "whats up ", "aloha ", "hafa adai "]

    name = str(entry1.get())

    return phrases[random.randint(0, 4)] + name

def phrase_display():
    greeting = phrase_generator()
    greeting_display = tk.Text(master=Window,height=10, width=30)
    greeting_display.grid(column=0, row=3)
    greeting_display.insert(tk.END, greeting)

#Labels
prompt = tk.Label(text="welcome to my app", font=("Times New Roman", 20))
prompt.grid(column=0, row=0)
prompt1= tk.Label(text="what is ur name?", font=("Verdana bold italic", 15))
prompt1.grid(column=0, row=1)
#Entry Fields
entry1 = tk.Entry()
entry1.grid(column=1, row=1)
#Buttons
button1 = tk.Button(text="click me!", command=phrase_display)
button1.grid(column=0, row=2)



Window.mainloop()

#Text fields
text_field = tk.Text(master=Window, height=10, width=30)
text_field.grid()
#makes frame appear on the screen '''
