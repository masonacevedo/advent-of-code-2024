import sys


def line_is_safe_without_removal(line):
#     print(line)
    if sorted(line, reverse=True) != line and sorted(line, reverse=False) != line:
#         print("1")
        return False

    diffs = [abs(a-b) for a,b in zip(line[0:-1], line[1:])]

    if max(diffs) > 3:
#         print('2')
        return False

    if min(diffs) < 1:
#         print('3')
        return False

#     print(4)
    return True

def line_is_safe_with_removal(line):
    line_variants = [line[0:i]+line[i+1:] for i in range(0, len(line))]
    safety_statuses = [line_is_safe_without_removal(l) for l in line_variants]
    return any(safety_statuses)

def main(file_name):
    with open(file_name) as file_handle:
        lines = file_handle.readlines()

    clean_lines = [line.replace("\n","") for line in lines]
    data = map(lambda l: [int(e) for e in l], [line.split(" ") for line in clean_lines])


    safe_data = list(filter(lambda line: line_is_safe_with_removal(line), data))
    return len(safe_data)



if __name__ == "__main__":
    print(main(sys.argv[1]))