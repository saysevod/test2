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


def unique() -> None:
    """
    Print count of unique elements of list
    :return:
    """
    list_one = input("Input list of number, please: ").split()
    print('Count of unique number is  {}'.format(len(set(list_one))))


def print_table(lst: list) -> list:
    """
    :param lst: list of matrix number
    :return: list of sum col
    """

    for row in range(0, len(lst)):
        print(' '.join(["{:4d}".format(x) for x in lst[row]]))

    list_two = [sum([row[i] for row in lst]) for i in range(0, len(lst[0]))]
    print(' '.join(["{:4d}".format(x) for x in list_two]))
    return list_two


if __name__ == '__main__':
    pass
