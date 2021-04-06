"""
Custom game exceptions
"""

from datetime import datetime


class GameOver(Exception):
    """
        Saving score at the end of the game
    """

    @staticmethod
    def scores(name, score):
        """
        Writing and print result of player
        :param name: player name
        :param score: player score
        :return: Name, score and time of player
        """

        with open('scores.txt', 'a') as scores:
            scores.write(f'{name} | score: {score} | '
                         f'{str(datetime.now().replace(microsecond=0))}\n')
        print(f'{name}, your score: {score}')


class EnemyDown(Exception):
    """
    Exception when enemy down
    """
