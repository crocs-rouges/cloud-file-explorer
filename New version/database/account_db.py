# database/account_db.py

import sqlite3
from encryption.password_manager import PasswordManager

class AccountManager:
    def __init__(self):
        self.conn = sqlite3.connect("cloud_storage.db")
        self.password_manager = PasswordManager()

    def add_account(self, prenom, nom, email, password):
        encrypted_password = self.password_manager.encrypt(password)
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Compte (email, nom, prenom, password ) VALUES (?, ?, ?, ?)",
                       (email, nom, prenom, encrypted_password))
        self.conn.commit()

    def login(self, email, password):
        cursor = self.conn.cursor()
        cursor.execute("SELECT password FROM Compte WHERE email = ?", (email,))
        record = cursor.fetchone()
        print(record)
        if record and self.password_manager.check_password(record[0], password):
            return True
        return False
    
    # Dans account_db.py


    def get_user_id(self, email):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT id_compte FROM Compte WHERE email = ?", (email,))
            result = cursor.fetchone()  # Récupère le premier résultat
            return result[0] if result else None  # Retourne uniquement l'ID
        except Exception as e:
            print(f"Erreur lors de la récupération de l'ID utilisateur : {e}")
            return None

