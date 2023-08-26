import sqlite3
import os


class User:
    def __init__(self):
        if not os.path.exists(path):
            first_con = sqlite3.connect(path)
            first_cur = first_con.cursor()

            first_cur.execute("CREATE TABLE users(username TEXT)")

            first_cur.execute("INSERT INTO users VALUES ('default_user')")

            first_cur.execute(f"CREATE TABLE default_user_form(name TEXT, value TEXT)")
            first_cur.execute(f"CREATE TABLE selector_user_selector(name TEXT, value TEXT)")

            first_cur.close()
            first_con.commit()

        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()

    def create_user(self, username):
        self.cursor.execute("INSERT INTO users VALUES (?)", (username,))
        self.connection.commit()

    def get_users(self):
        data = self.cursor.execute("SELECT username FROM users").fetchall()

        users = []
        for column in data:
            for user in column:
                users.append(user)

        return users

    def gen_user_tables(self, username):
        form_table_name = f"{username}_form"
        selector_table_name = f"{username}_selector"

        self.cursor.execute(f"CREATE TABLE {form_table_name}(name TEXT, value TEXT)")
        self.cursor.execute(f"CREATE TABLE {selector_table_name}(name TEXT, value TEXT)")

        self.connection.commit()

    def get_no(self, username):
        form_fetch = self.cursor.execute(f"SELECT name FROM {username}_form").fetchall()
        selector_fetch = self.cursor.execute(f"SELECT name FROM {username}_selector").fetchall()
        no_forms = len(form_fetch)
        no_selectors = len(selector_fetch)
        self.connection.commit()

        return no_forms, no_selectors

    def save_forms(self, forms, username):
        print(forms)
        for id_value in forms:
            self.connection.execute(f"INSERT INTO {username}_form (name, value) VALUES (?,?)", id_value)
        self.connection.commit()

    def save_selectors(self, selectors, username):
        for id_value in selectors:
            self.connection.execute(f"INSERT INTO {username}_selector (name, value) VALUES (?,?)", id_value)
        self.connection.commit()

    def get_forms(self, username):
        table_name = f"{username}_form"
        forms_dict = {}

        forms = self.connection.execute(f"SELECT name, value FROM {table_name}").fetchall()

        for key, value in forms:
            forms_dict[key] = value

        return forms_dict

    def get_selectors(self, username):
        table_name = f"{username}_selector"
        selectors_dict = {}

        selectors = self.connection.execute(f"SELECT name, value FROM {table_name}").fetchall()

        for key, value in selectors:
            selectors_dict[key] = value

        return selectors_dict


path = "database.db"
