import customtkinter as ct

ct.set_default_color_theme("blue")


class Gui(ct.CTk):
    def __init__(self):
        super().__init__()
        self.to_fill = None
        self.name = None
        self.row = 1
        self.dic = {}

        # Configure Window
        self.title("Automatic Web Filler")
        self.geometry("500x500")

        # Font
        self.font = ("Work Sans", 16)

        # Selection Part

        # Selection Label
        select_label = ct.CTkLabel(self, text="Select the form type:  ", font=self.font)

        # Dropdown
        self.drop = ct.CTkOptionMenu(self, values=["Form", "Dropdown"], font=self.font, corner_radius=3)

        # Selection Button
        create_button = ct.CTkButton(self, text="Create", font=self.font, command=self.create_load_form)

        # Submit All Button
        self.submit_button_all = ct.CTkButton(self, text="Submit All", font=self.font, command=self.submit)

        # Display Selection Part
        select_label.grid(column=0, row=0, padx=12)
        self.drop.grid(column=1, row=0, padx=12)
        create_button.grid(column=2, row=0, padx=12)

    def create_form(self):
        if self.drop.get() == "Form":

            self.name = ct.CTkEntry(self, placeholder_text="Name of element", font=self.font)
            self.name.grid(column=0, row=self.row, padx=12, pady=20)

            self.to_fill = ct.CTkEntry(self, placeholder_text="Value to fill", font=self.font)
            self.to_fill.grid(column=1, row=self.row, padx=12, pady=20)

            self.submit_button_all.grid(column=2, row=self.row + 1, pady=12)

            self.row += 1

        else:
            pass

    def load(self):
        self.dic[self.name.get()] = self.to_fill.get()

    def create_load_form(self):
        if self.name is None:
            self.create_form()

        else:
            self.load()
            self.create_form()

    def submit(self):
        self.load()
        print(self.dic)


app = Gui()
app.mainloop()
