import sys
import copy

from enum import Enum

class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

def updateGrid(grid, direction, currentPos):

	row, col = currentPos
	nextRowForwards, nextColForwards = nextPos(currentPos, direction)
	
	if itemAtLocation(grid, nextRowForwards, nextColForwards) == "#":
		direction = turn90(direction)
		nextRowTurned, nextColTurned = nextPos(currentPos, direction)
		currentPos = [nextRowTurned, nextColTurned] 
	else:
		currentPos = [nextRowForwards, nextColForwards]

	grid[row][col] = "X"
	return direction

def nextStepInBounds(grid, direction, currentPosition):
	raise Exception("Fill this in")

def loops(grid, direction):
    n = 1000
    i = 0
    while(i < n) and nextStepInBounds(grid, direction):
        i += 1
        try:
            direction, position = updateGrid(grid, direction)
        except IndexError:
            return False
    return True

def generatePotentialGrids(grid):
    ans = []
    for rowIndex in range(0, len(grid)):
        for colIndex in range(0, len(grid[0])):
            if grid[rowIndex][colIndex] == ".":
                newGrid = copy.deepcopy(grid)
                newGrid[rowIndex][colIndex] = "#"
                ans.append(newGrid)

    return ans

def main(file_name):
    with open(file_name) as file_handle:
        lines = file_handle.readlines()
    grid = [list(line.replace("\n","")) for line in lines]


    potentialGrids = generatePotentialGrids(grid)




if __name__ == "__main__":
    print(main(sys.argv[1]))
