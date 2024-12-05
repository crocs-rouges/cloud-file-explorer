# file_management/files.py

import sqlite3
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import tempfile

class FileManager:
    def __init__(self):
        self.conn = sqlite3.connect("cloud_storage.db")



    def add_file(self, folder_id, file_name, file_type, file_data):
        """ajoute un fichier dans la base de donnée

        Args:
            folder_id (int): l'idantifiant du fichier
            file_name (str): le nom du fichier
            file_type (str): l'extension du fichier
            file_data (int binaire): tout le ficier en binaire ou exadécimal 
        """
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Fichier (id_dossier, nom_fichier, type_fichier, binaire) VALUES (?, ?, ?, ?)",
                       (folder_id, file_name, file_type, file_data))
        self.conn.commit()

    def get_file_type(self, file_name):
        """une méthode qui donne le type du fichier demandé

        Args:
            file_name str: nom du fichier souhaité

        Returns:
            list: une liste de tuples qui continent le type du fichier
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT type_fichier FROM Fichier WHERE nom_fichier = ?", (file_name,))
        return cursor.fetchall()

    def get_files(self, folder_id):
        """une méthode qui donne toutes les informations
        concernant tous les fichiers d'un dossiers spécifiques

        Args:
            folder_id (_type_): _description_

        Returns:
            list: une liste de tuples qui continent toutes les informations sur un fichier
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT id_fichier, nom_fichier, type_fichier FROM Fichier WHERE id_dossier = ?", (folder_id,))
        return cursor.fetchall()
        
        
    def rename_file(self, id_folder, file_name, new_name : str):
        """change le nom du fichier sélectionner avec le nouveau nom

        Args:
            id_folder (int): identifiant du dossier dans lequel est le fichier
            file_name (str): nom du fichier sélectionner pour etre renommé
            new_name (str): nouveau nom du fichier sélectionner qui va remplacer l'ancien
        """
        
        cursor = self.conn.cursor()
        cursor.execute("UPDATE Fichier SET nom_fichier = ? WHERE id_dossier = ? AND nom_fichier = ?", 
                    (new_name, id_folder, file_name))
        self.conn.commit()
    

    def convert_file_to_binary(self , file_path):
        """
        Convertit un fichier en données binaires.
        
        Args:
            file_path (str): Chemin complet vers le fichier.
        
        Returns:
            bytes: Données binaires du fichier
        """
        try:
            # Lire le fichier en mode binaire
            with open(file_path, 'rb') as file:
                return file.read()
        
        except FileNotFoundError:
            print(f"Erreur : Le fichier {file_path} n'a pas été trouvé.")
            return None
        
        except Exception as e:
            print(f"Erreur lors de la conversion du fichier : {e}")
            return None
        
    def convert_to_str(self, bytes_tab):
        if isinstance(bytes_tab, bytes):
            return bytes_tab.decode('utf-8')
        return ''.join(chr(b) for b in bytes_tab)

    def get_binary(self, file_name) -> bytes:
        """prend le fichier en binaire et le renvoie sous forme de bytes
        

        Args:
            file_name (str): nom du fichier qui va etre ouvert par windows

        Returns:
            bytes: bytes qui vont etre lu par la méthode open_binary
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT binaire FROM Fichier WHERE nom_fichier = ?", (file_name,))
            result = cursor.fetchone()
            print(result)
            if result:
                binary_data = result[0]
                # Vérifier si les données sont au format hexadécimal
                if isinstance(binary_data, bytes) and binary_data.startswith(b'0x'):
                    # Convertir les données hexadécimales en bytes
                    binary_data = binary_data[2:]  # Supprimer le préfixe '0x'
                    binary_data = bytes.fromhex(binary_data.decode('ascii'))
                return binary_data
            else:
                print(f"Aucune donnée trouvée pour {file_name}")
                return None
        except Exception as e:
            print(f"Erreur lors de la récupération des données binaires : {e}")
            return None

    def open_binary(self, binary_data, file_extension):
        """
        Ouvre un fichier binaire à partir de données binaires.
        en convertissant les bytes en un fichier temporaire qui sera supprimé après la lecture
        ce fichier temporaire est ouvert par windows et est donc accessible par le système d'exploitation

        Args:
            binary_data (bytes): Données binaires à écrire dans le fichier.
            file_extension (str): Extension du fichier (ex: '.jpg', '.pdf').

        Returns:
            bool: True si le fichier a été ouvert avec succès, False sinon.
        """
        try:
            # Vérifier que binary_data est bien de type bytes
            if not isinstance(binary_data, bytes):
                raise TypeError("Les données doivent être de type bytes")

            # Créer un fichier temporaire et y écrire les données
            with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as temp_file:
                temp_file.write(binary_data)
                temp_file_path = temp_file.name

            # Ouvrir le fichier
            os.startfile(temp_file_path)
            return True

        except Exception as e:
            print(f"Erreur lors de l'ouverture du fichier : {e}")
            return False