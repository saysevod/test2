def main():
    list_one = input("Input first list of number, please: ").split()
    list_two = input("Input second list of number, please: ").split()
    # TODO list_one, list_two to validate of fill
    print(f'Count of unique number in both lists is  {len(set(list_one).intersection(set(list_two)))}')


if __name__ == '__main__':
    main()