# ui/app_interface.py

import tkinter as tk
from database.account_db import AccountManager
from file_management.folders import FolderManager
from file_management.files import FileManager

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.account_manager = AccountManager()
        self.folder_manager = FolderManager()
        self.file_manager = FileManager()
        self.title("Cloud File Explorer")
        self.user_id = None
        self.init_login_screen()

    def init_login_screen(self):
        # Création de l'interface de connexion
        self.login_frame = tk.Frame(self)
        self.login_frame.pack()
        tk.Label(self.login_frame, text="Nom d'utilisateur").pack()
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()
        tk.Label(self.login_frame, text="Mot de passe").pack()
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack()
        tk.Button(self.login_frame, text="Connexion", command=self.check_login).pack()

    def check_login(self):
        # Vérification de l'identité de l'utilisateur
        email = self.username_entry.get()
        password = self.password_entry.get()
        if self.account_manager.login(email, password):
            self.login_frame.pack_forget()
            self.user_id = self.account_manager.get_user_id(email)
            self.init_main_interface()
        else:
            tk.Label(self.login_frame, text="Erreur de connexion", fg="red").pack()

    def init_main_interface(self):
        # Interface principale après la connexion
        self.main_frame = tk.Frame(self)
        self.main_frame.pack()
        username = self.username_entry.get()
        tk.Label(self.main_frame, text="Bienvenue dans votre espace de fichiers").pack()
        self.folder_manager.show_folders(username)
        # faire une zone ou on peut ajouter des boutons et avoir un scroll si il y en a trop
        
        
        # zone bouton ajouter et supprimer dossiers
        tk.Label(self.main_frame, text="Nom du nouveau dossier").pack()
        self.folder_name = tk.Entry(self.main_frame)
        self.folder_name_entry = tk.Entry(self.main_frame)
        self.folder_name.pack()
        
        
        tk.Button(self.main_frame, text="ajouter", command=self.add_folder).pack()
        
    def add_folder(self):
        username = self.user_id
        foldername = self.folder_name_entry.get()
        # on arrive pas à obtenir le nom du fichier créer
        # le formatage
        print("debut")
        print(username)
        print("patate")
        print(foldername)
        print("comment")
        if self.folder_manager.add_folder(username, foldername):
            tk.Label(self.main_frame, text="Dossier créer", fg="green").pack()
        else:
            tk.Label(self.main_frame, text="Erreur lors de la création", fg="red").pack()
        
        # Autres widgets pour la gestion des dossiers et fichiers
