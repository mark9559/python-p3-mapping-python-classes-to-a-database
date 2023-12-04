from config import CONN, CURSOR

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        with CONN:
            CONN.execute(sql)

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        with CONN:
            CONN.execute(sql, (self.name, self.album))
            self.id = CONN.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]
    
    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song

