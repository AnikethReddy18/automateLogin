import customtkinter as ct
from automate import Driver


class MainMenu(ct.CTk):
    def __init__(self):
        super().__init__()

        # Configure Window
        self.title("Web Automator")
        self.geometry("400*200")

        # Web Filler:
        label_form = ct.CTkLabel(self, text="Form Filler: ", font=font)
        self.url_entry = ct.CTkEntry(self, placeholder_text="Enter URL", font=font)
        self.load_time_entry = ct.CTkEntry(self, placeholder_text="Enter loading time", font=font)
        open_filler_button = ct.CTkButton(self, text="Open", font=font, command=self.run_web_filler)

        # Web Filler Display
        label_form.grid(column=0, row=0, padx=5, pady=50)
        self.url_entry.grid(column=1, row=0, padx=10, pady=50)
        self.load_time_entry.grid(column=2, row=0, padx=10, pady=50)
        open_filler_button.grid(column=3, row=0, padx=10, pady=50)

    def run_web_filler(self):
        url = self.url_entry.get()
        load_time = int(self.load_time_entry.get())
        web_filler = WebFiller(url, load_time)
        web_filler.mainloop()


class WebFiller(ct.CTk):
    def __init__(self, url, load_time):
        super().__init__()

        self.to_fill = None
        self.name_form = None
        self.to_select = None
        self.name_selector = None
        self.row = 2
        self.dic_forms = {}
        self.dic_selectors = {}
        self.previous_selection = None
        self.url = url
        self.load_time = load_time

        # Configure Window
        self.title("Automatic Web Filler")
        self.geometry("600x500")

        # Url and load time
        self.url_entry = ct.CTkEntry(self, placeholder_text="URL of the target site", font=font)
        self.load_time_entry = ct.CTkEntry(self, placeholder_text="Time to load(s)", font=font)

        # Selection Label
        select_label = ct.CTkLabel(self, text="Select the form type:  ", font=font)

        # Dropdown
        self.drop = ct.CTkOptionMenu(self, values=["Form", "Dropdown"], font=font, corner_radius=3)

        # Selection Button
        create_button = ct.CTkButton(self, text="Create", font=font, command=self.create_load)

        # Submit All Button
        self.submit_button_all = ct.CTkButton(self, text="Submit All", font=font, command=self.submit)

        # Display

        select_label.grid(column=0, row=1, padx=12)
        self.drop.grid(column=1, row=1, padx=12)
        create_button.grid(column=2, row=1, padx=12)

    def create_form(self):

        self.name_form = ct.CTkEntry(self, placeholder_text="Name of element", font=font)
        self.name_form.grid(column=0, row=self.row, padx=12, pady=20)

        self.to_fill = ct.CTkEntry(self, placeholder_text="Value to fill", font=font)
        self.to_fill.grid(column=1, row=self.row, padx=12, pady=20)

        self.submit_button_all.grid(column=2, row=self.row + 1, pady=12)

        self.row += 1

        self.previous_selection = "form"

    def create_selector(self):

        self.name_selector = ct.CTkEntry(self, placeholder_text="Name of element", font=font)
        self.name_selector.grid(column=0, row=self.row, padx=12, pady=20)

        self.to_select = ct.CTkEntry(self, placeholder_text="Value to Select", font=font)
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
        # url = self.url_entry.get()
        # load_time = int(self.load_time_entry.get())
        driver_instance = Driver(self.url, int(self.load_time))

        for name in self.dic_forms:
            driver_instance.form_fill(name, self.dic_forms[name])

        for name in self.dic_selectors:
            driver_instance.select_dropdown(name, self.dic_selectors[name])


# url = "https://www.instagram.com/"
# instagram_driver = Driver(ul, 3)


font = ("Work Sans", 16)
app = MainMenu()
app.mainloop()
