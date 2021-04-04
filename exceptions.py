"""
Custom game exceptions
"""

from datetime import datetime


class GameOver(Exception):
    """
        Saving score at the end of the game
    """

    def __init__(self, player):
        self.player = player
        self.scores(player)

    @staticmethod
    def scores(player):
        """
        Writing and print result of player
        :param player: player object
        :return: Name, score and time of player
        """
        with open('scores.txt', 'a') as scores:
            scores.write(f'{player.name} | score: {player.score} | '
                         f'{str(datetime.now().replace(microsecond=0))} \n')
        print(f'{player.name}, your score: {player.score}')


class EnemyDown(Exception):
    """
    Exception when enemy down
    """
