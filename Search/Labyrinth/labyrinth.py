from enum import Enum
from typing import List, NamedTuple
from random import uniform

class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

class LabyrinthLocation(NamedTuple):
    row: int
    column: int

class Labyrinth:
    def __init__(self, rows: int = 10, columns: int = 20, rarity: float = 0.2,
                start: LabyrinthLocation = LabyrinthLocation(0,0), 
                goal: LabyrinthLocation = LabyrinthLocation(9,19)) -> None:
        self.__rows = rows
        self.__columns = columns
        self.start = start
        self.goal = goal
        self.__grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        self.__randomly_fill(rows, columns, rarity)
        self.__grid[start.row][start.column] = Cell.START
        self.__grid[goal.row][goal.column] = Cell.GOAL
    
    def __randomly_fill(self, rows: int, columns: int, rarity: float) -> None:
        for row in range(rows):
            for column in range(columns):
                if uniform(0, 1.0) < rarity:
                    self.__grid[row][column] = Cell.BLOCKED
    
    def goal_test(self, labLoc: LabyrinthLocation) -> bool:
        return labLoc == self.goal
    
    def __str__(self) -> str:
        output: str = ""
        for row in self.__grid:
            output += "".join([c.value for c in row]) + '\n'
        return output

if __name__ == "__main__":
    labyrinth: Labyrinth = Labyrinth()
    print(labyrinth)