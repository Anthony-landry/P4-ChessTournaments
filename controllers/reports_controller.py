from models.player_model import PlayerModel
from models.tournament_model import load_tournement_all_tournament
from views.reports_view import ReportsView


class ReportController:
    """
        controleur qui gère les rapports.
        Attributs:
            - reportView: ReportsView

        Methodes:
            - def __init__(self)
    """
    def __init__(self):
        self.reportView = ReportsView()

    #
    def create_report(self):
        """
             Méthode qui permet de sauvegarder dans un ficher le rapport demander par l'utilisateur.
             :param self: l'instance du ReportController
             :return: -
        """
        choix = self.reportView.show_menu()

        match choix:
            case "1":
                self.list_all_players()
            case "2":
                self.list_all_tournament()
            case "3":
                self.name_and_date_tournament()
            case "4":
                self.list_player_sorted()
            case "5":
                self.all_round_and_all_match()

    def list_all_players(self):
        """
            Methode qui récupère la liste de tous les joueurs pour les écrire dans un fichier texte.
            :param self: l'instance du ReportController
            :return: -
        """

        list_all_players = PlayerModel.get_all_player_from_db()
        list_all_players = sorted(list_all_players, key=lambda x: x.nom, reverse=False)

        fichier = open("report_tournoi.txt", "a")
        title = "List all players !"
        self.write_title_in_report(fichier, title)

        for player in list_all_players:
            print(f"{player.nom} {player.prenom} ({player.scoreglobal})\n")
            fichier.write(f"{player.nom} {player.prenom} ({player.scoreglobal})\n")
        fichier.close()

    def list_all_tournament(self):
        """
          Methode qui récupère la liste de tous les tournois pour les écrire dans un fichier texte.
          :param self: l'instance du ReportController
          :return: -
        """

        list_all_tournament = load_tournement_all_tournament()

        fichier = open("report_tournoi.txt", "a")
        title = "List all tournament !"
        self.write_title_in_report(fichier, title)

        for tournament in list_all_tournament:
            print(tournament.nom+"\n")
            fichier.write(tournament.nom+"\n")
        fichier.close()

    def name_and_date_tournament(self):
        """
           Methode qui récupère la liste de tous les nom et tournois pour les écrire dans un fichier texte.
           :param self: l'instance du ReportController
           :return: -

        """
        # affichier la liste des tournois + selection.
        list_all_tournament = load_tournement_all_tournament()
        tournament = self.reportView.show_select_in_list(list_all_tournament, "tournoi")
        if tournament:
            fichier = open("report_tournoi.txt", "a")
            title = "Name and date tournament !"
            self.write_title_in_report(fichier, title)
            print("\n le nom du tournoi : " + tournament.nom)
            print("\n la date début : " + tournament.date_de_debut + "  la date début : " + tournament.date_de_fin)
            print("\n")
            fichier.write(tournament.nom + " " + tournament.date_de_debut + " " + tournament.date_de_fin + "\n")
            fichier.close()

    def list_player_sorted(self):
        """
           Methode qui récupère la liste de tous les joueurs, les tri par nom par ordre Alphabétique,
           et les écrient dans un fichier texte.
           :param self: l'instance du ReportController
           :return: -

        """
        list_all_tournament = load_tournement_all_tournament()
        tournament = self.reportView.show_select_in_list(list_all_tournament, "tournoi")
        if tournament:
            fichier = open("report_tournoi.txt", "a")
            title = "list player sorted !"
            self.write_title_in_report(fichier, title)

            fichier.write(f"Tournoi: {tournament.nom}\n\n")

            list_player_sorted = sorted(tournament.liste_joueurs_enregistres, key=lambda x: x.nom)
            for player in list_player_sorted:
                print(f"{player.nom}  {player.prenom} ({player.scoreglobal})")
                fichier.write(f"{player.nom}  {player.prenom} ({player.scoreglobal})\n")
            fichier.close()

    def all_round_and_all_match(self):
        """
           Methode qui récupère liste de tous les tours du tournoi et de tous les matchs du tour
           pour les écrire dans un fichier texte.
           :param self: l'instance du ReportController
           :return: -

        """
        list_all_tournament = load_tournement_all_tournament()
        tournament = self.reportView.show_select_in_list(list_all_tournament, "tournoi")
        if tournament:
            fichier = open("report_tournoi.txt", "a")
            title = "All rounds and all match report !"
            self.write_title_in_report(fichier, title)
            fichier.write(f"Tournoi: {tournament.nom}\n\n")

            data_str = ""
            for round in tournament.liste_des_tours:
                data_str += "\n" + round.nom + " " + round.date_de_debut + " " + round.date_de_fin
                for match in round.liste_match:
                    data_str += "\n" + match.player1[0].nom + " vs " + match.player2[0].nom + "\n"
                    if match.player1[1] > match.player2[1]:
                        data_str += 'le vainqueur est ' + match.player1[0].nom + "\n"
                    elif match.player1[1] < match.player2[1]:
                        data_str += 'le vainqueur est ' + match.player2[0].nom + "\n"
                    else:
                        data_str += 'match nul\n'
            print(data_str)
            fichier.write(data_str)
            fichier.close()

    def write_title_in_report(self, fichier, title):
        """
            Méthode qui ecrit un titre dans le rapport
           :param title:
           :param fichier:
           :param self: l'instance du ReportController
           :return: -

        """
        fichier.write("\n" + "=" * len(title)+"\n")
        fichier.write(title+"\n")
        fichier.write("=" * len(title)+"\n"*2)
