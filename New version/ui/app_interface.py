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
        email = self.username_entry.get()
        password = self.password_entry.get()
        if self.account_manager.login(email, password):
            self.login_frame.pack_forget()
            result = self.account_manager.get_user_id(email)
            self.user_id = result[0] if isinstance(result, tuple) else result  # Extrait l'ID du tuple si nécessaire
            self.init_main_interface()
        else:
            tk.Label(self.login_frame, text="Erreur de connexion", fg="red").pack()

    def init_main_interface(self):
        # Interface principale après la connexion
        self.main_frame = tk.Frame(self)
        self.main_frame.pack()
        username = self.username_entry.get()
        tk.Label(self.main_frame, text="Bienvenue dans votre espace de fichiers").pack()
        
        # Afficher les dossiers existants
        self.folder_manager.show_folders(username)
        
        # Zone pour ajouter et supprimer des dossiers
        tk.Label(self.main_frame, text="Nom du nouveau dossier").pack()
        self.folder_name_entry = tk.Entry(self.main_frame)  # Entrée pour nom de dossier
        self.folder_name_entry.pack()
        # Bouton pour ajouter un nouveau dossier
        tk.Button(self.main_frame, text="Ajouter", command=self.add_folder).pack()
        
        
        # bouton pour supprimer un fichier
        
        # zone qui affiche tous les dossiers 
        
        
        
        # bouton pour ouvrir les dossiers

    def add_folder(self):
        username = self.user_id
        foldername = self.folder_name_entry.get().strip()  # Enlève les espaces inutiles

        if not foldername:
            tk.Label(self.main_frame, text="Veuillez entrer un nom de dossier.", fg="red").pack()
            return

        # Tenter de créer le dossier
        success = self.folder_manager.add_folder(username, foldername)
        
        if success:
            # Effacer le champ de saisie
            self.folder_name_entry.delete(0, tk.END)
            
            # Mettre à jour l'affichage des dossiers
            folders = self.folder_manager.show_folders(username)
            
            # Afficher un message de succès
            success_label = tk.Label(self.main_frame, text=f"Dossier '{foldername}' créé avec succès.", fg="green")
            success_label.pack()
            
            # Optionnel : faire disparaître le message après quelques secondes
            self.after(3000, success_label.destroy)
        else:
            # Afficher un message d'erreur
            error_label = tk.Label(self.main_frame, text="Erreur lors de la création du dossier.", fg="red")
            error_label.pack()
            
            # Optionnel : faire disparaître le message après quelques secondes
            self.after(3000, error_label.destroy)

        
        # Autres widgets pour la gestion des dossiers et fichiers
