from abc import abstractmethod
from Board import Board


class Player:
    name : str

    def __init__(self, name : str):
        self.name = name

    @abstractmethod
    def move(self, board : Board, playerChar : int) -> bool:
        pass