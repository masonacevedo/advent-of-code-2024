import sys

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
        print(row)
        input()
        count += countXMASOccurences("".join(row))
        count += countXMASOccurences("".join(list(reversed(row))))
    return count

# def diagCount(table):
#     diag1 = [table[0][0]]
#     d2 = [table[1][0] , table[0][1]]
#     d3 = [table[2][0] , [1][1], [0][2]]
#
#     diags = [[table[][] for ] for ]


def main(file_name):
    with open(file_name) as file_handle:
        lines = file_handle.readlines()
    table = [line.replace("\n","") for line in lines]

#     return horizCount(table) + vertCount(table) + diagCount(table)
    return horizCount(table) + vertCount(table)



if __name__ == "__main__":
    print(main(sys.argv[1]))
