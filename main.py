import customtkinter as ct

ct.set_default_color_theme("blue")


class Gui(ct.CTk):
    def __init__(self):
        super().__init__()
        self.row = 1

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
        select_button = ct.CTkButton(self, text="Create", font=self.font, command=self.create_form)

        # Display Selection Part
        select_label.grid(column=0, row=0, padx=12)
        self.drop.grid(column=1, row=0, padx=12)
        select_button.grid(column=2, row=0, padx=12)

    def create_form(self):
        if self.drop.get() == "Form":
            name = ct.CTkEntry(self, placeholder_text="Name of element", font=self.font)
            name.grid(column=0, row=self.row, padx=12, pady=20)

            to_fill = ct.CTkEntry(self, placeholder_text="Value to fill", font=self.font)
            to_fill.grid(column=1, row=self.row, padx=12, pady=20)

            submit_button = ct.CTkButton(self, text="Submit", font=self.font)
            submit_button.grid(column=2, row=self.row, padx=12, pady=12)

            self.row += 1

        else:
            pass


app = Gui()
app.mainloop()
