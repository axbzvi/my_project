import tkinter as tk



def on_button_click():
    global data, vivod
    data = entry.get()
    vivod = eval(data)
    output_label.config(text=vivod)

app = tk.Tk()
app.title("Пример формы")

entry = tk.Entry(app)
entry.pack(pady=10)

button = tk.Button(app, text="=", command=on_button_click)
button.pack(pady=10)

output_label = tk.Label(app, text="")
output_label.pack(pady=10)


app.mainloop()
