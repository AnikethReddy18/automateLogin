from tkinter import *
import customtkinter as ct

ct.set_default_color_theme("blue")


class Gui(ct.CTk):
    def __init__(self):
        super().__init__()

        # Configure Window
        self.title("Automatic Web Filler")
        self.geometry("500x500")



app = Gui()
app.mainloop()
