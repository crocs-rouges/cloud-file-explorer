# file_management/folders.py

import sqlite3

class FolderManager:
    def __init__(self):
        self.conn = sqlite3.connect("cloud_storage.db")

    def add_folder(self, user_id, folder_name):
        try:
            cursor = self.conn.cursor()
            # Vérifier si le dossier existe déjà pour cet utilisateur
            cursor.execute("SELECT COUNT(*) FROM Dossier WHERE id_compte = ? AND nom_dossier = ?",
                         (user_id, folder_name))
            if cursor.fetchone()[0] > 0:
                print(f"Le dossier {folder_name} existe déjà pour cet utilisateur")
                return False
            
            # Ajouter le nouveau dossier
            cursor.execute("INSERT INTO Dossier (id_compte, nom_dossier) VALUES (?, ?)",
                         (user_id, folder_name))
            self.conn.commit()
            print(f"Dossier {folder_name} créé avec succès pour l'utilisateur {user_id}")
            return True
        except sqlite3.Error as e:
            print(f"Erreur lors de la création du dossier: {e}")
            return False

    def get_folders(self, user_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT id_dossier, nom_dossier FROM Dossier WHERE id_compte = ?", (user_id,))
            return cursor.fetchall()  # Retourne tous les dossiers
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération des dossiers: {e}")
            return []

    def show_folders(self, user_id):
        try:
            folders = self.get_folders(user_id)
            if not folders:
                print(f"Aucun dossier trouvé pour l'utilisateur {user_id}")
                return []
            
            print(f"Dossiers de l'utilisateur {user_id}:")
            for folder_id, folder_name in folders:
                print(f"ID: {folder_id}, Nom: {folder_name}")
            return folders
        except Exception as e:
            print(f"Erreur lors de l'affichage des dossiers: {e}")
            return []

    def __del__(self):
        """Ferme la connexion à la base de données lors de la destruction de l'objet"""
        if hasattr(self, 'conn'):
            self.conn.close()
