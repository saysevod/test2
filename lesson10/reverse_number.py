res = 0


def reverse_it(number):
    '''
    :param number:
    :return:
    '''
    global res
    if number > 0:
        res = res * 10 + number % 10
        reverse_it(number // 10)
    return res


if __name__ == '__main__':
    print(reverse_it(2178))
