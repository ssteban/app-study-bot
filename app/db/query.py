from app.db.init import Database
import bcrypt


class user_query:
    def __init__(self):
        self.db = Database()

    def login(self, email, password_plain):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT contraseña FROM users WHERE email = %s", (email,))
        row = cursor.fetchone()
        if row is None:
            return False
        password_db = row[0]
        # password_db puede ser string o bytes según el driver
        if isinstance(password_db, str):
            password_db = password_db.encode('utf-8')
        return bcrypt.checkpw(password_plain.encode('utf-8'), password_db)

    def register(self, username, email, tipo_usuario, password_hash):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (usuario, email, tipo, contraseña) VALUES (%s, %s, %s, %s)",
            (username, email, tipo_usuario, password_hash.decode('utf-8'))
        )
        conn.commit()
        return cursor.rowcount > 0

    def close(self):
        self.db.close()