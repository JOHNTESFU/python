import tkinter as tk

HEIGHT=500
WIDTH=600

def test_function(entry):
    print("this is the entry: ", entry)

def get_weather(city):
    weather_key ="saadwqeddwed"
    url = "adfassfas"
    params = {"APPID" : weather_key, "q" :city}



root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width= WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="Capturedsada.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#80c1ff",bd=3)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, bg ="white", font=40)
entry.place(relheight=1, relwidth=0.65)

button = tk.Button(frame, text="get weather", bg="grey", font=40, command=lambda: test_function(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#80c1ff",bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lower_frame, text="this is a label", bg= "white")
label.place(relwidth=1, relheight=1)


root.mainloop()


'''''
label = tk.Label(frame, text="this is a label", bg= "white")
label.place(relx=0.3, rely=0, relwidth=0.45, relheight=0.25)'''


print(weather["name"])
print(weather["weather"][0]["description"])
print(weather["main"]["temp"])
