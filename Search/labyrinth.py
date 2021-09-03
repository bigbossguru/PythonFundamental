from enum import Enum
from typing import List, NamedTuple, Optional
from random import uniform
from generic_search import Node, node_to_path, dfs
from random import randint

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
    def __init__(self, rows: int = 10, columns: int = 10, rarity: float = 0.2,
                start: LabyrinthLocation = LabyrinthLocation(0,0), 
                goal: LabyrinthLocation = LabyrinthLocation(9,9)) -> None:
        self._rows = rows
        self._columns = columns
        self.start = start
        self.goal = goal
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        self._randomly_fill(rows, columns, rarity)
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL
    
    def _randomly_fill(self, rows: int, columns: int, rarity: float) -> None:
        for row in range(rows):
            for column in range(columns):
                if uniform(0, 1.0) < rarity:
                    self._grid[row][column] = Cell.BLOCKED
    
    def goal_test(self, labloc: LabyrinthLocation) -> bool:
        return labloc == self.goal

    def successors(self, labloc: LabyrinthLocation) -> List[LabyrinthLocation]:
        locations: List[LabyrinthLocation] = []
        if labloc.row+1 < self._rows and self._grid[labloc.row+1][labloc.column] != Cell.BLOCKED:
            locations.append(LabyrinthLocation(labloc.row+1, labloc.column))
        if labloc.row-1 >= 0 and self._grid[labloc.row-1][labloc.column] != Cell.BLOCKED:
            locations.append(LabyrinthLocation(labloc.row-1, labloc.column))
        if labloc.column+1 < self._columns and self._grid[labloc.row][labloc.column+1] != Cell.BLOCKED:
            locations.append(LabyrinthLocation(labloc.row, labloc.column+1))
        if labloc.column-1 >= 0 and self._grid[labloc.row][labloc.column-1] != Cell.BLOCKED:
            locations.append(LabyrinthLocation(labloc.row, labloc.column-1))
        return locations
    
    def mark(self, path: List[LabyrinthLocation]) -> None:
        for labloc in path:
            self._grid[labloc.row][labloc.column] =  Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL
    
    def clear(self, path: List[LabyrinthLocation]):
        for labloc in path:
            self._grid[labloc.row][labloc.column] =  Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL
    
    def __str__(self) -> str:
        output: str = ""
        for row in self._grid:
            output += "".join([c.value for c in row]) + '\n'
        return output

if __name__ == "__main__":
    coords = [(randint(0,20), randint(0,60)) for _ in range(2)]
    labyrinth: Labyrinth = Labyrinth(rows=20, columns=60, start=LabyrinthLocation(*coords[0]), goal=LabyrinthLocation(*coords[1]), rarity=0.2)
    # print(labyrinth)

    solution1: Optional[Node[LabyrinthLocation]] = dfs(labyrinth.start, labyrinth.goal_test, labyrinth.successors)

    if solution1 is None:
        print("\tNo solution found using depth-first search!\n".upper())
    else:
        path1: List[LabyrinthLocation] = node_to_path(solution1)
        labyrinth.mark(path1)
        print(labyrinth)
        labyrinth.clear(path1)
        print("\tGreat, we have path to our goal!\n".upper())