import sqlite3
import os


class User:
    def __init__(self):
        if not os.path.exists(path):
            first_con = sqlite3.connect(path)
            first_cur = first_con.cursor()

            first_cur.execute("CREATE TABLE users(username TEXT)")

            first_cur.execute("INSERT INTO users VALUES ('default_user')")

            first_cur.execute(f"CREATE TABLE default_user_form(id TEXT, value TEXT)")
            first_cur.execute(f"CREATE TABLE selector_default_selector(id TEXT, value TEXT)")

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

        self.cursor.execute(f"CREATE TABLE {form_table_name}(id TEXT, value TEXT)")
        self.cursor.execute(f"CREATE TABLE {selector_table_name}(id TEXT, value TEXT)")

        self.connection.commit()


path = "database.db"
