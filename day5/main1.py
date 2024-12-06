import sys
import copy

def isUpdateCorrect(update, rule):
    earlyNum, lateNum = rule.split("|")
    nums = update.split(",")
    if not(earlyNum in update) or not(lateNum in update):
        return True

    earlyNumIndex = nums.index(earlyNum)
    lateNumIndex = nums.index(lateNum)
    return earlyNumIndex < lateNumIndex

def validUpdate(update, rules):
    for rule in rules:
        if not(isUpdateCorrect(update, rule)):
            return False
    return True

def main(file_name):
    with open(file_name) as file_handle:
        lines = file_handle.readlines()
    table = [line.replace("\n","") for line in lines]
    rules = []
    updates = []
    pastRulesSection = False

    for line in table:
        if pastRulesSection:
            updates.append(line)
        else:
            rules.append(line)
        if line == '':
            pastRulesSection = True
    rules.pop()

    validUpdates = list(filter(lambda f: validUpdate(f, rules), updates))

    validUpdatesAsList = [updateString.split(",") for updateString in validUpdates]
#     for update in validUpdatesAsList:
#         print(update)

    middleNums = [int(update[len(update)//2]) for update in validUpdatesAsList]

    return sum(middleNums)



#     return horizCount(table) + vertCount(table) + diagCount(table) + diagCount(flipped_table)



if __name__ == "__main__":
    print(main(sys.argv[1]))
