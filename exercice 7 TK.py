first = input("_")
first2 = (first.upper())

if first2 == "RUN":
    print("Program is Running...")

    import tkinter as tk

    WIDTH = 700
    HEIGHT = 400


    def join():
        print("join")




    def user():
        print("user")




    def exit():
        print("exit")
    def test_function(entry):
        print("this is the entry: ", entry)

    root = tk.Tk()

    root.title("Cheetah Super Car Club")

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()


    Frame_one = tk.Frame(root, bg="black", bd=3)
    Frame_one.place(relx=0.5, rely=0.02, relwidth=1, relheight=0.1, anchor="n")

    label = tk.Label(Frame_one, text="Cheetah Super Car Club", bg="#80c1ff", fg="black", font=("Times New Roman", 20))
    label.place(relwidth=1, relheight=1)

    Frame_two = tk.Frame(root, bg="#80c1ff", bd=3)
    Frame_two.place(relx=0.5, rely=0.25, relwidth=0.5, relheight=0.5, anchor="n")

    label = tk.Label(Frame_two, text="Press 'Join' if u want to join our club, \nPress 'user' if you have joined "
              "and \n'Exit' if you want to leave.", bg="black", fg="white", font=("Times New Roman", 15))
    label.place(relwidth=1, relheight=1)

    Frame_three = tk.Frame(root, bg="#80c1ff", bd=3)
    Frame_three.place(relx=0.5, rely=0.80, relwidth=0.5, relheight=0.08, anchor="n")

    button = tk.Button(Frame_three, text="User", bg="#80c1ff", font=40, command = user )
    button.place(relx=0, rely=0, relwidth=0.3, relheight=1)

    button = tk.Button(Frame_three, text="Exit", bg="#80c1ff", font=40, command = join)
    button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

    button = tk.Button(Frame_three, text="Join", bg="#80c1ff", font=40, command = exit)
    button.place(relx=0.35, rely=0, relwidth=0.3, relheight=1)

    root.mainloop()


elif first2 == "DEV.DEVELOPER":
    print("Welcome To The Developers Section")


elif first2 == "QUIT":
    print("Program is Closed.")

else:
    print("PLEASE FILL IN A VALID COMMAND.")


