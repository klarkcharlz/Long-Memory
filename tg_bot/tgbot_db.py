import sqlite3

class Database:
    def __int__(self, db_file):
        #Инициализация базы данных
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    #Наличие пользователя в таблице:
    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' =? ", (user_id,)).fetchmany(1)
            return bool(len(result))

    #Добавление пользователя:
    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))

    #Если пользователь активный
    def set_active(self, user_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'active' = ? WHERE 'user_id' = ?", (active, user_id,))

    #Параметр для рассылки
    def get_user(self):
        with self.connection:
            return self.cursor.execute("SELECT 'user_id', 'active' FROM 'users'").fetchall()