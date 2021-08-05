MIN = 3
MAX = 9


def main():
    number = int(input(f'Input digit from  {MIN} to {MAX}, please: '))
    if number in range(MIN, MAX + 1):
        for i in range(1, number + 1):
            str_row = ''.join(list(map(str, range(1, i+1))))
            str_row += ''.join(list(map(str, range(i-1, 0, -1))))
            print(str_row)
    else:
        print(f'{number} not in range {MIN}..{MAX}')


if __name__ == '__main__':
    main()
