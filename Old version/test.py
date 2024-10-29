import tkinter as tk

def show_frame(frame):
    frame.tkraise()  # Met le cadre au premier plan

# Création de la fenêtre principale
root = tk.Tk()
root.title("Navigation avec Retour")
root.geometry("400x300")

# Configuration pour que chaque frame occupe l'espace
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Création de deux frames
main_frame = tk.Frame(root)
second_frame = tk.Frame(root)

for frame in (main_frame, second_frame):
    frame.grid(row=0, column=0, sticky='nsew')

# Contenu de la page principale
main_label = tk.Label(main_frame, text="Page principale", font=('Helvetica', 18))
main_label.pack(pady=20)

# Bouton pour aller à la seconde page
go_to_second_button = tk.Button(main_frame, text="Aller à la seconde page", command=lambda: show_frame(second_frame))
go_to_second_button.pack()

# Contenu de la seconde page
second_label = tk.Label(second_frame, text="Seconde page", font=('Helvetica', 18))
second_label.pack(pady=20)

# Bouton retour à la page principale
back_button = tk.Button(second_frame, text="Retour", command=lambda: show_frame(main_frame))
back_button.pack()

# Afficher le premier cadre (main_frame)
show_frame(main_frame)

root.mainloop()
