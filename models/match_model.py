class MatchModel:
    """
    Class qui représente un match.
    ...

    Attributs:
    ----------
    player1: tuple
        une instance player et un nombre float.
    player2: tuple
        une instance player et un nombre float.

    Methodes:
    -------
    none

    """

    def __init__(self, player1, player2, score1=0.0, score2=0.0):
        """
        constructeur pour initialiser le modèle du match.

        Parameters
        ----------
        player1: instance
            player instance
        player2: instance
            player instance
        score1: float number
            score of player1
        score2: float number
            score of player2

        """

        self.player1 = (player1, score1)
        self.player2 = (player2, score2)
