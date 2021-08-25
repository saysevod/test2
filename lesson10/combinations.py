res = 0
k = False


def without_00(a, b):
    '''
    :param a: count of zero
    :param b: count of one
    :return:
    '''
    global res
    global k  # if previous digit is zero
    if a != 0 or b != 0:
        if a > 0 and b > 0:
            if k:
                k = False
            else:
                k = True
                without_00(a - 1, b)
            k = False
            without_00(a, b - 1)
        if a > 0 and b == 0:
            if not k:
                k = True
                without_00(a - 1, b)
        if b > 0 and a == 0:
            without_00(a, b - 1)
    else:
        res += 1
    return res


if __name__ == '__main__':
    a = int(input('Input number of zero, please: '))
    b = int(input('Input number of one, please: '))

    print(without_00(a, b))
