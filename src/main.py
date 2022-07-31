from Game import Game
from Player import Player
from Human import Human
from Robot import Robot


def main():
    game = Game()

    player1 = Robot("Player 1")
    player2 = Human("Player 2")

    game.start(player1, player2)


if (__name__ == "__main__"):
    main()