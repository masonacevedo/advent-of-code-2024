import sys
import copy

def countXMASOccurences(row):
#     print("row:", row)
    if len(row) < 4:
        return 0

    count = 0
    for index in range(0, len(row)-3):
        if row[index:index+4] == "XMAS":
            count += 1

#     print("count:", count)
    return count

def horizCount(table):
    count = 0
    for row in table:
        count += countXMASOccurences(row)
        count += countXMASOccurences("".join(list(reversed(row))))
    return count

def vertCount(table):
#     print(table)
    count = 0
    rows = [[table[i][j] for i in range(0, len(table))] for j in range(0, len(table[0]))]

#     rows = [[table[j][i] for i in range(0, len(table))] for j in range(0, len(table))]
    for row in rows:
        count += countXMASOccurences("".join(row))
        count += countXMASOccurences("".join(list(reversed(row))))
    return count


def calculateNextCoord(coord, table):
    y,x = copy.deepcopy(coord)
    if (y < 0 or y >= len(table)):
        return None
    if (x < 0 or x >= len(table[0])):
       return None

    return [y-1, x+1]

def diagFromStartCoord(coord, table):
    result = []
    currentCoord = copy.deepcopy(coord)
    while currentCoord:
        result.append(currentCoord)
        currentCoord = calculateNextCoord(currentCoord, table)
    return result[:-1]


def diagCount(table):
    count = 0
    # careful not to double count diagStartCoords!
    diagStartCoords = [[i, 0] for i in range(0, len(table)-1)] + [[len(table)-1, i] for i in range(0, len(table[0]))]
#     print("diagStartCoords", diagStartCoords)
    diagsAsCoords = [diagFromStartCoord(coord, table) for coord in diagStartCoords]




    diagsAsEntries = [[table[coord[0]][coord[1]] for coord in diagAsCoord] for diagAsCoord in diagsAsCoords]

    for diag in diagsAsEntries:
#         print(diag)
#         input()
        forwardResult = countXMASOccurences("".join(diag))
        reverseResult = countXMASOccurences("".join(list(reversed(diag))))

        if forwardResult > 0:
#             print("diag:", diag)
#             print("forwardResult:", forwardResult)
#             print()
            count += forwardResult

        if reverseResult > 0:
#             print("diag:", diag)
#             print("reverseResult:", reverseResult)
#             print()
            count += reverseResult


    return count

def main(file_name):
    with open(file_name) as file_handle:
        lines = file_handle.readlines()
    table = [line.replace("\n","") for line in lines]
    flipped_table = ["".join(list(reversed(row))) for row in table]
    print("horizCount(table):", horizCount(table))
    print("vertCount(table):", vertCount(table))
    print("diagCount(table):", diagCount(table))
    print("diagCount(flipped_table):", diagCount(flipped_table))


    return horizCount(table) + vertCount(table) + diagCount(table) + diagCount(flipped_table)



if __name__ == "__main__":
    print(main(sys.argv[1]))
