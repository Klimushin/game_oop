"""
Contains the player, the enemy and the show scores table classes
"""

from random import randint

import settings
from exceptions import GameOver, EnemyDown


class Enemy:
    """
    The enemy class
    """

    def __init__(self, level=1):
        """
        Construction the name and level of the enemy
        :param level: level enemy
        """
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """
        Method for generate random int number
        :return: number from 1 to 3
        """
        return randint(1, 3)

    def decrease_lives(self):
        """
        Method for decrease lives from enemy and add to player
        :return: exception EnemyDown
        """
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown


class Player:
    """
    The player class
    """

    def __init__(self, name):
        """
        Construction the name player
        Prints a greeting.
        :param name: player name
        """
        print(f"Hello, {name}, lets go!!! \n")
        self.name = name
        self.lives = settings.PLAYER_LIVES
        self.score = 0

    @staticmethod
    def fight(attack, defense):
        """
        Method for fight.
        :return result of round
        """
        if attack == defense:
            return 0
        elif attack == settings.WIZARD and defense == settings.WARRIOR:
            return 1
        elif attack == settings.WARRIOR and defense == settings.ROBBER:
            return 1
        elif attack == settings.ROBBER and defense == settings.WIZARD:
            return 1
        else:
            return -1

    def decrease_lives(self):
        """
        Method for decrease lives from player
        :return: exception Game over
        """
        self.lives -= 1
        if self.lives == 0:
            raise GameOver(self)

    def attack(self, enemy):
        """
        Method for determining the result of a player's attack
        :param enemy: Enemy
        :return: message with result of attack
        """
        attack = int(input("Whu Attack? : 1 - WIZARD, 2 - WARRIOR, 3 - ROBBER: \n"))
        enemy_defense = enemy.select_attack()
        result = self.fight(attack=attack, defense=enemy_defense)
        if result == 0:
            print("It's a draw!")
        elif result == 1:
            print("You attacked successfully!")
            enemy.decrease_lives()
            self.score += 1
        else:
            print("You missed!")
            self.decrease_lives()

    def defense(self, enemy):
        """
        Method for determining the result of a player's defence
        :param enemy: Enemy
        :return: message with result of defence
        """
        defense = int(input("Whu Defense?: 1 - WIZARD, 2 - WARRIOR, 3 - ROBBER: \n "))
        enemy_attack = enemy.select_attack()
        result = self.fight(attack=enemy_attack, defense=defense)
        if result == 0:
            print("It's a draw!")
        elif result == 1:
            print("Enemy won!")
            self.decrease_lives()
        else:
            print("Defense successful!")
