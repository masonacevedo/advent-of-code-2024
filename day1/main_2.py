import sys

def main(file_name):
    with open(file_name) as file_handle:
        lines = file_handle.readlines()

    clean_lines = [line.replace("\n","") for line in lines]

    list_1 = [int(line.split(" ")[0]) for line in clean_lines]
    list_2 = [int(line.split(" ")[-1]) for line in clean_lines]

    frequencies = [list_2.count(num) for num in list_1]

    multiples = [num * freq for num, freq in zip(list_1, frequencies)]
    return sum(multiples)


if __name__ == "__main__":
    print(main(sys.argv[1]))