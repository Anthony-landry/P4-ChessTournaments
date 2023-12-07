# OpenClassrooms: Projet 4 - Gestionnaire de Tournoi d'Échecs

Ce programme a été développé dans le cadre du projet 4 d'OpenClassrooms. Il s'agit d'un gestionnaire de tournois d'échecs.

![Gestionnaire de Tournoi d'Échecs](.readme/landry_anthony_chesstournament_openclassroms_developpeur_python_application.png)

## Installation

Pour commencer, assurez-vous d'avoir Python installé sur votre système.

Ensuite, suivez ces étapes pour installer et exécuter le programme :

1. Clonez ce dépôt dans le répertoire de votre choix en utilisant la commande suivante :
    
    ```bash
    git clone https://github.com/Anthony-landry/P4-ChessTournaments.git
    ```
    
2. Accédez au dossier P4-ChessTournaments.
    
3. Créez un nouvel environnement virtuel en utilisant la commande suivante :
    
    ```bash
    python -m venv env
    ```
    
4. Activez l'environnement virtuel :
    
    * Sur Windows :
        
        ```bash
        env\Scripts\activate.bat
        ```
        
    * Sur Linux :
        
        ```bash
        source env/bin/activate
        ```
        
5. Installez les packages requis en exécutant la commande suivante :
    
    ```bash
    pip install -r requirements.txt
    ```
    
6. Vous pouvez maintenant lancer le script principal avec la commande :
    
    ```bash
    python main.py
    ```
    

## Utilisation

Le menu principal est divisé en 4 options.

### 1) Créer des joueurs

* Lorsque vous sélectionnez cette option, vous êtes invité à spécifier à saisir les informations du joueur.

### 2) Créer un tournoi

* Cette option vous permet de gérer des tournois d'échecs. Lors de la première utilisation, sélectionnez "Créer un tournoi", puis suivez les instructions.
* Pendant un tournoi, vous serez invité à entrer les résultats après chaque match.
* Pendant le tournoi, si le programme à été fermé, il est possible de reprendre le tournoi en cours ultérieurement.

### 3) Reprendre un tournoi en cours

* Cette section vous permet de charger un tournoi depuis la base de données.
* Une fois le tournoi chargé, vous serez invité à le continuer.

### 4) Les rapports

* Cette section vous permet de générer différents rapports.
* Vous pouvez consulter le classement global des joueurs par classement et par ordre alphabétique.
* Vous pouvez également obtenir des détails sur les tournois passés, y compris le classement des joueurs, les tours et les matchs de chaque tournoi.

### 5) Générer le rapport Flake8

Pour générer le rapport Flake8, suivez ces étapes :

1. Installez Flake8 avec la commande :
    
    ```bash
    pip install flake8-html
    ```
    
2. Si le fichier setup.cfg n'existe pas, créez-le.
    
3. Ajoutez le texte suivant dans le fichier setup.cfg :
    
    ```ini
    [flake8]
    exclude = .git, env, __pycache__, .gitignore
    max-line-length = 119
    ```
    
4. Exécutez la commande suivante pour générer le rapport :
    
    ```bash
    flake8 --format=html --htmldir=flake-report  --exclude=venv

    ```
    

Le rapport sera généré dans le dossier "flake-report".
