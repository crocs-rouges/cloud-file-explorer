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
            self.init_folder_interface()
        else:
            tk.Label(self.login_frame, text="Erreur de connexion", fg="red").pack()

    def init_folder_interface(self):
        # Interface principale après la connexion
        self.folder_main = tk.Frame(self)
        self.folder_main.pack()
        username = self.username_entry.get()
        tk.Label(self.folder_main, text="Bienvenue dans votre espace de fichiers").pack()
        
        
        # compiler tout le code en dessous en un bouton qui ouvre une page pour ajouter un bouton
        # Zone pour ajouter des dossiers
        tk.Label(self.folder_main, text="Nom du nouveau dossier").pack()
        self.folder_name_entry = tk.Entry(self.folder_main)  # Entrée pour nom de dossier
        self.folder_name_entry.pack()
        # Bouton pour ajouter un nouveau dossier
        tk.Button(self.folder_main, text="Ajouter", command=self.add_folder).pack()
        
        
        # bouton pour supprimer un fichier
        tk.Label(self.folder_main, text="dossier à supprimer").pack()
        self.folder_name_entry = tk.Entry(self.folder_main)  # Entrée pour nom de dossier
        self.folder_name_entry.pack()
        # Bouton pour ajouter un nouveau dossier
        tk.Button(self.folder_main, text="supprimer", command=self.delete_folder).pack()
        
        
        
        
        # zone qui affiche tous les dossiers
        self.folder_manager.show_folders(self.user_id)
        self.showfolder()
        
        
        # bouton pour ouvrir les dossiers
        tk.Button(self.folder_main, text="Ouvrir", command=self.openfolder).pack()

    def init_files_interface(self):
        # Interface principale après l'ouverture d'un fichier
        self.file_main = tk.Frame(self)
        self.file_main.pack()
        username = self.username_entry.get()
        tk.Label(self.file_main, text="Bienvenue dans votre espace de fichiers").pack()
        tk.Label(self.file_main, text="ici sont affichés tous vos fichiers").pack()


    def showfolder(self):
        # affiche tous les fichiers venant  de la base de données
        # et étant relié au compte de l'utilisateur
        
        # bug quand un  fichier est supprimé, il reste dans la liste
        # bug quand les fichiers s'affiche il se place à la fin de la page tkinter et pas dans une zone spécial
        


        folder_id = self.folder_manager.get_folders(self.user_id)
        self.folder_manager.show_folders(self.user_id)
        for i in range(len(folder_id)):
            tk.Label(self.folder_main, text=folder_id[i]).pack()

            

    def add_folder(self):
        # partie logique qui sert à créer un fichier
        # et à l'ajouter à la base de données
    
        
        # prend tout les dossiers de l'utilisateurs
        foldername = self.folder_name_entry.get().strip()  # Enlève les espaces inutiles

        if not foldername:
            # gestion de l'erreur si l'utilisateur  n'a pas saisi de nom de dossier
            tk.Label(self.folder_main, text="Veuillez entrer un nom de dossier.", fg="red").pack()
            return

        # Tenter de créer le dossier
        success = self.folder_manager.add_folder(self.user_id, foldername)
        
        if success:
            # Effacer le champ de saisie
            self.folder_name_entry.delete(0, tk.END)
            
            # Mettre à jour l'affichage des dossiers
            self.folder_manager.show_folders(self.user_id)
            self.showfolder()
            
            # Afficher un message de succès
            success_label = tk.Label(self.folder_main, text=f"Dossier '{foldername}' créé avec succès.", fg="green")
            success_label.pack()
            
            # Optionnel : faire disparaître le message après quelques secondes
            self.after(3000, success_label.destroy)
        else:
            # Afficher un message d'erreur
            error_label = tk.Label(self.folder_main, text="Erreur lors de la création du dossier.", fg="red")
            error_label.pack()
            
            # Optionnel : faire disparaître le message après quelques secondes
            self.after(3000, error_label.destroy)

        

    def openfolder(self , folderName):
        success = self.file_manager.get_files(folderName)
        
        if success:
            self.init_file_interface()
        else:
            error_label = tk.Label(self.folder_main, text="Erreur lors de l'ouverture du dossier.", fg="red")
            error_label.pack()
            



