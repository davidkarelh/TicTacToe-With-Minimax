import math, random
from Board import Board
from Player import Player


class Robot(Player):
    # totalMove = 0

    def __init__(self, name : str):
        super().__init__(name)
    
    def move(self, board : Board, playerNumber : int) -> bool:
        # self.totalMove = 0
        if (board.getNumberOfEmptyCell() == 9):
            temp = random.randint(0, 8)
            board.setCell(temp, playerNumber)
            print(f"{self.name} select cell {temp}.")
            return False

        maxScore = -math.inf
        maxIdx = 0
        alpha = -math.inf
        beta = math.inf

        for idx in board.getEmptyCellIndexList():
            # self.totalMove += 1
            if (board.setCellAndCheckWin(idx, playerNumber)):
                # print(f"Total move =  {self.totalMove}.")
                print(f"{self.name} select cell {maxIdx}.")
                return True

            temp = self.__miniMax(board, board.getNumberOfEmptyCell(), alpha, beta, False, -1 if playerNumber == 1 else 1)

            if (temp > maxScore):
                maxScore = temp
                maxIdx = idx
            
            alpha = max(alpha, temp)

            if (beta <= alpha):
                break

            board.setCell(idx, 0)

        # print(f"Total move =  {self.totalMove}.")
        print(f"{self.name} select cell {maxIdx}.")
        return board.setCellAndCheckWin(maxIdx, playerNumber)
    
    def __miniMax(self, board : Board, depth : int, alpha : float, beta : float, maximizing : bool, playerNumber : int):
        # self.totalMove += 1

        if (depth == 0):
            return 0

        if (maximizing):
            score = -math.inf
            for idx in board.getEmptyCellIndexList():
                if (not board.setCellAndCheckWin(idx, playerNumber)):
                    temp = self.__miniMax(board, depth - 1, alpha, beta, False, -1 if playerNumber == 1 else 1)
                    score = max(temp, score)
                    alpha = max(alpha, temp)
                else:
                    temp = (board.getNumberOfEmptyCell() + 1)
                    score = max(temp, score)
                    alpha = max(alpha, temp)
                
                board.setCell(idx, 0)

                if (beta <= alpha):
                    break

            return score

        else:
            score = math.inf
            for idx in board.getEmptyCellIndexList():
                if (not board.setCellAndCheckWin(idx, playerNumber)):
                    temp = self.__miniMax(board, depth - 1, alpha, beta, True, -1 if playerNumber == 1 else 1)
                    score = min(temp, score)
                    beta = min(beta, temp)
                else:
                    temp = (board.getNumberOfEmptyCell() + 1) * -1
                    score = min(temp, score)
                    beta = min(beta, temp)

                board.setCell(idx, 0)

                if (beta <= alpha):
                    break

            return score
