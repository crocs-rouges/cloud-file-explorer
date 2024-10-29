# database/account_db.py

import sqlite3
from encryption.password_manager import PasswordManager

class AccountManager:
    def __init__(self):
        self.conn = sqlite3.connect("cloud_storage.db")
        self.password_manager = PasswordManager()

    def add_account(self, email, password, card_info):
        encrypted_password = self.password_manager.encrypt(password)
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Compte (adresse, mot_de_passe, carte_bancaire) VALUES (?, ?, ?)",
                       (email, encrypted_password, card_info))
        self.conn.commit()

    def login(self, email, password):
        cursor = self.conn.cursor()
        cursor.execute("SELECT mot_de_passe FROM Compte WHERE adresse = ?", (email,))
        record = cursor.fetchone()
        if record and self.password_manager.check_password(record[0], password):
            return True
        return False
