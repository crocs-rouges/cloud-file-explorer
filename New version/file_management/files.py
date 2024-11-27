# file_management/files.py

import sqlite3
from PIL import Image, ImageTk
from tkinter import filedialog
import io

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

    def add_file_to_db(self, file_path, file_name, file_type, id_folder):
        with sqlite3.connect('cloud_storage.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO Fichier (id_dossier, nom_fichier, type_fichier, binaire) VALUES (?, ?, ?, ?)", 
                    (id_folder, file_name, file_type, sqlite3.Binary(open(file_path, 'rb').read())))
            conn.commit()