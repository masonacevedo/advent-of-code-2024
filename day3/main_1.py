import sys

def getNumsToMul(line):
#     print("line:", line)
    if line[0:3] != 'mul':
#         print("1")
        return None

    if line[3] != "(":
#         print("2")
        return None

    closeParenIndex = line.index(")")
    subString = line[4:closeParenIndex]

    subStringSplitByComma = subString.split(",")
    if len(subStringSplitByComma) != 2:
#         print("3")
        return None

    if (subStringSplitByComma[0].isdigit()) and (subStringSplitByComma[1].isdigit()):
#         print("4")
        return subStringSplitByComma

#     print("5")



def extractMuls(line):
    muls = []
    enabled = True
    for index, (char1, char2, char3, char4, char5, char6, char7) in enumerate(zip(line[0:-6], line[1:-5], line[2:-4], line[3:-3], line[4:-2], line[5:-1], line[6:])):
        if char1+char2+char3+char4 == 'do()':
            enabled = True
        if char1+char2+char3+char4+char5+char6+char7 == "don't()":
            print("disabling")
            enabled = False

        if (char1, char2, char3) == ('m','u','l') and enabled:
            result = getNumsToMul(line[index:])
            if (result):
                muls.append(result)

    return muls


def main(file_name):
    with open(file_name) as file_handle:
        line = file_handle.read()

    muls = extractMuls(line)

    return sum([int(x)*int(y) for x,y in muls])



if __name__ == "__main__":
    print(main(sys.argv[1]))
