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

    def gen(min,max):
        i = min
        while i <= max:
            if simple(i):
                yield i
            i += 1

    print(' '.join(str(i) for i in gen(min, max)))

if __name__ == '__main__':
    min,max = input('Input two numbers, please: ').split()
    main(int(min), int(max))
