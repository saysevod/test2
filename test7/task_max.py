def main():
    list_one = input("Input string, please: ").split()
    # TODO list_one to validate of fill

    dict_text = dict.fromkeys(list_one, 0)
    for i in list_one:
        dict_text.update({i: dict_text.get(i)+1})

    max_count = (0,0)
    while bool(dict_text):
        last = dict_text.popitem()
        max_count = last if last[1] > max_count[1] else max_count

    print(f'"{max_count[0]}" is the most common word')


if __name__ == '__main__':
    main()
