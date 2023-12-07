from views.view import View


class PlayerView(View):
    """
    Classe qui permet de gérer la vue du joueur.
    Hérite de la class View.

    Methodes:
     def show_menu(self): permet de retourner les informations du joueur qui ont été saisies.
     def display_error(message): affiche un message d'erreur.

    """

    def show_menu(self):
        """
        Méthode qui permet de retourner les informations du joueur qui ont été saisies.
        :param self: l'instance du PlayerView.
        :type self: <class 'PlayerView'>.
        :return: les informations du joueur.
        :rtype: tuple <str>
        """
        nom = self.input_str("nom du joueur: ")
        prenom = self.input_str("prénom du joueur: ")
        date_de_naissance = self.input_date("date de naissance du joueur (JJ/MM/AAAA): ")
        identifiant_national = self.input_id("votre identifiant national (AB12345): ")
        return nom, prenom, date_de_naissance, identifiant_national

    @staticmethod
    def display_error(message):
        """
        Afficher un message d'erreur.
        :param message : le message à faire afficher.
        :type message: str

        """
        print("Erreur", message)
