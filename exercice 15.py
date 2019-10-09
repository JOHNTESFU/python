import tkinter as tk

window = tk.Tk()

window.title("My app")

window.geometry("1000x350")

prompt = tk.Label(text="this is cs50.", font=("Times New Roman", 20))
prompt.grid()


#label
entry_field = tk.Entry()
entry_field.grid()

#button
button1 = tk.Button(text="click me!", bg="red")
button1.grid()

#entry_field
text_field = tk.Text(master=window, height=10, width=30)
text_field.grid()

window.mainloop()


