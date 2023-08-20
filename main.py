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
        self.input_selectors = ct.CTkEntry(self, placeholder_text="No of forms", font=font)
        self.input_forms = ct.CTkEntry(self, placeholder_text="No of dropdowns", font=font)

        # Web Filler Display
        label_form.grid(column=0, row=0, padx=5)
        self.url_entry.grid(column=1, row=0, padx=10)
        self.load_time_entry.grid(column=2, row=0, padx=10)
        open_filler_button.grid(column=3, row=0, padx=10, rowspan=2, ipady=15)
        self.input_forms.grid(column=1, row=1, padx=10, pady=10)
        self.input_selectors.grid(column=2, row=1, padx=10, pady=10)

    def run_web_filler(self):
        url = self.url_entry.get()
        load_time = int(self.load_time_entry.get())
        no_forms = int(self.input_forms.get())
        no_selectors = int(self.input_selectors.get())

        web_filler = WebFiller(url, load_time, no_forms, no_selectors)
        web_filler.mainloop()


class WebFiller(ct.CTk):
    def __init__(self, url, load_time, no_forms, no_selectors):
        super().__init__()

        self.name_selector = None
        self.row_form = 1
        self.row_selector = 1
        self.previous_selection = None
        self.url = url
        self.load_time = load_time
        self.no_forms = no_forms
        self.no_selectors = no_selectors
        self.dic_forms = {}
        self.dic_selectors = {}

        self.form_entry_names = []
        self.form_entry_values = []

        self.selector_entry_names = []
        self.selector_entry_values = []

        # Configure Window
        self.title("Automatic Web Filler")
        self.geometry("1000x500")

        # Titles
        form_label = ct.CTkLabel(self, text="Forms", font=("Work Sans", 50))
        selector_label = ct.CTkLabel(self, text="Dropdowns", font=("Work Sans", 50))

        # Display Titles
        form_label.grid(column=0, row=0, padx=50, pady=30)
        selector_label.grid(column=2, row=0, padx=50, pady=30)

        # Make Form Entries
        for entry in range(self.no_forms):
            self.form_entry_name = ct.CTkEntry(self)
            self.form_entry_name.grid(column=0, row=self.row_form, pady=10, padx=10)
            self.form_entry_value = ct.CTkEntry(self)
            self.form_entry_value.grid(column=1, row=self.row_form, pady=10, padx=10)

            self.form_entry_names.append(self.form_entry_name)
            self.form_entry_values.append(self.form_entry_value)

            self.row_form += 1

        # Make Selector Entries
        for entry in range(self.no_selectors):
            self.selector_entry_name = ct.CTkEntry(self)
            self.selector_entry_name.grid(column=2, row=self.row_selector, pady=10, padx=10)
            self.selector_entry_value = ct.CTkEntry(self)
            self.selector_entry_value.grid(column=3, row=self.row_selector, pady=10, padx=10)

            self.selector_entry_names.append(self.selector_entry_name)
            self.selector_entry_values.append(self.selector_entry_value)

            self.row_selector += 1

        # Submit Button
        submit_button = ct.CTkButton(self, text="Submit", font=("Work Sans", 40), command=self.submit)
        if self.row_form > self.row_selector:
            submit_button.grid(column=0, row=self.row_form + 1, columnspan=4, pady=20, ipadx=400,
                               ipady=25)
        else:
            submit_button.grid(column=0, row=self.row_selector + 1, columnspan=4, pady=20, ipadx=400,
                               ipady=25)

    def load(self):
        for entry_index in range(self.no_forms):
            form_entry_name = self.form_entry_names[entry_index].get()
            form_entry_value = self.form_entry_values[entry_index].get()
            self.dic_forms[form_entry_name] = form_entry_value

        for entry_index in range(self.no_selectors):
            selector_entry_name = self.selector_entry_names[entry_index].get()
            selector_entry_value = self.selector_entry_values[entry_index].get()
            self.dic_selectors[selector_entry_name] = selector_entry_value

    def submit(self):
        self.load()

        forms = self.dic_forms
        selectors = self.dic_selectors

        driver = Driver(self.url, self.load_time)

        for name in forms:
            driver.form_fill(name, forms[name])

        for name in selectors:
            driver.select_dropdown(name, selectors[name])


font = ("Work Sans", 16)
app = MainMenu()
app.mainloop()
