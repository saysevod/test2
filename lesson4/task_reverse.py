def main():
    first, second = [ x for x in input('Input two word, please: ').split()]
    print('{} {}'.format(second[::-1].title(),first[::-1].title()))

if __name__ == '__main__':
    main()

