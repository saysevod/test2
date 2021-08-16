def main(min, max):
    '''
    :param min:
    :param max:
    :return:
    '''

    def simple(number):
        '''
        Check if number is simple
        :param number:
        :return:
        '''
        res = True
        count = 1
        while res and count < number - 1:
            count += 1
            res = res if number % count != 0 else False
        return res

    print(' '.join([str(x) for x in range(min, max+1) if simple(x)]))


if __name__ == '__main__':
    min,max = input('Input two numbers, please: ').split()
    main(int(min), int(max))
