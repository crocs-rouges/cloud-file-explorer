# ui/app_interface.py

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import sqlite3
import io
from database.account_db import AccountManager
from file_management.folders import FolderManager
from file_management.files import FileManager

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap("images/Logo.ico")
        self.account_manager = AccountManager()
        self.folder_manager = FolderManager()
        self.file_manager = FileManager()
        self.title("Cloud File Explorer")
        self.user_id = None
        self.folder = self.folder_manager.get_folders(self.user_id)
        self.folderNAME = self.initfolderNAME(self.folder)

        self.page_choix = tk.Frame(self)
        self.page_choix.grid(row=0, column=0, sticky="nsew")
        self.page_connexion = tk.Frame(self)  # initialisation_page_connexion()
        self.page_connexion.grid(row=0, column=0, sticky="nsew")
        self.page_creation = tk.Frame(self)  # self.initialisation_page_creation()
        self.page_creation.grid(row=0, column=0, sticky="nsew")
        
        self.init_connexion_screen()
        
    def initfolderNAME(self, folder):
        folderNAME = []
        for name in folder:
            folderNAME.append(name[1])
        return folderNAME

    def init_connexion_screen(self):
        # self.initialisation()
        self.page_choix.tkraise()

        self.bouton_connexion = tk.Button(self.page_choix, text="Connexion au compte", command=self.init_login_screen, 
                                          bg="#00AA90", fg="white")
        self.bouton_connexion.grid(row=3, column=5)

        self.bouton_creation = tk.Button(self.page_choix, text="Creation du compte", command=self.start_creation_compte
                                        bg="#00AA90", fg="white")
        self.bouton_creation.grid(row=3, column=2)

    def init_login_screen(self):
        # Création de l'interface de connexion
        self.login_frame = tk.Frame(self)
        self.login_frame.grid(row=0, column=0, sticky="nsew")
        tk.Label(self.login_frame, text="Nom d'utilisateur").pack()
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()
        tk.Label(self.login_frame, text="Mot de passe").pack()
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack()
        tk.Button(self.login_frame, text="Connexion", command=self.check_login, bg="#00AA90", fg="white").pack()
        self.error_label = tk.Label(self.login_frame, text="", fg="red") 
        self.error_label.pack()

    def start_creation_compte(self):
        self.page_creation.tkraise()

        self.nom = tk.Entry(self.page_creation)
        self.prenom = tk.Entry(self.page_creation)
        self.email = tk.Entry(self.page_creation)
        self.password = tk.Entry(self.page_creation)

        label_nom = tk.Label(self.page_creation, text="Nom")
        label_prenom = tk.Label(self.page_creation, text="Prénom")
        label_email = tk.Label(self.page_creation, text="Adresse Email")
        label_password = tk.Label(self.page_creation, text="Mot de passe")

        label_nom.grid(row=0, column=0)
        self.nom.grid(row=0, column=1)
        label_prenom.grid(row=1, column=0)
        self.prenom.grid(row=1, column=1)
        label_email.grid(row=2, column=0)
        self.email.grid(row=2, column=1)
        label_password.grid(row=3, column=0)
        self.password.grid(row=3, column=1)

        # bouton_creer = tk.Button(self.page_creation, text="Creation du compte", command=self.creer_compte)
        # bouton_creer.grid(row=5, column=1)

        bouton_retour = tk.Button(self.page_creation, text="Retour", command=self.init_connexion_screen, bg="#00AA90", 
                                  fg="white")
        bouton_retour.grid(row=5, column=0)
    
    def check_login(self):
        email = self.username_entry.get()
        password = self.password_entry.get()
        if self.account_manager.login(email, password):
            self.login_frame.pack_forget()
            result = self.account_manager.get_user_id(email)
            self.user_id = result[0] if isinstance(result, tuple) else result  # Extrait l'ID du tuple si nécessaire
            self.folder = self.folder_manager.get_folders(self.user_id)
            self.folderNAME = self.initfolderNAME(self.folder)
            self.init_folder_interface()
        else:
            self.error_label.config(text="Erreur de connexion")





    def init_folder_interface(self):
        self.login_frame.pack_forget()
        # Interface principale après la connexion
        self.folder_main = tk.Frame(self)
        self.folder_main.grid(row=0, column=0, sticky="nsew")
        tk.Label(self.folder_main, text="Bienvenue dans votre espace de fichiers").pack()
        self.folder = self.folder_manager.get_folders(self.user_id)
        self.folderNAME = self.initfolderNAME(self.folder)
        
        # compiler tout le code en dessous en un bouton qui ouvre une page pour ajouter un bouton
        # Zone pour ajouter des dossiers
        tk.Label(self.folder_main, text="Nom du nouveau dossier").pack()
        self.folder_name_entry = tk.Entry(self.folder_main)  # Entrée pour nom de dossier
        self.folder_name_entry.pack()
        # Bouton pour ajouter un nouveau dossier
        tk.Button(self.folder_main, text="Ajouter", command=self.add_folder, bg="#00AA90", fg="white").pack()
        # bouton pour supprimer un fichier
        tk.Label(self.folder_main, text="dossier à supprimer").pack()
        # Menu déroulant pour afficher les options
        self.selected_var = tk.StringVar()
        self.selected_var.set("Sélectionne une option")
        print(self.folder)
        print(self.folderNAME)
        self.menu = tk.OptionMenu(self.folder_main, self.selected_var, *self.folderNAME)
        self.menu.pack(pady=10)
        
        # Bouton pour ajouter un nouveau dossier
        tk.Button(self.folder_main, text="supprimer", command=self.delete_folder, bg="#00AA90", fg="white").pack()
        
        # zone qui affiche tous les dossiers
        # la listbox est une liste de tous les dossiers
        self.listbox = tk.Listbox(self.folder_main, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10, fill=tk.BOTH)
        self.showfolder()
        # bouton pour ouvrir les dossiers
        tk.Button(self.folder_main, text="Ouvrir", command=self.openfolder, bg="#00AA90", fg="white").pack()


    def showfolder(self):
        # affiche tous les dossiers venant de la base de données
        # et étant relié au compte de l'utilisateur
        self.folder = self.folder_manager.get_folders(self.user_id)
        self.folderNAME = self.initfolderNAME(self.folder)
        self.listbox.delete(0,tk.END)
        for option in self.folderNAME:
            self.listbox.insert(tk.END, option)

    def delete_folder(self):
        # supprime le dossier choisi par l'utilisateur
        folderNAME = self.selected_var.get()
        self.folder_manager.delete_folder(self.user_id, folderNAME)
        self.showfolder()

    def add_folder(self):
        # partie logique qui sert à créer un fichier
        # et à l'ajouter à la base de données
        self.folder = self.folder_manager.get_folders(self.user_id)
        self.folderNAME = self.initfolderNAME(self.folder)
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
            self.folder = self.folder_manager.get_folders(self.user_id)
            self.folderNAME = self.initfolderNAME(self.folder)
            # Optionnel : faire disparaître le message après quelques secondes
            self.after(3000, success_label.destroy)
        else:
            # Afficher un message d'erreur
            error_label = tk.Label(self.folder_main, text="Erreur lors de la création du dossier.", fg="red")
            error_label.pack()
            # Optionnel : faire disparaître le message après quelques secondes
            self.after(3000, error_label.destroy)

    def openfolder(self):
        folderName = self.listbox.get(tk.ACTIVE)
        print(folderName)
        self.folderID = self.folder_manager.get_file_id(folderName)
        self.folderID = self.folderID[0][0]
        print(self.folderID)
        success = self.file_manager.get_files(self.folderID)
        if success:
            self.init_files_interface()
        else:
            error_label = tk.Label(self.folder_main, text="Erreur lors de l'ouverture du dossier.", fg="red")
            error_label.pack()
            


    def init_files_interface(self):
        self.folder_main.pack_forget()
        # Interface principale après l'ouverture d'un fichier
        self.file_main = tk.Frame(self)
        self.file_main.grid(row=0, column=0, sticky="nsew")
        
        tk.Label(self.file_main, text="rename the file currently selected").pack()
        self.file_name_entry = tk.Entry(self.file_main)  # Entrée pour nom de dossier
        self.file_name_entry.pack()
        tk.Button(self.file_main, text="rename the file", command=self.rename_file, bg="#00AA90", fg="white").pack()
        
        self.listboxfile = tk.Listbox(self.file_main, width=50)
        self.listboxfile.pack()
        self.showfile()
        # bouton pour ouvrir les dossiers
        tk.Button(self.file_main, text="Ouvrir", command=self.openfile, bg="#00AA90", fg="white").pack()
        
        tk.Button(self.file_main, text="ajouter des fichiers", command=self.addfile, bg="#00AA90", fg="white").pack()


    def addfile(self):
        # Ouvrir la boîte de dialogue de sélection de fichier
        file_path = filedialog.askopenfilename()
        # Vérifier si un fichier a été sélectionné
        if file_path:
            # Extraire le nom du fichier 
            # Utilisez os.path pour une méthode plus robuste
            import os
            file_name = os.path.basename(file_path)
            # Extraire l'extension du fichier
            file_type = os.path.splitext(file_path)[1].lstrip('.')
            # Convertir le fichier en données binaires
            filedata = self.file_manager.convert_file_to_binary(file_path)
            # Vérifier que la conversion a réussi
            if filedata is not None:
                # Ajouter le fichier à la base de données
                self.file_manager.add_file(self.folderID, file_name, file_type, filedata)
                # Mettre à jour l'interface
                self.listbox.insert(tk.END, file_name)
                self.showfile()
            else:
                # Gérer l'erreur de conversion
                tk.messagebox.showerror("Erreur", "Impossible de convertir le fichier")

    def rename_file(self):
        fileName = self.listboxfile.get(tk.ACTIVE)
        print("bonjour")
        print(fileName)
        print("coucou")
        self.file_manager.rename_file(self.folderID, fileName, self.file_name_entry.get())
        self.init_files_interface()
        

    def openfile(self):
        file_name = self.listboxfile.get(tk.ACTIVE)
        file_type = self.file_manager.get_file_type(file_name)
        binary_data = self.file_manager.get_binary(file_name)
        binary_data = self.file_manager.convert_to_str(binary_data)
        self.file_manager.open_binary(binary_data, file_type)
        
    def display_image(self, photo):
        self.image_label = tk.Label(self.file_main, image=photo)
        self.image_label.image = photo
        self.image_label.pack()


    def initfileNAME(self, allfile):
        fileNAME = []
        for name in allfile:
            fileNAME.append(name[1])
        return fileNAME

    def showfile(self):
        # affiche tous les dossiers venant de la base de données
        # et étant relié au compte de l'utilisateur
        self.file = self.file_manager.get_files(self.folderID)
        print(self.file)
        self.fileNAME = self.initfileNAME(self.file)
        print(self.fileNAME)
        self.listboxfile.delete(0,tk.END)
        for option in self.fileNAME:
            self.listboxfile.insert(tk.END, option)
