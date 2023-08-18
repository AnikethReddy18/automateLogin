import customtkinter as ct

ct.set_default_color_theme("blue")
#

class Gui(ct.CTk):
    def __init__(self):
        super().__init__()
        self.to_fill = None
        self.name_form = None
        self.to_select = None
        self.name_selector = None
        self.row = 2
        self.dic_forms = {}
        self.dic_selectors = {}
        self.previous_selection = None

        # Configure Window
        self.title("Automatic Web Filler")
        self.geometry("625x500")

        # Font
        self.font = ("Work Sans", 16)

        # Selection Label
        select_label = ct.CTkLabel(self, text="Select the form type:  ", font=self.font)
        warning_label = ct.CTkLabel(self, text="Only click create after filling the values", font=self.font)

        # Dropdown
        self.drop = ct.CTkOptionMenu(self, values=["Form", "Dropdown"], font=self.font, corner_radius=3)

        # Selection Button
        create_button = ct.CTkButton(self, text="Create", font=self.font, command=self.create_load)

        # Submit All Button
        self.submit_button_all = ct.CTkButton(self, text="Submit All", font=self.font, command=self.submit)

        # Display Selection Part
        select_label.grid(column=0, row=1, padx=12)
        warning_label.grid(column=1, row=0, sticky="n")
        self.drop.grid(column=1, row=1, padx=12)
        create_button.grid(column=2, row=1, padx=12)

    def create_form(self):

        self.name_form = ct.CTkEntry(self, placeholder_text="Name of element", font=self.font)
        self.name_form.grid(column=0, row=self.row, padx=12, pady=20)

        self.to_fill = ct.CTkEntry(self, placeholder_text="Value to fill", font=self.font)
        self.to_fill.grid(column=1, row=self.row, padx=12, pady=20)

        self.submit_button_all.grid(column=2, row=self.row + 1, pady=12)

        self.row += 1

        self.previous_selection = "form"

    def create_selector(self):

        self.name_selector = ct.CTkEntry(self, placeholder_text="Name of element", font=self.font)
        self.name_selector.grid(column=0, row=self.row, padx=12, pady=20)

        self.to_select = ct.CTkEntry(self, placeholder_text="Value to Select", font=self.font)
        self.to_select.grid(column=1, row=self.row, padx=12, pady=20)

        self.submit_button_all.grid(column=2, row=self.row + 1, pady=12)

        self.row += 1

        self.previous_selection = "dropdown"

    def load(self):

        if self.previous_selection == "form":
            self.dic_forms[self.name_form.get()] = self.to_fill.get()
        else:
            self.dic_selectors[self.name_selector.get()] = self.to_select.get()

    def create_load(self):

        state = self.drop.get()
        if not self.previous_selection:
            if state == "Form":
                self.create_form()
            else:
                self.create_selector()

        else:
            self.load()
            if state == "Form":
                self.create_form()
            else:
                self.create_selector()

    def submit(self):
        self.load()
        print(f"Forms: {self.dic_forms}\nSelectors={self.dic_selectors}")


app = Gui()
app.mainloop()
