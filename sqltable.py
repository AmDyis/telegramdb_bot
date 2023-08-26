import sqlite3

class Anime():
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    async def add_anime(self, anime_id):
        with self.connection:
            self.cursor.execute("INSERT INTO anime (anime_id) VALUES (?)", (anime_id,))

    async def anime_exists(self, anime_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM anime WHERE anime_id = ?", (anime_id,)).fetchall()
            return bool(len(result))

    async def add_rating(self, anime_id, rating):
        with self.connection:
            self.cursor.execute("UPDATE anime SET rating = ? WHERE anime_id = ?", (anime_id, rating,))

    # async def get_signup(self, anime_id):
    #     with self.connection:
    #         result = self.cursor.execute("SELECT signup FROM anime WHERE anime_id =?", (anime_id,)).fetchall()
    #         for row in result:
    #             signup = str(row[0])
    #         return signup
    #
    # async def set_signup(self, anime_id, signup):
    #     with self.connection:
    #         return self.cursor.execute("UPDATE anime SET rating = ? WHERE anime_id = ?", (anime_id, signup,))
    async def del_anime(self, anime_id):
        with self.connection:
            self.cursor.execute("DELETE FROM anime WHERE anime_id = ?", (anime_id,))


