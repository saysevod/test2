import random

MIN = 1
MAX = 50


def print_table(list_one):
    '''
    :param list_one:
    :return:
    '''

    for row in range(0, len(list_one)):
        print(' '.join(["{:4d}".format(x) for x in list_one[row]]))

    list_two = [sum([row[i] for row in list_one]) for i in range(0, len(list_one[0]))]
    print(' '.join(["{:4d}".format(x) for x in list_two]))
    return list_two


def sort_col(list_one):
    '''
    :param col:
    :return:
    '''
    for k in range(0,len(list_one[0])):
        for i in range(len(list_one) - 1, 0, -1):
            for j in range(0, i):
                if list_one[j][k] < list_one[j + 1][k]:
                    list_one[j][k], list_one[j + 1][k] = list_one[j + 1][k], list_one[j][k]


    for k in range(0,len(list_one[0])):
        if k % 2 != 0:
            for j in range(0,len(list_one) // 2):
                list_one[j][k], list_one[len(list_one) - 1 - j][k] = list_one[len(list_one) - 1 - j][k], list_one[j][k]
    return list_one
try:
    M = int(input('Input number more than 4, please: '))
except ValueError:
    print('Your number is not valid')
else:
    if M < 5:
        print("Number must be more than 4")
    else:
        list_one = [[random.randint(MIN, MAX) for i in range(1, M + 1)] for _ in range(1, M + 1)]
        print('Before sort')
        list_two = print_table(list_one)
        print("---")

        for i in range(len(list_two) - 1, 1, -1):
            for j in range(0, i):
                if list_two[j] > list_two[j + 1]:
                    list_two[j], list_two[j + 1] = list_two[j + 1], list_two[j]
                    for row in range(0, len(list_one)):
                        list_one[row][j], list_one[row][j + 1] = list_one[row][j + 1], list_one[row][j]

        print("After sort")
        print_table(sort_col(list_one))
