from tinydb import TinyDB

from models.player_model import PlayerModel, getPlayerFromID
from views.player_view import PlayerView


# controleur qui gère un player
class PlayerController:
    """
    controleur qui gère un player
    Attributs:
        -
    Methodes:
        - def create_player(self)
    """
    def create_player(self):
        """
        Permet de créer un joueur et de l'ajouter à la bd
        :param self: l'instance du PlayerController
        :return: -
        """
        player_view = PlayerView()
        nom, prenom, date_de_naissance, identifiant_national = player_view.show_menu()

        # Verification player que le player n'existe pas.
        p = getPlayerFromID(identifiant_national)
        if p:
            PlayerView.display_error(f"Existe déjà {p.nom} {p.prenom} {p.identifiant_national}")
            return

        player = PlayerModel(nom, prenom, date_de_naissance, identifiant_national)
        db = TinyDB('datas/player.json')
        db.insert({"nom": player.nom,
                   "prenom": player.prenom,
                   "date_de_naissance": player.date_de_naissance,
                   "identifiant_national": player.identifiant_national})
