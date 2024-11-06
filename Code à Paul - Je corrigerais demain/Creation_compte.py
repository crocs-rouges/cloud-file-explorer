import tkinter as tk
from tkinter import messagebox
import sqlite3


class ChaineTropLongueException(Exception):
    pass


conn = sqlite3.connect('cloud.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS  connexion (
    id_utilisateur INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
    )
''')
conn.commit()





# def start():
#     bouton_connexion = tk.Button(root, text="Connexion au compte", command=start_creation_compte)
#     bouton_connexion.grid(row=3, column=5)
#
#     bouton_creation = tk.Button(root, text="Creation du compte", command=start_creation_compte)
#     bouton_creation.grid(row=3, column=2)

root = tk.Tk()
root.title("Cloud :")


class Login:
    def __init__(self):
        self.page_choix = tk.Frame(root)
        self.page_choix.grid(row=0, column=0, sticky="nsew")
        self.page_connexion = tk.Frame(root) #initialisation_page_connexion()
        self.page_connexion.grid(row=0, column=0, sticky="nsew")
        self.page_creation = tk.Frame(root) #self.initialisation_page_creation()
        self.page_creation.grid(row=0, column=0, sticky="nsew")

        self.nom = ""
        self.prenom = ""
        self.email = ""
        self.password = ""

    def start(self):
        # self.initialisation()
        self.page_choix.tkraise()

        self.bouton_connexion = tk.Button(self.page_choix, text="Connexion au compte", command=self.start_connexion_compte)
        self.bouton_connexion.grid(row=3, column=5)

        self.bouton_creation = tk.Button(self.page_choix, text="Creation du compte", command=self.start_creation_compte)
        self.bouton_creation.grid(row=3, column=2)

    def retour(self):
        self.page_choix.tkraise()

            # self.bouton_connexion = tk.Button(self.page_choix, text="Connexion au compte", command=self.start_creation_compte)
            # self.bouton_connexion.grid(row=3, column=5)

            # self.bouton_creation = tk.Button(self.page_choix, text="Creation du compte", command=self.start_creation_compte)
            # self.bouton_creation.grid(row=3, column=2)
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

        bouton_creer = tk.Button(self.page_creation, text="Creation du compte", command=self.creer_compte)
        bouton_creer.grid(row=5, column=1)

        bouton_retour = tk.Button(self.page_creation, text="Retour", command=self.start)
        bouton_retour.grid(row=5, column=0)

    def start_connexion_compte(self):
        self.page_connexion.tkraise()

        self.email = tk.Entry(self.page_connexion)
        self.password = tk.Entry(self.page_connexion)

        label_email = tk.Label(self.page_connexion, text="Adresse Email")
        label_password = tk.Label(self.page_connexion, text="Mot de passe")

        label_email.grid(row=2, column=0)
        self.email.grid(row=2, column=1)
        label_password.grid(row=3, column=0)
        self.password.grid(row=3, column=1)

        bouton_connexion = tk.Button(self.page_connexion, text="Connexion au compte", command=self.connexion_compte)
        bouton_connexion.grid(row=5, column=1)

        bouton_retour = tk.Button(self.page_connexion, text="Retour", command=self.start)
        bouton_retour.grid(row=5, column=0)
    def creer_compte(self):
        nom = self.nom.get()
        prenom = self.prenom.get()
        email = self.email.get()
        password = self.password.get()
        if len(nom) <= 0:
            messagebox.showerror("Erreur", "Veuillez entrez votre nom")
            return
        elif len(prenom) <= 0:
            messagebox.showerror("Erreur", "Veuillez entrez votre prenom")
            return
        elif len(email) <= 3:
            messagebox.showerror("Erreur", "Veuillez entrez votre email")
            return
        elif len(password) <= 12:
            messagebox.showerror("Erreur", "Le mot de passe doit contenir au moins 12 caractères")
            return
        print("nom ", nom)
        print("prenom ", prenom)
        print("password ", password)
        c = conn.cursor()
        # "{nom}", "{prenom}", "{email}","{password}"
        c.execute(f'INSERT INTO connexion (nom, prenom, email, password) VALUES ("{nom}", "{prenom}", "{email}","{password}")')
        conn.commit()
        conn.close()

        #entree_nom.delete(0, tk.END)
        #entree_prenom.delete(0, tk.END)
        #entree_password.delete(0, tk.END)

        messagebox.showinfo(" ", "Le compte a bien été crée")
    
    def connexion_compte(self):
        email = self.email.get()
        password = self.password.get()

        
        c = conn.cursor()
        c.execute('SELECT email, password FROM connexion')  # Requête pour récupérer tous les comptes
        comptes = c.fetchall()  # Récupération de toutes les lignes
        conn.close()  # Fermeture de la connexion
        print(comptes)

        for compte in comptes:
            print(compte)
            if email == compte[0] and password == compte[1]:
                messagebox.showinfo("Succès", "Vous êtes connecté")
                return True
            
        messagebox.showerror("Erreur", "Email ou mot de passe incorrect")
        #entree_nom.delete(0, tk.END)
        #entree_prenom.delete(0, tk.END)
        #entree_password.delete(0, tk.END)

        # messagebox.showinfo(" ", "Le compte a bien été crée")

print(Login().start())

root.mainloop()
