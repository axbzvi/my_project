import tkinter as tk
from PIL import Image, ImageTk
import math


class Inter:
    def __init__(self, root):
        self.root = root
        self.root.title("Движущийся текст скидки")

        image_path = "etap_6/logo.png"
        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)

        self.canvas = tk.Canvas(root, width=self.photo.width(), height=self.photo.height())
        self.canvas.pack()

        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        self.text = "Скидка 50%"
        self.font_size = 24
        self.angle = 0
        self.radius = 100 
        self.center_x = self.photo.width() // 2 
        self.center_y = self.photo.height() // 2

        self.text_id = self.canvas.create_text(self.center_x, self.center_y, text=self.text, fill="red", font=("Helvetica", self.font_size))

        self.animate_text()

    def animate_text(self):
        x = self.center_x + self.radius * math.cos(math.radians(self.angle))
        y = self.center_y + self.radius * math.sin(math.radians(self.angle))

        self.canvas.coords(self.text_id, x, y)

        self.angle = (self.angle + 5) % 360

        self.root.after(50, self.animate_text)

root = tk.Tk()
app = Inter(root)

root.mainloop()