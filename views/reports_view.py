from views.view import View


class ReportsView(View):
    """
    classe qui permet de gérer les intéractions avec le choix de l'utilisateur.
    Hérite de la class View.

    Methodes:
        def show_menu(self): Permet de récuperer le choix utilisateur du menu des rapports.
        def show_select_in_list(self, list_data, name): Permet de récuper une valeur dans une liste.

    """

    def show_menu(self):
        """
        Méthode qui permet de retourner les informations
        :param self: l'instance du ReportsView.
        :type self: <class 'ReportsView'>.
        :return: le choix de l'entrée du menu.
        :rtype: str
        """

        menu = [
            "1 : liste de tous les joueurs par ordre alphabétique.",
            "2 : liste de tous les tournois.",
            "3 : nom et dates d’un tournoi donné.",
            "4 : liste des joueurs du tournoi par ordre alphabétique.",
            "5 : liste de tous les tours du tournoi et de tous les matchs du tour.",
            "r : retour dans le menu principal."
        ]
        choix = self.affichage_menu(
            "\n=== RAPPORTS ===\n",
            menu,
            ["1", "2", "3", "4", "5", "r"]
        )
        return choix

    def show_select_in_list(self, list_data, name):
        """
        Méthode qui permet de récuper une valeur dans une liste.
        :param self: l'instance du ReportsView.
        :type self: <class 'ReportsView'>.
        :param list_data: liste de donnée.
        :type list_data: list <X>
        :param name: le nom à afficher.
        :type name: str
        :return: un élément choisi par l'utilisateur.
        :rtype: X
        """
        return self.select_one_in_list(list_data, name)
