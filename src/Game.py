from Board import Board
from Player import Player


class Game:
    def __init__(self):
        self.__board = Board()
        self.__round = 1

    def start(self, 
        player1 : Player, # X -> 1
        player2 : Player # O -> -1
        ):

        # reset board
        self.__board = Board()
        self.__round = 1
        print("Game resetted.")

        playerWin = False
        while (not playerWin) and (self.__round <= 9):
            if (self.__round % 2 == 0):
                self.__printRound(player2)
                playerWin = player2.move(self.__board, -1)
            else:
                self.__printRound(player1)
                playerWin = player1.move(self.__board, 1)

            self.__round += 1
        
        print()
        if playerWin:
            self.__board.show()
            print(f"{player1.name if (self.__round % 2 == 0) else player2.name} Win!")
        else:
            self.__board.show()
            print("It's a draw!")
    
    def __printRound(self, currentPlayer : Player):
        print()
        self.__board.show()
        print(f"Current Player : {currentPlayer.name}")