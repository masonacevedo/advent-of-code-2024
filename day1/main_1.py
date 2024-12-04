import sys

def main(file_name):
    with open(file_name) as file_handle:
        lines = file_handle.readlines()

    clean_lines = [line.replace("\n","") for line in lines]

    list_1 = [int(line.split(" ")[0]) for line in clean_lines]
    list_2 = [int(line.split(" ")[-1]) for line in clean_lines]


#     for num1, num2 in zip(list_1, list_2):
#         print(num1, num2)
#         input()

    list_1_sorted = sorted(list_1)
    list_2_sorted = sorted(list_2)


    differences = [abs(num1-num2) for num1,num2 in zip(list_1_sorted, list_2_sorted)]
    return sum(differences)


if __name__ == "__main__":
    print(main(sys.argv[1]))