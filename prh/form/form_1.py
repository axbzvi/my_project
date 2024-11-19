"""."""

import tkinter


app = tkinter.Tk()

app.geometry('500x500')

entry = tkinter.Entry(app)
entry.grid(column=2, row=2)


app.mainloop()