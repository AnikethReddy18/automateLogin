import sqlite3
import os


class User:
    def __init__(self):
        if not os.path.exists(path):
            first_con = sqlite3.connect(path)
            first_cur = first_con.cursor()

            first_cur.execute("CREATE TABLE users(username text)")

            first_cur.execute("INSERT INTO users VALUES ('default_user')")
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


path = "database.db"
