def main():
    list_one = input("Input string, please: ").split()
    # TODO list_one to validate of fill
    dict_text = dict.fromkeys(list_one, 0)
    for i in list_one:
        dict_text.update({i: dict_text.get(i)+1})
    print(f'{dict_text}')


if __name__ == '__main__':
    main()
