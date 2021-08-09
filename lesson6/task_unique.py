def main():
    list_first = input(f'Input first list, please(ex. 2 34 5 6): ').split()
    list_second = input(f'Input second list, please(ex. 0 5 5 12): ').split()
    # TODO list_first, list_second validate to fill
    print(
        f'List of unique value from lists {len([x for x in list_first + list_second if (list_first + list_second).count(x) == 1])}')


if __name__ == '__main__':
    main()
