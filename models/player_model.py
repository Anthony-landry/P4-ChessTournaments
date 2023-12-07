from tinydb import TinyDB, Query

PATH = 'datas/player.json'


class PlayerModel:
    """
    classe qui permet géré le modèle des joueurs.
    Attributs instance:
        nom : le nom du joueur.
        prenom : le prénom du joueur.
        date_de_naissance : la date de naissance du joueur.
        identifiant_national: l'identifiant du joueur.
        couleur: la couleur du joueur.
        scoreglobal: le score global du joueur.
        scoretournois: le score du joueur dans le tournoi.

    Methodes:
        def __init__(self, nom, prenom, date_de_naissance, identifiant_national, couleur=None, scoreglobal=0,
         scoretournois=0) : Le constructeur pour initialiser le modèle du joueur.
        def get_all_player_from_db(): Permet de récupérer les listes des joueurs depuis la database.
        def add_point_to_player(nationnal_id, point): Permet d'ajouter les points au joueurs.
        def load_player(nationnal_id): Permet de charger un joueurs avec son identifiant national.
        def get_color_str(self): Permet de retourner l'affectation de la couleur.
        def to_dict(self): Permet de retourner un dictionnaire avec les informations du joueurs.
        def to_dict_for_tournament(self): Permet de retourner une représentation du joueur pour un tournoi.
        def to_dict_for_tour(self): Permet de retourner une représentation du joueur pour un tour.
        def save(self): Permet de sauvegarder le joueur dans la base de donnée.
    """
    def __init__(self, nom, prenom, date_de_naissance, identifiant_national, couleur=None, scoreglobal=0,
                 scoretournois=0):
        """
           constructeur pour initialiser le model du joueur.
           :param self: l'instance du PlayerModel.
           :type self: <class 'PlayerModel'>

             :param nom: le nom du joueur.
             :type nom: str
             :param prenom: le prénom du joueur.
             :type prenom: str
             :param date_de_naissance: la date de naissance du joueur.
             :type date_de_naissance: str
             :param identifiant_national: l'identifiant du joueur.
             :type identifiant_national: str
             :param couleur: la couleur du joueur.
             :type couleur: int / None
             :param scoreglobal: le score global du joueur.
             :type scoreglobal: int
             :param scoretournois: le score du joueur dans le tournoi.
             :type scoretournois: int

        """

        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.identifiant_national = identifiant_national
        self.couleur = couleur
        self.scoreglobal = scoreglobal
        self.scoretournois = scoretournois

    @staticmethod
    def get_all_player_from_db():
        """
            Permet de récupérer les listes des joueurs depuis la database.
            :return: une liste de tous les joueurs présent dans la base de donnée.
            :rtype: list < <class 'PlayerModel'>  >
        """
        players_db = TinyDB(PATH, indent=4)
        players_db.all()
        players = []
        for item in players_db:
            player = PlayerModel(item["nom"],
                                 item["prenom"],
                                 item["date_de_naissance"],
                                 item["identifiant_national"],
                                 item["couleur"] if "couleur" in item else None,
                                 item["scoreglobal"] if "scoreglobal" in item else 0,
                                 item["scoretournois"] if "scoretournois" in item else 0)
            players.append(player)
        players_db.close()

        return players

    @staticmethod
    def add_point_to_player(nationnal_id, point):
        """
            Méthode qui permet d'ajouter les points au joueurs.
            :param nationnal_id: l'identifiant national du joueur.
            :type nationnal_id: str
            :param point: le nombre de points a ajouté du joueur.
            :type point: int
            :return: Retourne la liste du résultat de la mise à jour du score du joueur dans la base de donnée.
            :rtype: list<int>
        """
        players_db = TinyDB(PATH, indent=4)
        query = Query()
        player = players_db.search(query.identifiant_national == nationnal_id)

        current_score = 0
        if len(player) == 1 and "score" in player[0]:
            current_score = int(player[0]["score"])
        ret = players_db.update({'score': current_score + point}, query.identifiant_national == nationnal_id)
        players_db.close()

        return ret

    @staticmethod
    def load_player(nationnal_id):
        """
            Méthode qui permet de charger un joueurs avec son identifiant national.
            :param nationnal_id: l'identifiant national du joueur.
            :type nationnal_id: str
            :return: retourne une liste du joueur.
            :rtype: list < class 'PlayerModel'>
        """
        players_db = TinyDB(PATH, indent=4)
        query = Query()
        ret = players_db.search(query.identifiant_national == nationnal_id)
        players_db.close()

        return ret

    def get_color_str(self):
        """
            Méthode qui permet de retourner l'affectation de la couleur.
            :return: la couleur assignée au joueur.
            :rtype: str
        """
        if not self.couleur:
            return "BLANC"
        return "NOIR"

    def to_dict(self):
        """
            Méthode qui permet de retourner un dictionnaire avec les informations du joueur.
            :return: le dictionnaire contenant les informations associés au joueur.
            :rtype: dict<str, X>
        """
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "date_de_naissance": self.date_de_naissance,
            "identifiant_national": self.identifiant_national,
            "scoreglobal": self.scoreglobal
        }

    def to_dict_for_tournament(self):
        """
           Méthode qui permet de retourner une représentation du joueur pour un tournoi.
           :return: le dictionnaire contenant les informations associés au joueur.
           :rtype: dict<str, X>
        """
        return {
            "identifiant_national": self.identifiant_national,
            "scoretournois": self.scoretournois
        }

    def to_dict_for_tour(self):
        """
            Méthode qui permet de retourner une représentation du joueur pour un tour.
            :return: le dictionnaire contenant les informations associés au joueur.
            :rtype: dict<str, X>
        """
        return {
            "identifiant_national": self.identifiant_national,
            "couleur": self.couleur,
            "scoretournois": self.scoretournois
        }

    def save(self):
        """
            Méthode qui permet de sauvegarder le joueur dans la base de donnée.
            :return: le resultat de la sauvegarde.
            :rtype: list <int>
        """
        db = TinyDB(PATH, indent=4)
        query = Query()
        tournoi = db.search(query.identifiant_national == self.identifiant_national)

        if len(tournoi) == 0:
            ret = db.insert(self.to_dict())
        else:
            ret = db.update(self.to_dict(), query.nom == self.nom)
        db.close()

        return ret

    def __str__(self):
        """
            retourne la chaine de de caractère pour la fonction str(objet).
            :return: une chaine de caractères avec les informations du joueur.
            :rtype: str
        """
        return f"{self.nom} {self.prenom} {self.date_de_naissance} {self.identifiant_national}" \
               f" {self.scoreglobal} {self.scoretournois}"

    def __repr__(self):
        """
            retourne la chaine de de caractère pour la fonction , et print(objet).
            :return: une chaine de caractères avec les informations du joueur.
            :rtype: str
        """
        return f"{self.nom} {self.prenom} {self.date_de_naissance} {self.identifiant_national} " \
               f"{self.scoreglobal} {self.scoretournois}"


def getPlayerFromID(idnational, scoretournois=0):
    """
        Retourne la représentation du joueur par l'identifiant passé en paramètre.
        :param idnational: l'identifiant national du joueur.
        :type idnational: str
        :param scoretournois: le score final du joueur à la fin du tournoi.
        :type scoretournois: int
        :rtype: <class 'PlayerModel'>  / None
    """
    players_db = TinyDB(PATH, indent=4)
    query = Query()
    player_dict = players_db.search(query.identifiant_national == idnational)
    if player_dict:
        return PlayerModel(player_dict[0]["nom"],
                           player_dict[0]["prenom"],
                           player_dict[0]["date_de_naissance"],
                           player_dict[0]["identifiant_national"],
                           player_dict[0]["scoreglobal"] if "scoreglobal" in player_dict[0] else 0,
                           scoretournois)
    return None
