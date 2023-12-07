from views.view import View
from models.player_model import PlayerModel
from utils.date_manip import get_timestamp


PLAYER_1 = 0
PLAYER_2 = 1


class TournamentView(View):
    """
    classe qui permet permet de gérer les intéractions avec le choix de l'utilisateur.
    Hérite de la class View.

    Methodes:
        def show_menu(self): Permet de récuperer le choix utilisateur du menu des rapports.
        def show_menu_load(self, list_tournament): Permet de récuper une valeur dans une liste.
        def show_match_player (self, list_match): Permet d'afficher le match.

    """

    def show_menu(self):
        """
        Retourne les informations saisi pour un tournoi.
        :param self: l'instance du TournamentView.
        :type self: <class 'TournamentView'>
        :return: les informations sur le tournoi.
        :rtype: tuple <X>
        """
        nom = self.input_str("nom: ")
        lieu = self.input_str("entrez un lieu: ")
        date_de_debut = get_timestamp()
        all_player = PlayerModel.get_all_player_from_db()
        while True:
            nombre_de_tours = self.input_int("nombre de tour (defaut : 4): ", defaut_value=4)
            if nombre_de_tours*2 > len(all_player):
                print("Vous avez selectionner trop de tour par rapport au nombre de joueurs inscrit")
            else:
                break

        numero_de_tour = 0
        nb_player = nombre_de_tours*2
        liste_joueurs_enregistres = self.select_many_in_list(all_player, nb_player, "player")
        descritpion_remarque = self.input_str("remarque général: ")

        return nom, lieu, date_de_debut, nombre_de_tours, numero_de_tour, \
            liste_joueurs_enregistres, descritpion_remarque

    def show_menu_load(self, list_tournament):
        """
        Permet de redemarrer un tournoi.
        :param self: l'instance du TournamentView.
        :type self: <class 'TournamentView'>
        :param list_tournament: liste des tournois en cours.
        :type list_tournament: list < class 'TournamentModel'>
        :return: le tournoi à redemarrer.
        :rtype: None / <class 'TournamentModel'>
        """
        print("====================================")
        while True:
            if list_tournament == []:

                print("\n\nAucun tournois en cours\n\n")

                return None
            else:
                for idx, tournament in enumerate(list_tournament):
                    print(f"[{idx}] {tournament.nom} {tournament.lieu} ( {tournament.date_de_debut} )")

                tournament_id_select = self.input_int("Selectionner le tournois qu'il faut reprendre: ")
                if tournament_id_select in range(len(list_tournament)):
                    return list_tournament[tournament_id_select]
                else:
                    print("L id sélectionné(", tournament_id_select, ") n'est pas correct.")

    def show_match_player(self, list_match):
        """
        Permet d'afficher le match en cours.
        :param self: l'instance du TournamentController.'
        :type self: <class 'TournamentController'>
        :param list_match: liste des matchs en cours
        :type list_match: list_tournament: list < class 'RoundModel'>
        """
        # +++ round.list_match = list_match) +++
        for player_paire in list_match:
            # Nom [Couleur ]   VS Nom [Couleur ]   VS
            # ...
            print(f"{player_paire.player1[0].nom} {player_paire.player1[0].get_color_str()}  VS "
                  f"{player_paire.player2[0].nom} {player_paire.player2[0].get_color_str()} ")

            # Enter pour demarrer

        input("appuyez 'enter' pour demarrer")
