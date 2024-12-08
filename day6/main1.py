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

def updateGrid(grid, direction):
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if grid[row][col] == "^":
                currentPos = [row,col]
    
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

def main(file_name):
    with open(file_name) as file_handle:
        lines = file_handle.readlines()
    grid = [list(line.replace("\n","")) for line in lines]
    # for row in grid:
    #     print("".join(row))
    # input()

   
    direction = Direction.NORTH
    while(True):
        # print("before")
        # print(direction)
        # for row in grid:
        #     print("".join(row))
        try:
            direction = updateGrid(grid, direction)
        except Exception as e:
            break
        # print()
        # print()
        # print("after")
        # print(direction)
        # for row in grid:
        #     print("".join(row))

        # input()
    
    # for row in grid:
    #     print("".join(row))

    xCounts = [row.count("X") for row in grid]
    return sum(xCounts)+1

if __name__ == "__main__":
    print(main(sys.argv[1]))
