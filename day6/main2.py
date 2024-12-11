import sys
import copy
import pprint
from enum import Enum

class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

myDict = {
    Direction.NORTH: Direction.EAST,
    Direction.EAST: Direction.SOUTH,
    Direction.SOUTH: Direction.WEST,
    Direction.WEST: Direction.NORTH,
}

def turn90(direction):
    return myDict.get(direction)    

def nextPos(currentPos, direction):
    row, col = currentPos 

    if direction == Direction.NORTH:
        return [row-1, col]
    elif direction == Direction.SOUTH:
        return [row+1, col]
    elif direction == Direction.WEST:
        return [row, col-1]
    elif direction == Direction.EAST:
        return [row, col+1]

def updateGrid(grid, direction, currentPos):
    # print("currentPos, beginning:", currentPos)
    row, col = currentPos
    nextRowForwards, nextColForwards = nextPos(currentPos, direction)
	
    if grid[nextRowForwards][nextColForwards] == "#":
        direction = turn90(direction)
        nextRowTurned, nextColTurned = nextPos(currentPos, direction)
        if grid[nextRowTurned][nextColTurned] == "#":
            direction = turn90(direction)
            nextRowTurned, nextColTurned = nextPos(currentPos, direction)
        currentPos[0] = nextRowTurned
        currentPos[1] = nextColTurned
    else:
        currentPos[0] = nextRowForwards
        currentPos[1] = nextColForwards

    grid[currentPos[0]][currentPos[1]] = "^"
    
    grid[row][col] = "X"
    # print("currentPos, ending:", currentPos)
    return direction

def nextStepInBounds(grid, direction, currentPosition):
    row, col = currentPosition
    if direction == Direction.NORTH:
        return (row != 0)
    elif direction == Direction.SOUTH:
        return (row != len(grid)-1)
    elif direction == Direction.WEST:
        return (col != 0)
    elif direction == Direction.EAST:
        return (col != len(grid)-1)
    raise Exception("Fill this in")

def loops(grid, direction, position):
    n = 10000
    i = 0
    while(i < n) and nextStepInBounds(grid, direction, position):
        i += 1
        direction = updateGrid(grid, direction, position)
        # pprint.pprint(grid)
        # input()

    return nextStepInBounds(grid, direction, position)

def generatePotentialGrids(grid):
    ans = []
    for rowIndex in range(0, len(grid)):
        for colIndex in range(0, len(grid[0])):
            if grid[rowIndex][colIndex] == ".":
                newGrid = copy.deepcopy(grid)
                newGrid[rowIndex][colIndex] = "#"
                ans.append(newGrid)

    return ans

def findStartingPositino(grid):
    for rowIndex in range(0, len(grid)):
        for colIndex in range(0,len(grid[0])):
            if grid[rowIndex][colIndex] == "^":
                return [rowIndex, colIndex]
    raise Exception("it shouldn't be possible to get here")

def main(file_name):
    with open(file_name) as file_handle:
        lines = file_handle.readlines()
    grid = [list(line.replace("\n","")) for line in lines]


    potentialGrids = generatePotentialGrids(grid)
    count = 0
    for grid in potentialGrids:
        startingPosition = findStartingPositino(grid)
        if loops(grid, Direction.NORTH, startingPosition):
            count += 1

    return count



if __name__ == "__main__":
    print(main(sys.argv[1]))
