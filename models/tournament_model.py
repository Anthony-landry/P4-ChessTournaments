from tinydb import TinyDB, Query
from models.player_model import getPlayerFromID
from models.round_model import RoundModel
from models.match_model import MatchModel
from utils.date_manip import get_timestamp

PATH = 'datas/tournament.json'
PLAYER_1 = 0
PLAYER_2 = 1


class TournamentModel:
    """
    classe qui permet de gérer le modèle du tournoi.
    .
    Attributs instance:
        nom: le nom du tournoi.
        lieu: le lieu du tournoi.
        date_de_debut: la date de début du tournoi.
        nombre_de_tours: le nombre de tour dans le tournoi.
        numero_de_tour: le numero du tour actuel dans le tournoi.
        liste_des_tours: la liste des tours du tournoi.
        liste_joueurs_enregistres: la liste des joueurs enregistrés dans le tournoi
        description_remarque: Permet d'ajouter une remarque sur le tournoi en cours

    Methodes:
        def __init__(self,
                nom,
                lieu,
                date_de_debut,
                nombre_de_tours:4,
                numero_de_tour,
                liste_des_tours,
                liste_joueurs_enregistres,
                descritpion_remarque
                 ):
        Le constructeur pour initialiser le modèle du tournoi.
        def save(self):  Méthode qui permet de sauvegarder le tournoi dans la base de données.
        def finish(self): Méthode qui permet de terminer le tournoi.
        def to_dict(self): Méthode qui permet de retourner un dictionnaire avec les informations du tournoi.
        def to_dict_for_update(self): Permet de récupérer le tournoi sous forme de dictionnaire pour mise à jour
    """

    def __init__(self,
                 nom, lieu, date_de_debut, nombre_de_tours: 4, numero_de_tour, liste_des_tours,
                 liste_joueurs_enregistres, descritpion_remarque):

        """
        Description
        :param self: l'instance du TournamentModel.
        :type self: <class 'TournamentModel'>
        :param nom: le nom du joueur.
        :type nom: str
        :param lieu: le lieu du tournois.
        :type lieu: str
        :param date_de_debut: la date du début du tournois.
        :type date_de_debut: str
        :param nombre_de_tours: le nombre de tour dans le tournoi.
        :type nombre_de_tours: int
        :param numero_de_tour: le numéro dans le tour.
        :type numero_de_tour: int
        :param liste_des_tours: la liste des tours dans le tournoi
        :type liste_des_tours: list < class 'RoundModel' >
        :param liste_joueurs_enregistres: la liste des joueurs enregistrés dans le tournoi
        :type liste_joueurs_enregistres: list < class 'PlayerModel' >
        :param descritpion_remarque: Permet d'inscrire une remarque sur le tournoi en cours.
        :type descritpion_remarque: str
        """

        self.nom = nom
        self.lieu = lieu
        self.date_de_debut = date_de_debut
        self.date_de_fin = ""
        self.nombre_de_tours = nombre_de_tours
        self.numero_de_tour = numero_de_tour
        self.liste_des_tours = liste_des_tours
        self.liste_joueurs_enregistres = liste_joueurs_enregistres
        self.descritpion_remarque = descritpion_remarque

    def save(self):
        """
            Méthode qui permet de sauvegarder le tournoi dans la base de données.
            :return: le resultat de la sauvegarde.
            :rtype: list <str>
        """
        db = TinyDB(PATH, indent=4)
        query = Query()
        tournoi = db.search(query.nom == self.nom)

        if len(tournoi) == 0:
            return db.insert(self.to_dict())
        else:
            return db.update(self.to_dict_for_update(), query.nom == self.nom)

    def finish(self):
        """
            Méthode qui permet de terminer le tournoi.
        """
        self.date_de_fin = get_timestamp()

    def to_dict(self):
        """
           Méthode qui permet de retourner un dictionnaire avec les informations du tournoi.
            :return: retourne un dictionnaire avec les informations du tournoi.
            :rtype: dict<str,X>
        """
        liste_joueurs_enregistres_dict = []
        for player in self.liste_joueurs_enregistres:
            # liste_joueurs_enregistres_dict.append(player.identifiant_national)
            liste_joueurs_enregistres_dict.append(player.to_dict_for_tournament())

        return {
            "nom": self.nom,
            "lieu": self.lieu,
            "date_de_debut": self.date_de_debut,
            "date_de_fin": self.date_de_fin,
            "nombre_de_tours": self.nombre_de_tours,
            "numero_de_tour": self.numero_de_tour,
            "liste_des_tours": self.liste_des_tours,
            "liste_joueurs_enregistres": liste_joueurs_enregistres_dict,
            "descritpion_remarque": self.descritpion_remarque
        }

    def to_dict_for_update(self):
        """
            Permet de récupérer le tournoi sous forme de dictionnaire pour mise à jour
            :return: retourne un dictionnaire avec les informations du tournoi.
            :rtype: dict <str, X >
        """
        liste_joueurs_enregistres_dict = []
        for player in self.liste_joueurs_enregistres:
            liste_joueurs_enregistres_dict.append(player.to_dict_for_tournament())

        liste_round_dict = []
        for round in self.liste_des_tours:
            liste_round_dict.append(round.to_dict())

        return {
            "date_de_fin": self.date_de_fin,
            "numero_de_tour": self.numero_de_tour,
            "liste_des_tours": liste_round_dict,
            "liste_joueurs_enregistres": liste_joueurs_enregistres_dict
        }

    def __str__(self):
        """
            retourne la chaine de de caractère pour la fonction str(objet).
            :return: une chaine de caractères avec les informations du tournoi.
            :rtype: str
        """
        return self.nom


def load_tournement_all_tournament(only_not_finish=False):
    """
        Fonction qui permet de charger tous les tournois.
        :param only_not_finish: paremetre qui indique les tournois pas finis.
        :type only_not_finish: bool
        :return: retourne la liste des tounois.
        :rtype: list <class 'TournamentModel'>
    """

    # On recupere les données du tournoi "name" dans tinyDB
    db = TinyDB(PATH, indent=4)
    if only_not_finish:
        x = [item for item in db.all() if item["nombre_de_tours"] != item["numero_de_tour"]]
    else:
        x = db.all()

    list_tournois = []
    for tournoi in x:
        list_tournois.append(dict_to_tournament(tournoi))
    return list_tournois


def load_tournament(name):
    """
        Fonction qui permet de charger un tournoi.
        :param name: nom du tournoi à charger.
        :type name: str
        :return: le tournoi dont le nom est passé en paramètre.
        :rtype: <class 'TournamentModel'>  / None
    """
    # On recupere les données du tournoi "name" dans tinyDB
    db = TinyDB(PATH, indent=4)
    tournoi_query = Query()
    # je recupère tous les tournois qui correspond à la condition.
    x = db.search(tournoi_query.nom == name)
    # on verifie que l'on recupère qu'un seul tournois donnée.

    if len(x) == 1:
        return dict_to_tournament(x[0])
    return None


def dict_to_tournament(dict_tournament):
    """
        Fonction qui permet de construction un tournoi à partir du dictionnaire passé en paramètre.
        :param dict_tournament: répresentation du tournoi sous forme de dictionnaire.
        :type dict_tournament: dict <str, X>
        :rtype: <class 'TournamentModel'>
    """
    listPlayer = []
    for player in dict_tournament["liste_joueurs_enregistres"]:
        inst_player = getPlayerFromID(player["identifiant_national"],
                                      player["scoretournois"] if "scoretournois" in player else 0)
        listPlayer.append(inst_player)

    liste_des_tours = []
    for round in dict_tournament["liste_des_tours"]:
        list_match = []
        for match in round["liste_match"]:
            instance_match = MatchModel(getPlayerFromID(match[PLAYER_1][0]),
                                        getPlayerFromID(match[PLAYER_2][0]), match[PLAYER_1][1], match[PLAYER_2][1])
            list_match.append(instance_match)
        liste_des_tours.append(RoundModel(round["nom"], list_match, round["date_de_debut"], round["date_de_fin"]))
    tournament = TournamentModel(
        dict_tournament["nom"],
        dict_tournament["lieu"],
        dict_tournament["date_de_debut"],
        dict_tournament["nombre_de_tours"],
        dict_tournament["numero_de_tour"],
        liste_des_tours,
        listPlayer,
        dict_tournament["descritpion_remarque"])

    tournament.date_de_fin = dict_tournament["date_de_fin"]
    return tournament
