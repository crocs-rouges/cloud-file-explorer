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
    password TEXT NOT NULL
    )
''')
conn.commit()

def double_click_action(event):
    print("Double-clic détecté, fonction lancée !")

def single_click_action(event):
    print("Bouton sélectionné")
    event.widget.config(bg="lightblue")  # Change la couleur du bouton lors de la sélection



root = tk.Tk()
root.title("Interface de jeu")

label_nom = tk.Label(root, text=" tout les dossiers seront présents ici")
label_nom.grid(row=0, column=0)
entree_nom = tk.Button(root, text="dossier N1")
entree_nom.grid(row=0, column=10, padx=10, pady=10)

button = tk.Button(root, text="Cliquez ici", bg="red")
button.grid(pady=50)

# Liaison des événements
button.bind("<Button-1>", single_click_action)  # Clic simple
button.bind("<Double-1>", double_click_action)  # Double-clic



label_resultat = tk.Label(root, text="", fg="red")
label_resultat.grid(row=2, column=0, columnspan=2, padx=10,
                    pady=10)



root.mainloop()

