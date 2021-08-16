def main(sum_in, numbers):
    '''
    :param numbers:
    :param sum:
    :return:
    '''
    res = False
    while not res:
        if (sum_in - numbers.pop()) in numbers:
            res = True
    return res

if __name__ == '__main__':
    list_one = input('Input some numbers, please: ').split()
    list_one = list(map(int, list_one))
    sum_ext = int(input('Input any number, please: '))
    print(main(sum_ext, list_one))