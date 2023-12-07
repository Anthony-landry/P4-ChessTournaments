import random

from models.tournament_model import TournamentModel, load_tournement_all_tournament
from views.tournament_view import TournamentView
from models.round_model import RoundModel
from models.match_model import MatchModel


BLANC = 0
NOIR = 1
EGALITE = 2

PLAYER_1 = 0
PLAYER_2 = 1

liste_match_deja_joue = []


class TournamentController:
    """
            classe qui permet de gérer le controller tounoi.
            Attributs:
                 tournament: None / TournamentModel() : L'instance du tournoi à gérer.
                 view: TournamentView() : La vue pour interagir avec l'utilisateur.

            Methodes:
                 def __init__(self): Le constructeur pour initialiser le controleur du tournoi.
                 def create_tounament(self): Permet d'initialiser et de lancer le tournoi.
                 def load_tournament(self): Permet qui initilise la liste des tounrois.
                 def start_tournament(self): Permet de lancer le tounoi.
                 def scoring_player(self, liste_match): Permet de mettre à jour le score des deux joueurs.
                 def saveAllPlayer(self): Permet de sauvegarder la liste des joueurs à jour.
                 def generation_paire(self,list_joueurs, name): Permet de générer des paires de joueurs
                 def generation_paire_by_score(self, list_joueurs, name) -> RoundModel:  permet de générer
                 des paires de joueur en fonction de leur score dans le tournoi.
                 def match_deja_joue(self, j1, j2): Permet de vérifier qu'un match n'a pas déjà été joué.
                 def add_score_player(self, nationalid, point): Ajoute des points aux joueurs
                 def add_pairs_round(self, round): Ajoute un tour à la liste des tours du tournoi.
                 def inc_tour(self): Permet d'incrémenter le tour actuel.
                 def extract_match_deja_joue(self): Permet d'extraire la liste des matchs déjà joués.
                 def __str__(self): Permet de retourner une chaine de caractère
        """

    def __init__(self):
        """
        constructeur pour initialiser le controleur du tournoi.
        :param self: l'instance du TournamentController.
        :type self: <class 'TournamentController'>
        """
        self.tournament = None
        self.view = TournamentView()

    def create_tounament(self):
        """
       initialiser et de lancer le tournoi.
       :param self: l'instance du TournamentController.
       :type self: <class 'TournamentController'>
        """
        sortie = self.view.show_menu()
        nom = sortie[0]
        lieu = sortie[1]
        date_de_debut = sortie[2]
        nombre_de_tours = sortie[3]
        numero_de_tour = sortie[4]
        liste_joueurs_enregistres = sortie[5]
        descritpion_remarque = sortie[6]
        self.tournament = TournamentModel(nom, lieu, date_de_debut, nombre_de_tours,  numero_de_tour,
                                          [], liste_joueurs_enregistres, descritpion_remarque)
        self.tournament.save()
        self.start_tournament()

    def load_tournament(self):
        """
        initilise la liste des tounrois.
        :param self:l'instance du TournamentController.
        :type self: <class 'TournamentController'>
        """
        list_tournament = load_tournement_all_tournament(only_not_finish=True)

        self.tournament = self.view.show_menu_load(list_tournament)
        # On recupere les données du tournoi "name" dans tinyDB
        if self.tournament is not None:
            self.extract_match_deja_joue()
            self.start_tournament()
        else:
            print("Aucun tournoi n'a été initialisé")

    def start_tournament(self):
        """
        Méthode qui permet de lancer le tounoi.
        :param self:l'instance du TournamentController.
        :type self: <class 'TournamentController'>
        """
        if self.tournament:
            # on mélange la liste des joueurs.
            random.shuffle(self.tournament.liste_joueurs_enregistres)
            # print(self.tournament.liste_joueurs_enregistres)
            while self.tournament.numero_de_tour < self.tournament.nombre_de_tours:
                print(f" --- ROUND {self.tournament.numero_de_tour + 1}---")
                if not liste_match_deja_joue:
                    round = self.generation_paire(self.tournament.liste_joueurs_enregistres,
                                                  f"Round {self.tournament.numero_de_tour +1}")
                else:
                    round = self.generation_paire_by_score(self.tournament.liste_joueurs_enregistres,
                                                           f"Round {self.tournament.numero_de_tour +1}")
                self.view.show_match_player(round.liste_match)
                # +++++++++++++++++++++++++++++++++++++++++++++++
                self.scoring_player(round.liste_match)
                # ++++++++++++++++++++++++++++++++++++++++++++++++
                self.tournament.liste_des_tours.append(round)
                self.inc_tour()
                round.finish()

                self.tournament.save()

                self.saveAllPlayer()
            self.tournament.finish()
            self.tournament.save()

        else:
            print("Tournament pas init")

    def scoring_player(self, liste_match):
        """
       Méthode qui permet de mettre à jour le score des deux joueurs.
       :param self: l'instance du TournamentController.
       :type self: <class 'TournamentController'>
       :param liste_match: liste des matchs joués.
       :type liste_match: list <tuple <class 'MatchModel'> > >

        """

        num_match = 1
        # Affichage du round Player 1 VS Player 2
        for player_paire in liste_match:
            liste_match_deja_joue.append((player_paire.player1[0].identifiant_national,
                                          player_paire.player2[0].identifiant_national))
            print(f" --- Match {num_match}---")
            print(
                f"{player_paire.player1[0].nom} {player_paire.player1[0].prenom}"
                f" {player_paire.player1[0].get_color_str()}\n"
                f"{player_paire.player2[0].nom} {player_paire.player2[0].prenom} "
                f"{player_paire.player2[0].get_color_str()}")

            '''
             saisie du resultat ( qui a gagné ? ou equalité ?)
             player =  noir ou player = blanc
            '''
            vainqueur = self.view.select_one_in_list(["Blanc", "Noir", "Egalité"], "resultat")

            if vainqueur == "Blanc":
                if player_paire.player1[0].couleur == BLANC:
                    player_paire.player1 = (player_paire.player1[0], player_paire.player1[1] + 1)

                    print(f"le joueur {player_paire.player1[0].nom} à gagner 1 point.")

                    self.add_score_player(player_paire.player1[0].identifiant_national, 1)
                    self.add_score_player(player_paire.player2[0].identifiant_national, 0)
                else:
                    player_paire.player2 = (player_paire.player2[0], player_paire.player2[1] + 1)
                    print(f"le joueur {player_paire.player2[0].nom} à gagner 1 point.")

                    self.add_score_player(player_paire.player2[0].identifiant_national, 1)
                    self.add_score_player(player_paire.player1[0].identifiant_national, 0)

            elif vainqueur == "Noir":
                if player_paire.player1[0].couleur == NOIR:
                    player_paire.player1 = (player_paire.player1[0], player_paire.player1[1] + 1)
                    print(f"le joueur {player_paire.player1[0].nom} a gagner 1 point.")
                    self.add_score_player(player_paire.player1[0].identifiant_national, 1)
                    self.add_score_player(player_paire.player2[0].identifiant_national, 0)
                else:
                    player_paire.player2 = (player_paire.player2[0], player_paire.player2[1] + 1)
                    print(f"le joueur {player_paire.player2[0].nom} a gagner 1 point.")
                    self.add_score_player(player_paire.player2[0].identifiant_national, 1)
                    self.add_score_player(player_paire.player1[0].identifiant_national, 0)
            elif vainqueur == "Egalité":
                player_paire.player1 = (player_paire.player1[0], player_paire.player1[1] + 0.5)
                player_paire.player2 = (player_paire.player2[0], player_paire.player2[1] + 0.5)

                self.add_score_player(player_paire.player1[0].identifiant_national, 0.5)
                self.add_score_player(player_paire.player2[0].identifiant_national, 0.5)
                print("Match nul 0.5 point pour chaque joueur.")

            # sauvegarde le match
            num_match += 1

    def saveAllPlayer(self):
        """
       Méthode qui permet de sauvegarder dans un ficher le rapport demander par l'utilisateur.
       :param self: l'instance du TournamentController.
       :type self: <class 'TournamentController'>
       :return: -
        """
        for player in self.tournament.liste_joueurs_enregistres:
            player.save()

    def generation_paire(self, list_joueurs, name):
        """
       Méthode qui permet de sauvegarder dans un ficher le rapport demander par l'utilisateur.
       :param self: l'instance du TournamentController.
       :type self: <class 'TournamentController'>
       :param list_joueurs: liste de joueurs.
       :type: liste < <class 'PlayerModel'> >
       :param name: nom du tour.
       :type: str
       :return: le tour avec la liste des matches générés par rapport à la liste des joueurs.
       :rtype: <class 'RoundModel'>
       """

        # representation d'un match ([ j , S ],[j ;  S ])
        # liste_joueurs sous la forme d'une liste de PlayerModel

        liste_paire_joueurs = []
        for x in range(0, len(list_joueurs), 2):
            list_joueurs[x].couleur = random.choice([NOIR, BLANC])
            # ou 0 ou 1 (noir), sinon on peux utilisé un bool et inversé le resulat pour l'autre
            list_joueurs[x+1].couleur = NOIR - list_joueurs[x].couleur
            instance_match = MatchModel(list_joueurs[x], list_joueurs[x + 1])
            liste_paire_joueurs.append(instance_match)

        round = RoundModel(name, liste_paire_joueurs)
        return round

    def generation_paire_by_score(self, list_joueurs, name) -> RoundModel:
        """
        Permet de générer des paires de joueur en fonction de leur score dans le tournoi.
       :param self: l'instance du TournamentController.
       :type self: <class 'TournamentController'>
       :param list_joueurs: liste de joueurs.
       :type: list < <class 'PlayerModel'> >
       :param name: nom du tour.
       :type: str
       :return: le tour avec la liste des matches générés par rapport à la liste des joueurs.
       :rtype: <class 'RoundModel'>
        """
        list_pairing = []
        list_joueurs_sorted = sorted(list_joueurs, key=lambda x: x.scoretournois, reverse=True)
        players_selected = []
        for player_white in list_joueurs_sorted:
            if player_white not in players_selected:
                players_selected.append(player_white)
                # looking for player black
                for player_black in list_joueurs_sorted:
                    if player_black not in players_selected and not self.match_deja_joue(player_white, player_black):
                        instance_match = MatchModel(player_white, player_black)
                        list_pairing.append(instance_match)
                        players_selected.append(player_black)
                        break
        round = RoundModel(name, list_pairing)
        return round

    def match_deja_joue(self, j1, j2):
        """
        Permet de vérifier qu'un match n'a pas déjà été joué.
        :param self: l'instance du TournamentController.
        :type self: <class 'TournamentController'>
        :param j1: joueur 1
        :type j1: <class 'PlayerModel'>
        :param j2: joueur 2
        :type j2: <class 'PlayerModel'>
        :return: si un match entre j1 et j2 est déjà joué.
        :rtype : bool
        """

        global liste_match_deja_joue
        if (j1.identifiant_national, j2.identifiant_national) not in liste_match_deja_joue and \
           (j2.identifiant_national, j1.identifiant_national) not in liste_match_deja_joue:
            return False
        return True

    def add_score_player(self, nationalid, point):
        """
       Ajoute des points au joueur.
       :param self: l'instance du TournamentController.
       :type self: <class 'TournamentController'>
       :param nationalid: identifiant du joueur auquel on veut ajouter des points.
       :type nationalid: str
       :param point: les points ajoutés aux joueurs
       :type point: int
       """
        for player in self.tournament.liste_joueurs_enregistres:
            if player.identifiant_national == nationalid:
                player.scoretournois += point
                player.scoreglobal += point

    def add_pairs_round(self, round):
        """
        Ajoute un tour à la liste des tours du tournoi.
        :param self: l'instance du TournamentController.
        :type self: <class 'TournamentController'>
        :param round: le tour à ajouter.
        :type round: <class 'RoundModel'>
        """
        self.tournament.liste_des_tours.append(round)

    def inc_tour(self):
        """
         Permet d'incrémenter le tour actuel.
         :param self: l'instance du TournamentController.
         :type self: <class 'TournamentController'>
         :return: -
        """
        self.tournament.numero_de_tour += 1

    def extract_match_deja_joue(self):
        """
         Permet d'extraire la liste des matchs déjà joués.
         :param self: l'instance du TournamentController.
         :type self: <class 'TournamentController'>
         :return: -
        """
        global liste_match_deja_joue

        if self.tournament is not None:
            for round in self.tournament.liste_des_tours:
                for match in round.liste_match:
                    liste_match_deja_joue.append((match.player1[0].identifiant_national,
                                                  match.player2[0].identifiant_national))

    def __str__(self):
        """
         Permet de retourner une chaine de caractère representant le controleur du tournoi
         :param self: l'instance du TournamentController.
         :type self: <class 'TournamentController'>
         :return: la representation du controleur de tournoi
         :rtype: str
        """
        if self.tournament:
            return "Tournois init\n"
        else:
            return "Tournois pas init\n"
