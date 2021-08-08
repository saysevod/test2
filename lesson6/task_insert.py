import random

SIZE = 10
MAX = 1000


def main():
    list_one = random.sample(range(MAX), k=SIZE)
    user_index, user_value = input(
        f'Input index for list from 0 to {SIZE - 1} and your value, please(ex. {random.randrange(SIZE)} {random.randrange(MAX)} ): ').split()
    # TODO user_index, user_value to validate the fill
    print(f'Random list:\n{list_one}')
    list_one.append(int(user_value))
    for i in range(SIZE, int(user_index), -1):
        list_one[i - 1], list_one[i] = list_one[i], list_one[i - 1]
    print(f'List after shift:\n{list_one}')


if __name__ == '__main__':
    main()
