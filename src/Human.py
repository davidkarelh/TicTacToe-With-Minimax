from Board import Board
from Player import Player


class Human(Player):

    def __init__(self, name : str):
        super().__init__(name)
    
    def move(self, board : Board, playerNumber : int) -> bool:
        while True:
            try:
                selectedCell = int(input("Select a cell ( 0 - 8 ): "))
                if (selectedCell < 0 or selectedCell > 8):
                    raise Exception("Input invalid. Enter in range of 0 to 8.")
                
                if (not board.isValidMove(selectedCell)):
                    raise Exception("Input invalid. Cell is already occupied.")
                
                return board.setCellAndCheckWin(selectedCell, playerNumber)
                
            except Exception as exc:
                print()
                print(exc)