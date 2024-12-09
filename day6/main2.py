import sys
import copy

from enum import Enum

class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

# # Example of using the enum
# selected_color = Color.RED

# print(selected_color)       # Output: Color.RED
# print(selected_color.value) # Output: 'red'

def updateGridWithPrints(grid, direction):
    for row in grid:
        print(row)
    input()

    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if grid[row][col] == "^":
#                 print("found start")
                currentPos = [row,col]
#     print("grid:", grid)
#     print("getting row and col")
    row, col = currentPos
    if direction == Direction.NORTH:
        if grid[row-1][col] == "#":
            direction = Direction.EAST
            grid[row][col+1] = "^"
        else:
            grid[row-1][col] = "^"
    elif direction == Direction.SOUTH:
        if grid[row+1][col] == "#":
            direction = Direction.WEST
            grid[row][col-1] = "^"
        else:
            grid[row+1][col] = "^"
    elif direction == Direction.EAST:
        if grid[row][col+1] == "#":
            direction = Direction.SOUTH
            grid[row+1][col] = "^"
        else:
            grid[row][col+1] = "^"
    elif direction == Direction.WEST:
        if grid[row][col-1] == "#":
            direction = Direction.NORTH
            grid[row-1][col] = "^"
        else:
            grid[row][col-1] = "^"

    grid[row][col] = "X"
    return direction

def updateGrid(grid, direction):
#     for row in grid:
#         print(row)
#     print()

    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if grid[row][col] == "^":
#                 print("found start")
                currentPos = [row,col]
#     print("grid:", grid)
#     print("getting row and col")
    row, col = currentPos
    if direction == Direction.NORTH:
        if grid[row-1][col] == "#":
            direction = Direction.EAST
            grid[row][col+1] = "^"
        else:
            grid[row-1][col] = "^"
    elif direction == Direction.SOUTH:
        if grid[row+1][col] == "#":
            direction = Direction.WEST
            grid[row][col-1] = "^"
        else:
            grid[row+1][col] = "^"
    elif direction == Direction.EAST:
        if grid[row][col+1] == "#":
            direction = Direction.SOUTH
            grid[row+1][col] = "^"
        else:
            grid[row][col+1] = "^"
    elif direction == Direction.WEST:
        if grid[row][col-1] == "#":
            direction = Direction.NORTH
            grid[row-1][col] = "^"
        else:
            grid[row][col-1] = "^"
    
    grid[row][col] = "X"
    return direction

def loops(grid, direction):
    n = 1000
    i = 0
    while(i < n):
        i += 1
        try:
            direction = updateGrid(grid, direction)
        except IndexError:
            return False
    return True


def loopsWithPrings(grid, direction):
    n = 1000
    i = 0
    while(i < n):
        i += 1
        print("about to update")
        direction = updateGridWithPrints(grid, direction)
        print("updated")
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
#     return loops(grid, Direction.NORTH)


    potentialGrids = generatePotentialGrids(grid)

    for g in potentialGrids:

        if loops(g, Direction.NORTH):
            for row in g:
                print(row)
            input()

            print("found a looper")
            loopsWithPrings(g, Direction.NORTH)
            input()


if __name__ == "__main__":
    print(main(sys.argv[1]))
