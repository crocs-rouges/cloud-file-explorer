# file_management/files.py

import sqlite3

class FileManager:
    def __init__(self):
        self.conn = sqlite3.connect("cloud_storage.db")

    def add_file(self, folder_id, file_name, file_type, file_data):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Fichier (id_dossier, nom_fichier, type_fichier, fichier_binaire) VALUES (?, ?, ?, ?)",
                       (folder_id, file_name, file_type, file_data))
        self.conn.commit()

    def get_files(self, folder_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id_fichier, nom_fichier, type_fichier FROM Fichier WHERE id_dossier = ?", (folder_id,))
        return cursor.fetchall()
