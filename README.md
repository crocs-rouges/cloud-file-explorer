# Cloud File Explorer

## Description

Cloud File Explorer est une application permettant aux utilisateurs de stocker, gérer et accéder à leurs fichiers dans le cloud. Chaque utilisateur dispose d'un compte sécurisé, avec des fonctionnalités de gestion des dossiers et des fichiers. L'application utilise un système de cryptage pour protéger les mots de passe des utilisateurs et gère l'accès aux fichiers de manière sécurisée.

## Fonctionnalités

- Création de comptes utilisateurs avec mot de passe crypté
- Gestion des dossiers et des fichiers
- Téléchargement et affichage de fichiers de différents types
- Interface graphique conviviale avec Tkinter
- Accès sécurisé aux fichiers par utilisateur

## Structure du projet

cloud_file_explorer/
├── main.py                   # Fichier principal pour lancer l'application
├── database/
│   ├── __init__.py           # Rendre le dossier database un module
│   ├── db_setup.py           # Configuration et initialisation des tables
│   └── account_db.py         # Gestion des comptes (enregistrement, connexion)
├── encryption/
│   ├── __init__.py           # Rendre le dossier encryption un module
│   └── password_manager.py    # Gestion du cryptage de mot de passe
├── file_management/
│   ├── __init__.py           # Rendre le dossier file_management un module
│   ├── folders.py            # Gestion des dossiers
│   └── files.py              # Gestion des fichiers
├── ui/
│   ├── __init__.py           # Rendre le dossier ui un module
│   └── app_interface.py      # Interface graphique avec Tkinter
└── utils/
    └── __init__.py           # Rendre le dossier utils un module

## Prérequis

- Python 3.x
- Bibliothèques nécessaires :
  - Tkinter (inclus avec Python)
  - sqlite3 (inclus avec Python)

## Installation

1. Clonez le dépôt :

   ```bash
   git clone <URL_DU_DEPOT>
   cd cloud_file_explorer
2. Installez les dépendances nécessaires (si des bibliothèques externes sont ajoutées ultérieurement).

3. Initialisez la base de données :

python database/db_setup.py
Utilisation
Pour lancer l'application, exécutez le fichier principal :

python main.py
Contributions
Les contributions sont les bienvenues ! Pour contribuer, suivez ces étapes :

Fork le projet.
Créez une nouvelle branche (git checkout -b feature/nouvelle-fonctionnalite).
Faites vos modifications et ajoutez-les (git add .).
Engagez vos modifications (git commit -m 'Ajout d\'une nouvelle fonctionnalité').
Poussez la branche (git push origin feature/nouvelle-fonctionnalite).
Ouvrez une Pull Request.
