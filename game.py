"""
The main executable file in which the gameplay starts
"""
from exceptions import GameOver, EnemyDown
from models import Player, Enemy
from settings import ALL_COMMANDS


def play():
    """
    Input player names, input game commands and create player object and enemy object.
    Print scores table.
    :return: Result of game
    """
    player_name = input("Enter your name: \n")
    player = Player(name=player_name)
    level = 1
    enemy = Enemy(level=level)
    command = None
    while command not in ALL_COMMANDS:
        command = input('Enter "start" to start the game or "help" to see all commands.\n').lower()
        if command == "help":
            print(f"All commands: {', '.join(ALL_COMMANDS)}.")
        if command == 'show scores':
            with open('scores.txt', 'r') as scores:
                for lines in scores.readlines():
                    print(lines.replace('\n', ''))
        if command == "exit":
            raise KeyboardInterrupt

        if command == "start":
            while command:
                try:
                    player.attack(enemy)
                    print(f"Your lives: {player.lives} | Enemy lives: {enemy.lives} \n")
                    player.defense(enemy)
                    print(f"Your lives: {player.lives} | Enemy lives: {enemy.lives} \n")
                except EnemyDown:
                    level += 1
                    enemy = Enemy(level=level)
                    player.score += 5
                    print(f"You WON. Your score: {player.score}. lives: {level}")


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        print('Fuck. You Lose! (((')
    except KeyboardInterrupt:
        pass
    finally:
        print("Good bye!")
