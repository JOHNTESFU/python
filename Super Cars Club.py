import tkinter as tk

def test_function(entry):
    print("this is the entry: ", entry)

def get_weather(city):
    weather_key ="saadwqeddwed"
    url = "adfassfas"
    params = {"APPID" : weather_key, "q" :city}

root = tk.Tk()

root.title("Cheetah Super Car Club")

canvas = tk.Canvas(root, height="700", width= "600")
canvas.pack()

background_image = tk.PhotoImage(file="Capture.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#80c1ff",bd=3)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

label = tk.Label(frame,text="Cheetah Super Car Club", bg = "#80c1ff", fg = "blue",font=("Times New Roman", 20))
label.place(relwidth=1, relheight=1)

button = tk.Button(frame, text="get weather", bg="grey", font=40, command=lambda: test_function(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


root.mainloop()
'''''
lower_frame = tk.Frame(root, bg="#80c1ff",bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lower_frame, text="this is a label", bg= "white")
label.place(relwidth=1, relheight=1)

logo_frame = tk.Frame(root, bg="#80c1ff",)
logo_frame.place(relx=0.1, rely=0.1, relwidth=0.4, relheight=0.1)
'''



