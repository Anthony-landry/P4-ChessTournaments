from utils.date_manip import get_timestamp


class RoundModel:
    """
    classe qui permet géré le modèle des tours

    Attributs instance:
        nom: le nom du tour.
        liste_match: une liste des matchs.
        date_de_debut: la date du début du tour.
        date_de_fin: la date de fin de tour.

    Methodes:
        def __init__(self, nom, liste_match, date_de_debut= get_timestamp(), date_de_fin=""): constructeur pour
        initialiser le model du joueur.
        def finish(self): Permet de mettre à jour la date de la fin du tour.
        def to_dict(self): Méthode qui permet de retourner une représentation du tour sous forme de dictionnaire.

    """
    def __init__(self, nom, liste_match, date_de_debut=get_timestamp(), date_de_fin=""):
        """
        constructeur pour initialiser le modèle du tour.
        :param self: l'instance du RoundModel.
        :type self: <class 'RoundModel'>
        :param nom: le nom du tour.
        :type nom: str
        :param liste_match: la liste des matches du tour
        :type liste_match: list< <class 'MatchModel'> >
        :param date_de_debut: la date de début du tour
        :type date_de_debut: str
        :param date_de_fin: la date de début du tour
        :type date_de_fin: str

        """
        self.nom = nom
        self.liste_match = liste_match
        self.date_de_debut = date_de_debut
        self.date_de_fin = date_de_fin

    def finish(self):
        """
        Permet de mettre à jour la date de la fin du tour..
        """

        self.date_de_fin = get_timestamp()

    def to_dict(self):
        """
        Méthode qui permet de retourner une représentation du tour sous forme de dictionnaire.
        :return: la réprésentation du joueur
        :rtype:  dict<str, X>
        """

        liste_match_dict = []
        for match in self.liste_match:
            liste_match_dict.append(([match.player1[0].identifiant_national, match.player1[1]],
                                     [match.player2[0].identifiant_national, match.player2[1]]))

        return {
            "nom": self.nom,
            "date_de_debut": self.date_de_debut,
            "date_de_fin": self.date_de_fin,
            "liste_match": liste_match_dict
        }
