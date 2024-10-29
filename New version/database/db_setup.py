# database/db_setup.py

import sqlite3

def init_db():
    conn = sqlite3.connect("cloud_storage.db")
    cursor = conn.cursor()
    # Création des tables Compte, Dossier et Fichier
    cursor.execute('''CREATE TABLE IF NOT EXISTS Compte (
                        id_compte INTEGER PRIMARY KEY AUTOINCREMENT,
                        adresse TEXT UNIQUE NOT NULL,
                        mot_de_passe TEXT NOT NULL,
                        carte_bancaire TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Dossier (
                        id_dossier INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_compte INTEGER,
                        nom_dossier TEXT,
                        FOREIGN KEY(id_compte) REFERENCES Compte(id_compte))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Fichier (
                        id_fichier INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_dossier INTEGER,
                        nom_fichier TEXT,
                        type_fichier TEXT,
                        fichier_binaire BLOB,
                        FOREIGN KEY(id_dossier) REFERENCES Dossier(id_dossier))''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
