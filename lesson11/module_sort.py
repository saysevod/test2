"""
Module has two functions of sort
"""
def bubble(list_one: list) -> list:
    """
    :param list_one: list of numbers
    :return: list is sorted acs
    """
    for i in range(len(list_one) - 1, 0, -1):
        for j in range(0, i):
            if list_one[j] > list_one[i]:
                list_one[j], list_one[j + 1] = list_one[j + 1], list_one[j]

    return list_one


def prepare(numbers: list, low: int, high: int) -> int:
    pivot = numbers[high]
    item = low - 1

    for i in range(low, high):
        if numbers[i] <= pivot:
            item = item + 1
            (numbers[item], numbers[i]) = (numbers[i], numbers[item])

    (numbers[item + 1], numbers[high]) = (numbers[high], numbers[item + 1])

    return item + 1


def quick_sort(numbers: list, low: int, high: int) ->None:
    """
    :param numbers: list of numbers
    :param low: start index list
    :param high: end index list
    :return: None
    function is sorted list by asc
    """
    if low < high:
        pivot = prepare(numbers, low, high)

        quick_sort(numbers, low, pivot - 1)

        quick_sort(numbers, pivot + 1, high)


__all__ = ['bubble', 'quick_sort']
if __name__ == '__main__':
    pass
