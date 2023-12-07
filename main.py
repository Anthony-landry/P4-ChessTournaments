# Import de class MainVieux puis de la méthode show_menu.
from views.main_view import MainView


# Fonction qui démarre et maintient l'application.
def main():
    """
    fonction qui permet gerer ll'application.
    """
    exit = False
    instanceMainView = MainView()
    while not exit:
        exit = instanceMainView.show_menu()


# Ce code est exécuté uniquement si le fichier est exécuté directement
if __name__ == "__main__":
    main()
