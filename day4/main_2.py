import sys
import copy

known_squares = [
[['M','.','S'],
['.','A','.'],
['M','.','S'],],

[['S','.','S'],
['.','A','.'],
['M','.','M'],],

[['S','.','M'],
['.','A','.'],
['S','.','M'],],

[['M','.','M'],
['.','A','.'],
['S','.','S'],],

]

def matches(small_table, square):
    return ((square[0][0] == small_table[0][0])
    and (square[0][2] == small_table[0][2])
    and (square[2][0] == small_table[2][0])
    and (square[2][2] == small_table[2][2])
    and (square[1][1] == small_table[1][1]))

def isXmasSquare(small_table):
    for square in known_squares:
        if matches(small_table, square):
            return True
    return False

def smallTablesFromTable(table):
    all_smalls = []
    for row in range(0, len(table)-2):
        for col in range(0, len(table[0])-2):
            small_table = [[table[row][col],   table[row][col+1],   table[row][col+2]],
                           [table[row+1][col], table[row+1][col+1], table[row+1][col+2]],
                           [table[row+2][col], table[row+2][col+1], table[row+2][col+2]]]
            all_smalls.append(small_table)

    return all_smalls

def main(file_name):
    with open(file_name) as file_handle:
        lines = file_handle.readlines()
    table = [line.replace("\n","") for line in lines]

#     print(list(filter(isXmasSquare, smallTablesFromTable(table))))

    ans = 0
    total = 0
    for smallTable in smallTablesFromTable(table):
#         for row in smallTable:
#             print(row)
#         input()
        total+= 1
        if isXmasSquare(smallTable):
#             print("match!")
            ans += 1

#     print("total:", total)

    return ans


if __name__ == "__main__":
    print(main(sys.argv[1]))
