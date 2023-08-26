import customtkinter as ct
from automate import Driver
from tkinter import simpledialog
from Database import User


class Login(ct.CTk):
    def __init__(self):
        super().__init__()
        self.user = User()
        self.users = self.user.get_users()

        # Configure Window
        self.title("Select User")
        # self.geometry("100x100")
        self.eval('tk::PlaceWindow . center')

        # UI

        select_label = ct.CTkLabel(self, text="Select User:", font=font)
        self.user_dropdown = ct.CTkOptionMenu(self, values=self.users, font=font, command=self.open_menu)
        new_user_button = ct.CTkButton(self, text="New User", font=font, command=self.new_user)

        # Display UI
        select_label.grid(column=0, row=0, padx=5, pady=5)
        self.user_dropdown.grid(column=1, row=0, padx=5, pady=5)
        new_user_button.grid(column=0, row=1, padx=5, pady=5, columnspan=2, ipadx=40)

    def new_user(self):
        new_username = simpledialog.askstring("New User", "What is do you want as your username?")
        self.user.create_user(new_username)
        self.user_dropdown.grid_forget()
        self.user.gen_user_tables(new_username)
        self.users = self.user.get_users()
        self.user_dropdown = ct.CTkOptionMenu(self, values=self.users, font=font, command=self.open_menu)
        self.user_dropdown.grid(column=1, row=0, padx=5, pady=5)

    def open_menu(self, username):
        main_menu = MainMenu(username, self.user)
        main_menu.mainloop()


class MainMenu(ct.CTk):
    def __init__(self, username, user):
        super().__init__()
        self.username = username
        self.load_time = 3
        self.user = user

        # Configure Window
        self.title("Web Automator")
        self.geometry("650x125")
        self.eval('tk::PlaceWindow . center')

        # Web Filler:
        label_form = ct.CTkLabel(self, text="Form Filler: ", font=font)
        self.url_entry = ct.CTkEntry(self, placeholder_text="Enter URL", font=font)
        open_filler_button = ct.CTkButton(self, text="Open", font=font, command=lambda: self.run_web_filler(True))
        self.input_selectors = ct.CTkEntry(self, placeholder_text="No of forms", font=font)
        self.input_forms = ct.CTkEntry(self, placeholder_text="No of dropdowns", font=font)

        # Web Filler Display
        label_form.grid(column=0, row=0, padx=5)
        self.url_entry.grid(column=1, row=0, padx=10)
        open_filler_button.grid(column=3, row=0, padx=10, rowspan=2, ipady=15)
        self.input_forms.grid(column=1, row=1, padx=10, pady=10)
        self.input_selectors.grid(column=2, row=1, padx=10, pady=10)

        # Load Previous Data
        label_prev_data = ct.CTkLabel(self, text="Load Previous Filler: ", font=font)
        button_prev_data = ct.CTkButton(self, text="Load", font=font, command=lambda: self.run_web_filler(False))
        self.prev_url_entry = ct.CTkEntry(self, placeholder_text="Enter URL", font=font)

        # Display Previous Data
        label_prev_data.grid(column=0, row=2, padx=5, pady=10)
        button_prev_data.grid(column=2, row=2, padx=10, pady=10)
        self.prev_url_entry.grid(column=1, row=2, pady=5)

    def run_web_filler(self, is_new):
        if is_new:
            url = self.url_entry.get()
            no_forms = int(self.input_forms.get())
            no_selectors = int(self.input_selectors.get())

            web_filler = WebFiller(url, self.load_time, no_forms, no_selectors, self.user, self.username, False)
            web_filler.mainloop()

        else:
            url = self.prev_url_entry.get()
            no_forms, no_selectors = self.user.get_no(self.username)

            web_filler = WebFiller(url, self.load_time, no_forms, no_selectors, self.user, self.username, True)
            web_filler.mainloop()


class WebFiller(ct.CTk):
    def __init__(self, url, load_time, no_forms, no_selectors, user, username, is_prev):
        super().__init__()
        self.is_prev = is_prev
        self.form_entry_value = None
        self.form_entry_name = None
        self.selector_entry_value = None
        self.selector_entry_name = None
        self.selectors_dict_prev = None
        self.forms_dict_prev = None
        self.user = user
        self.username = username

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
        self.geometry("765x500")
        self.eval('tk::PlaceWindow . center')
        self.resizable(height=True, width=True)

        # Titles
        form_label = ct.CTkLabel(self, text="Forms", font=("Work Sans", 50))
        selector_label = ct.CTkLabel(self, text="Dropdowns", font=("Work Sans", 50))

        # Display Titles
        form_label.grid(column=0, row=0, padx=100, pady=30, columnspan=2)
        selector_label.grid(column=2, row=0, padx=100, pady=30, columnspan=2)

        if self.is_prev:
            self.load_prev_data()
            self.make_entries()

        else:
            self.make_entries()

        # Save, Submit Buttons
        submit_button = ct.CTkButton(self, text="Submit", font=("Work Sans", 40), command=self.submit)
        save_button = ct.CTkButton(self, text="Save", font=("Work Sans", 25), command=self.save)
        save_submit_button = ct.CTkButton(self, text="Save & Submit", font=("Work Sans", 25), command=self.save_submit)

        if self.row_form > self.row_selector:
            submit_button.grid(column=0, row=self.row_form + 1, columnspan=4, pady=12, ipadx=300, ipady=25)
            save_button.grid(column=0, row=self.row_form + 2, columnspan=2, pady=5, ipadx=50)
            save_submit_button.grid(column=2, row=self.row_form + 2, columnspan=2, pady=5, ipadx=50)
        else:
            submit_button.grid(column=0, row=self.row_selector + 1, columnspan=4, pady=12, ipadx=300,
                               ipady=25)
            save_button.grid(column=0, row=self.row_selector + 2, columnspan=2, pady=5, ipadx=50)
            save_submit_button.grid(column=2, row=self.row_selector + 2, columnspan=2, pady=5, ipadx=50)

    def load(self):
        for entry_index in range(self.no_forms):
            form_entry_name = self.form_entry_names[entry_index].get()
            form_entry_value = self.form_entry_values[entry_index].get()
            self.dic_forms[form_entry_name] = form_entry_value

        for entry_index in range(self.no_selectors):
            selector_entry_name = self.selector_entry_names[entry_index].get()
            selector_entry_value = self.selector_entry_values[entry_index].get()
            self.dic_selectors[selector_entry_name] = selector_entry_value

    def make_entries(self):
        is_prev = self.is_prev

        # Make Selector Entries
        if is_prev:
            for name in self.forms_dict_prev:
                self.form_entry_name = ct.CTkEntry(self)
                self.form_entry_name.grid(column=0, row=self.row_form, pady=10, padx=5)
                self.form_entry_name.insert(0, name)

                self.form_entry_value = ct.CTkEntry(self)
                self.form_entry_value.grid(column=1, row=self.row_form, pady=10, padx=5)
                self.form_entry_value.insert(0, self.forms_dict_prev[name])

                self.row_form += 1

            for name in self.selectors_dict_prev:
                self.selector_entry_name = ct.CTkEntry(self)
                self.selector_entry_name.grid(column=2, row=self.row_selector, pady=10)
                self.selector_entry_name.insert(0, name)

                self.selector_entry_value = ct.CTkEntry(self)
                self.selector_entry_value.grid(column=3, row=self.row_selector, pady=10)
                self.selector_entry_value.insert(0, self.selectors_dict_prev[name])

                self.row_selector += 1

        else:
            # Make Form Entries
            for entry in range(self.no_forms):
                self.form_entry_name = ct.CTkEntry(self)
                self.form_entry_name.grid(column=0, row=self.row_form, pady=10, padx=5)
                self.form_entry_value = ct.CTkEntry(self)
                self.form_entry_value.grid(column=1, row=self.row_form, pady=10, padx=5)

                self.form_entry_names.append(self.form_entry_name)
                self.form_entry_values.append(self.form_entry_value)

                self.row_form += 1

            for entry in range(self.no_selectors):
                self.selector_entry_name = ct.CTkEntry(self)
                self.selector_entry_name.grid(column=2, row=self.row_selector, pady=10)
                self.selector_entry_value = ct.CTkEntry(self)
                self.selector_entry_value.grid(column=3, row=self.row_selector, pady=10)

                self.selector_entry_names.append(self.selector_entry_name)
                self.selector_entry_values.append(self.selector_entry_value)

                self.row_selector += 1

    def submit(self, is_prev):
        self.load()

        # if is_prev:
        #     forms = self.
        #
        #     pass
        forms = self.dic_forms
        selectors = self.dic_selectors

        driver = Driver(self.url, self.load_time)

        for name in forms:
            driver.form_fill(name, forms[name])

        for name in selectors:
            driver.select_dropdown(name, selectors[name])

    def save(self):
        self.load()
        forms = []
        for id_ in self.dic_forms:
            forms.append((id_, self.dic_forms[id_]))

        selectors = []
        for id_ in self.dic_selectors:
            selectors.append((id_, self.dic_selectors[id_]))

        self.user.save_forms(forms, self.username)
        self.user.save_selectors(selectors, self.username)

    def save_submit(self):
        self.save()
        self.submit()

    def load_prev_data(self):
        self.forms_dict_prev = self.user.get_forms(self.username)
        self.selectors_dict_prev = self.user.get_selectors(self.username)


font = ("Work Sans", 16)
app = Login()
app.mainloop()
