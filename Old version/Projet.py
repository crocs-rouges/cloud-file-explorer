import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('jeu.db')

# Création d'un curseur pour interagir avec la base de données
cur = conn.cursor()
# Création d'une table
cur.execute('''
    CREATE TABLE IF NOT EXISTS joueur (
        id_joueur INTEGER PRIMARY KEY AUTOINCREMENT,
        nom_joueur TEXT NOT NULL
        score_joueur INTEGER >= 0
    )
''')
conn.commit()


def ajouter_joueur(nom: str):
    cur.execute('INSERT INTO joueur (nom_joueur) VALUES (?)', (nom,))
    conn.commit()


def ajouter_joueur_interface():
    nom = entree_nom.get()
    cur.execute('INSERT INTO joueur (nom_joueur) VALUES (?)', (nom,))
    conn.commit()


def valider():
    nom = entree_nom.get()
    label_resultat.config(text=f"Votre nom est desormais {nom}")


root = tk.Tk()
root.title("Interface de jeu")

label_nom = tk.Label(root, text="Nom du joueur :")
label_nom.grid(row=0, column=0)
entree_nom = tk.Entry(root)
entree_nom.grid(row=0, column=1, padx=10, pady=10)

bouton_ajouter = tk.Button(root, text="Valider", command=valider)
bouton_ajouter.grid(row=1, column=0, padx=10, pady=10)

label_resultat = tk.Label(root, text="", fg="red")
label_resultat.grid(row=2, column=0, columnspan=2, padx=10,
                    pady=10)

root.mainloop()
conn.close()
