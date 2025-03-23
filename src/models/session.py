import hashlib
import json
import time
from src.models.database import Database

class Session:
    def __init__(self, email, password):
        self.email = email
        self._password = password
        self.logged = False
        self.db = Database()

    def hash(self):
        return hashlib.sha256(self._password.encode("utf-8")).hexdigest()

    def exist(self):
        print(f"[exist] Vérifie si {self.email} existe avec hash {self.hash()}")
        res = self.db.execute("SELECT uid FROM users WHERE email = ? AND password = ?", (self.email, self.hash()))
        result = res.fetchone()
        print(f"[exist] Résultat : {result}")
        return result is not None


    def get_uid(self):
        res = self.db.execute("SELECT uid FROM users WHERE email = ? AND password = ?", (self.email, self.hash()))
        row = res.fetchone()
        return row[0] if row else None

    def login(self):
        if self.exist():
            uid = self.get_uid()
            self.db.execute("INSERT INTO logs (uid, action, value) VALUES (?, ?, ?)", (uid, "logged", str(int(time.time()))))
            self.db.commit()
            self.logged = True

    def signin(self):
        print(f"[signin] Tentative de création pour {self.email}")
        if not self.exist():
            print("[signin] Utilisateur non existant, insertion en cours")
            self.db.execute("INSERT INTO users (email, password) VALUES (?, ?)", (self.email, self.hash()))
            self.db.commit()
            return True
        else:
            print("[signin] Utilisateur déjà présent")
            return False


    def persist(self):
        with open("session.json", "w") as f:
            json.dump({"email": self.email}, f)