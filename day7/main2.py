import sys
import copy
import pprint
from enum import Enum



def possiblyTrue(target, sequence):
    if len(sequence) == 1:
        return target == sequence[0]
    else:
        addSequence = [sequence[0]+sequence[1]] + sequence[2:]
        multSequence = [sequence[0]*sequence[1]] + sequence[2:]
        concatSequence = [int(str(sequence[0]) + str(sequence[1]))] + sequence[2:]
        addPossibility = possiblyTrue(target, addSequence)
        multPossibility = possiblyTrue(target, multSequence)
        concatPossibility = possiblyTrue(target, concatSequence)
        return (addPossibility or multPossibility or concatPossibility)

def parse(line):
    targetNumString, sequenceString = line.split(":")
    target = int(targetNumString)
    sequence = [int(s) for s in sequenceString.split(" ")[1:]]
    
    return target, sequence

def main(file_name):
    with open(file_name) as file_handle:
        lines = file_handle.readlines()
    clean_lines = [line.replace("\n","") for line in lines]
   
    sum = 0 
    for l in clean_lines:
        target, sequence = parse(l)
        if possiblyTrue(target, sequence):
            sum += target
    return sum
    

if __name__ == "__main__":
    print(main(sys.argv[1]))
