# file_management/folders.py

import sqlite3

class FolderManager:
    def __init__(self):
        self.conn = sqlite3.connect("cloud_storage.db")

    def add_folder(self, user_id, folder_name):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Dossier (id_compte, nom_dossier) VALUES (?, ?)", (user_id, folder_name))
        self.conn.commit()

    def get_folders(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id_dossier, nom_dossier FROM Dossier WHERE id_compte = ?", (user_id,))
        return cursor.fetchall()
