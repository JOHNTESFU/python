first = input("_")
first2 = (first.upper())

if first2 == "RUN":
    print("Program is Running...")

    import tkinter as tk

    WIDTH = 700
    HEIGHT = 400

    def test_function(entry):
        print("this is the entry: ", entry)

    root = tk.Tk()

    root.title("Cheetah Super Car Club")

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    background_image = tk.PhotoImage(file="Capture.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    Frame_one = tk.Frame(root, bg="#80c1ff", bd=3)
    Frame_one.place(relx=0.5, rely=0.02, relwidth=1, relheight=0.1, anchor="n")

    label = tk.Label(Frame_one, text="Cheetah Super Car Club", bg="#80c1ff", fg="black", font=("Times New Roman", 20))
    label.place(relwidth=1, relheight=1)

    Frame_two = tk.Frame(root, bg="#80c1ff", bd=3)
    Frame_two.place(relx=0.5, rely=0.25, relwidth=0.5, relheight=0.5, anchor="n")

    label = tk.Label(Frame_two, text="Welcome\n press Login if already a member\n"
                                     "Press Join if not a member", bg="#80c1ff", fg="white", font=("Times New Roman", 20))
    label.place(relwidth=1, relheight=1)

    Frame_three = tk.Frame(root, bg="#80c1ff", bd=3)
    Frame_three.place(relx=0.5, rely=0.80, relwidth=0.5, relheight=0.08, anchor="n")

    button = tk.Button(Frame_three, text="Login", bg="#80c1ff", font=40 )
    button.place(relx=0, rely=0, relwidth=0.3, relheight=1)
    if button == True:
        print("hi")

    button = tk.Button(Frame_three, text="Join", bg="#80c1ff", font=40 )
    button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

    root.mainloop()


elif first2 == "DEV.DEVELOPER":
    print("Welcome To The Developers Section")


elif first2 == "QUIT":
    print("Program is Closed.")

else:
    print("PLEASE FILL IN A VALID COMMAND.")




'''''

Frame_four = tk.Frame(root, bg="yellow", bd=3)
Frame_four.place(relx=0.5, rely=0.70, relwidth=0.50, relheight=0.08, anchor="n")

import tkinter as tk

HEIGHT=700
WIDTH=600

def test_function(entry):
    print("this is the entry: ", entry)

def get_weather(city):
    weather_key ="saadwqeddwed"
    url = "adfassfas"
    params = {"APPID" : weather_key, "q" :city}



root = tk.Tk()


root.title("Cheetah Super Car Club")

canvas = tk.Canvas(root, height=HEIGHT, width= WIDTH)
canvas.pack()



background_image = tk.PhotoImage(file="Capture.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

Frame_one = tk.Frame(root, bg="#80c1ff", bd=3)
Frame_one.place(relx=0.5, rely=0.1, relwidth=1, relheight=0.1, anchor="n")

Frame_two = tk.Frame(root, bg="#80c1ff", bd=3)
Frame_two.place(relx=0.5, rely=0.25, relwidth=0.5, relheight=0.5, anchor="n")

Frame_three = tk.Frame(root, bg="#80c1ff", bd=3)
Frame_three.place(relx=0.5, rely=0.80, relwidth=0.80, relheight=0.08, anchor="n")

Frame_four = tk.Frame(root, bg="yellow", bd=3)
Frame_four.place(relx=0.5, rely=0.70, relwidth=0.50, relheight=0.08, anchor="n")


label = tk.Label(Frame_one, text="Cheetah Super Car Club", bg ="#80c1ff", fg ="white", font=("Times New Roman", 20))
label.place(relwidth=1, relheight=1)

entry = tk.Entry(Frame_four, bg ="white", font=40)
entry.place(relheight=1, relwidth=0.8)

button = tk.Button(Frame_four, text="Login", bg="white", font=40, command=lambda: test_function(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

button = tk.Button(Frame_three, text="get weather", bg="white", font=40, command=lambda: test_function(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



root.mainloop() '''