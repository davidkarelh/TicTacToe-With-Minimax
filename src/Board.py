from itertools import chain


class Board:
    __mapIntToCharacter = {1 : 'X', -1 : 'O', 0 : "-"}

    def __init__(self) -> None:
        self.__board = [0 for i in range(9)]
    
    def show(self):
        for i in range(len(self.__board)):
            element = self.__board[i]
            print(self.__mapIntToCharacter[element] + ("|" if ((i + 1) % 3 != 0) else ""), end="" if ((i + 1) % 3 != 0) else "\n")
    
    def isValidMove(self, i : int):
        return self.__board[i] == 0
    
    def getNumberOfEmptyCell(self):
        ret = 0

        for element in self.__board:
            if (element == 0):
                ret += 1

        return ret
    
    def getEmptyCellIndexList(self):
        ret = []

        for i in range(len(self.__board)):
            if (self.__board[i] == 0):
                ret.append(i)

        return ret
    
    def setCell(self, i : int, element : int):
        self.__board[i] = element
    
    def setCellAndCheckWin(self, i : int, element : int):
        self.setCell(i, element)

        winCondition = False
        rowCheck = [0, 1, 2]
        j = 0
        while not winCondition and j <= 2:
            if (i in rowCheck):
                winCondition = self.__board[rowCheck[0]] == element and self.__board[rowCheck[1]] == element and self.__board[rowCheck[2]] == element

            if not winCondition:
                for idx in range(len(rowCheck)):
                    rowCheck[idx] += 3

            j += 1
        
        if (not winCondition):
            columnCheck = [0, 3, 6]
            j = 0
            while not winCondition and j <= 2:
                if (i in columnCheck):
                    winCondition = self.__board[columnCheck[0]] == element and self.__board[columnCheck[1]] == element and self.__board[columnCheck[2]] == element

                if not winCondition:
                    for idx in range(len(columnCheck)):
                        columnCheck[idx] += 1

                j += 1

        if (not winCondition):
            if (i in (0, 4, 8)):
                winCondition = self.__board[0] == element and self.__board[4] == element and self.__board[8] == element
            
            if (i in (2, 4, 6)):
                winCondition = self.__board[2] == element and self.__board[4] == element and self.__board[6] == element

        return winCondition