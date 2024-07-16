# Projet Back-end : Concessionnaire//RATTRAPAGES

## Description

Ce projet est une application backend permettant de gérer les ventes, clients, voitures, et modèles de voitures pour un concessionnaire. Il permet de suivre les ventes des employés, avec des rôles spécifiques pour les vendeurs et les managers.

## Fonctionnalités

- CRUD pour les ventes, clients, voitures, modèles de voiture.
- Authentification via JWT.
- Hachage des mots de passe.
- Chiffrement des informations sensibles (nom, prénom, email).

## Prérequis

- [Python 3.8+](https://www.python.org/downloads/)
- [MySQL](https://www.mysql.com/downloads/)
- [HeidiSQL](https://www.heidisql.com/download.php) 

## Installation

1. **Clonez le dépôt :**

    [git clone <repository_url>](https://github.com/hugo-gaudre/ProjetConcessionnaire.git)
    cd <repository_directory>


2. **Créez et activez un environnement virtuel :**

    python -m venv env
    source env/bin/activate  # Pour Windows: env\Scripts\Activate.ps1 <---

3. **Installez les dépendances :**

    pip install -r requirements.txt


4. **Créez un fichier `.env` dans le répertoire principal avec le contenu suivant :**

    ```plaintext
    SECRET_KEY=your_secret_key
    DATABASE_URL=mysql+pymysql://username:password@localhost/concessionnaire
    ```

    Remplacez `your_secret_key`, `username`, `password`, et `localhost/concessionnaire` par vos propres valeurs.

## Initialisation de la Base de Données

1. **Initialisez la base de données :**

    python init_db.py


2. **Seed la base de données avec des données initiales :** (Optionnel mais ça m'a principalement faciliter mes tests avec Swagger)

    python seed_db.py

## Lancement de l'application

uvicorn app.main:app --reload
