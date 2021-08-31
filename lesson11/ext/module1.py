__all__ = ['reverse_it', 'unique', 'print_table']
res = 0


def reverse_it(number: int) -> int:
    """
    Reverse number
    :param number: number to reverse
    :return: reverse number
    """
    global res
    if number > 0:
        res = res * 10 + number % 10
        reverse_it(number // 10)
    return res


def unique() ->None:
    """
    Print count of unique elements of list
    :return:
    """
    list_one = input("Input list of number, please: ").split()
    print('Count of unique number is  {}'.format(len(set(list_one))))



def print_table(list_one: list) -> list:
    """
    :param list_one: list of matrix number
    :return: list of sum col
    """

    for row in range(0, len(list_one)):
        print(' '.join(["{:4d}".format(x) for x in list_one[row]]))

    list_two = [sum([row[i] for row in list_one]) for i in range(0, len(list_one[0]))]
    print(' '.join(["{:4d}".format(x) for x in list_two]))
    return list_two


if __name__ == '__main__':
    pass
