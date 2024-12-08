import sys
import copy

def isUpdateCorrect(update, rule):
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

def reorderOneRule(update, rule):
    earlyNum, lateNum = rule
    if not(earlyNum in update) or not(lateNum in update):
        return

    earlyNumIndex = update.index(earlyNum)
    lateNumIndex = update.index(lateNum)

    if earlyNumIndex > lateNumIndex:
        temp = update[earlyNumIndex]
        update[earlyNumIndex] = update[lateNumIndex]
        update[lateNumIndex] = temp


def reorderAllRules(update, rules):
    answer = copy.deepcopy(update)
    # given an update,
    # we loop through the rules, and 
    # we change the update whenever
    # the update violates some rule.
    # The smart thing to do would be 
    # to loop through the rules and change
    # the update as long as the update is 
    # invalid.
    # The dumb thing to do is just loop
    # through the rules a lot, then increase
    # the number, and if the result doesn't change,
    # you know you've probably looped enough.
    # that's what we do here. 
    for i in range(0, 100):
        for rule in rules:
            reorderOneRule(answer, rule)
    return answer

def parseRule(ruleString):
    return ruleString.split("|")

def parseUpdate(update):
    return update.split(",")

def main(file_name):
    with open(file_name) as file_handle:
        lines = file_handle.readlines()
    table = [line.replace("\n","") for line in lines]
    ruleStrings = []
    updateStrings = []
    pastRulesSection = False

    for line in table:
        if pastRulesSection:
            updateStrings.append(line)
        else:
            ruleStrings.append(line)
        if line == '':
            pastRulesSection = True
    ruleStrings.pop()
    
    rules = list(map(parseRule, ruleStrings))
    updates = list(map(parseUpdate, updateStrings))


    newRules = []
    for update in updates:
        result = reorderAllRules(update, rules)
        if result == update:
            pass
        else:
            newRules.append(result)


    middleNums = [int(newRule[len(newRule)//2]) for newRule in newRules]
    return sum(middleNums)

if __name__ == "__main__":
    print(main(sys.argv[1]))
