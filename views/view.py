import re


class View:

    """
            classe qui permet de gérer la vue .

            Methodes:
                def affichage_menu(self, titre, choix, donnees_valide):
                def input_int(self, texte, defaut_value= None):
                def input_str(self, texte):
                def input_id(self, texte):
                def input_date(self, texte):
                def select_many_in_list(self, listdata, nb, name_element):
                def select_one_in_list(self, listdata, name_element):
    """

    def affichage_menu(self, titre, choix, donnees_valide):
        """
        Méthode qui permet d'afficher le menu et demander le choix de l'utlisateur.
        :param self: l'instance du View.
        :type self: <class 'View'>
        :param titre: titre du menu.
        :type titre: str
        :param choix: la liste des entrées du menu.
        :type choix: list < str >
        :param donnees_valide: la liste des choix valide.
        :type donnees_valide: list < str >
        :return: retourne le choix de l'utilisateur.
        :rtype: str
        """
        selection_option = None
        while selection_option not in donnees_valide:
            if selection_option is not None:
                print("Il y a une erreur dans ta saisie")

            print(titre)
            for valeur in choix:
                print(valeur)
            selection_option = input(
                "Selectionne une option parmis les propositions : "
            )
        return selection_option

    def input_int(self, texte, defaut_value=None):
        """
        Méthode qui permet de saisir un entier.
        :param self: l'instance du View.
        :type self: <class 'View'>
        :param texte: permet d'afficher du texte lors de la saisie de l'entier.
        :type texte: str
        :param defaut_value: permet de retourner une valeur par défaut.
        :type defaut_value: str
        :return: retourne une valeur
        :rtype: int / None
        """
        # tester que l'utilisateur ne rentre que des lettres.
        while True:
            saisie = input(texte)
            # il a rien saisie, et il n'y a pas de valeur par defaut
            if not saisie and defaut_value is None:
                print("Erreur de saisi")
            # il a fait une saisie, on verifie que c'est un nombre positif
            elif saisie.isnumeric() and int(saisie) >= 0:
                return int(saisie)
            # il a rien saisie, et il y a une valeur par defaut
            elif not saisie and defaut_value:
                return defaut_value

    def input_str(self, texte):
        """
        Méthode qui permet de saisir une chaine de caractère.
        :param self: l'instance du View.
        :type self: <class 'View'>
        :param texte: permet d'afficher du texte lors de la saisie d'une chaine de caractère.
        :type texte: str
        :return: retourne une valeur
        :rtype: str
        """
        # tester que l'utilisateur ne rentre que des lettres.
        saisie = ""
        while not saisie:
            saisie = input(texte)
            if not saisie:
                print("Erreur de saisi")
        return saisie

    # teste si la saisie correspond à la "regex AB12345".
    def input_id(self, texte):
        """
        Méthode qui permet de saisir que c'est un identifiant national.
        :param self: l'instance du View.
        :type self: <class 'View'>
        :param texte: permet d'afficher du texte lors de la saisie d'une chaine de caractère.
        :type texte: str
        :return: retourne un idenfiant nationmal.
        :rtype: str
        """
        while True:
            saisie = input(texte)
            if re.match("^[a-zA-Z]{2}[0-9]{5}$", saisie):
                return saisie.upper()
            else:
                print("\n")
                print("La saisie n'est pas bonne, merci de recommencer.")
                print("\n")

    def input_date(self, texte):
        """
        Méthode qui permet de saisir une date.
        :param self: l'instance du View.
        :type self: <class 'View'>
        :param texte: permet d'afficher un texte pour l'utilisateur.
        :type texte: str
        :return: Retourne une date.
        :rtype: str
        """
        while True:
            saisie = input(texte)
            if re.match("(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)[0-9]{2}$", saisie):
                return saisie
            else:
                print("Date de naissance invalide")

    def select_many_in_list(self, listdata, nb, name_element):
        """
        Methode qui permet de faire des selections multiples dans une liste.
        :param self: l'instance du View.
        :type self: <class 'View'>.
        :param listdata: liste des données.
        :type listdata: list < X >.
        :param nb: nombre de donnés a selectionner.
        :type nb: int.
        :param name_element: le nom du type délément a faire afficher.
        :type name_element: str.
        :return: retourne la liste sélectionné.
        :rtype: list < X >
        """
        if len(listdata) == 0:
            return []

        id_selected = []  # list des id selectionner
        liste_elem_enregistres = []  # list des elements selectionner
        while len(id_selected) < nb:
            print("====================================")
            for idx, elem in enumerate(listdata):
                if idx not in id_selected:
                    print(f"[{idx+1}]", elem)
            elem_id_select = self.input_int(
                f"Selectionner ... (encore {nb - len(id_selected)} {name_element} a selectionner): ")
            elem_id_select -= 1
            if elem_id_select in range(len(listdata)) and elem_id_select not in id_selected:
                liste_elem_enregistres.append(listdata[elem_id_select])
                id_selected.append(elem_id_select)
        return liste_elem_enregistres

    def select_one_in_list(self, listdata, name_element):
        """
        Methode qui permet de faire une selection dans une liste.
        :param self: l'instance du View.
        :type self: <class 'View'>.
        :param listdata: liste des données.
        :type listdata: list < X >.
        :param name_element: le nom du type délément a faire afficher.
        :type name_element: str.
        :return: retourne l'élément sélectionné.
        :rtype: list < X >
        """
        if len(listdata) == 0:
            return None
        while True:
            for idx, elem in enumerate(listdata):
                print(f"[{idx+1}]", elem)
            elem_id_select = self.input_int(f"Selectionner un {name_element}: ")
            elem_id_select -= 1
            if elem_id_select in range(len(listdata)):
                return listdata[elem_id_select]
