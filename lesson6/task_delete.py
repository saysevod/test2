import random

SIZE = 10


def main():
    list_one = random.sample(range(1000), k=SIZE)
    user_index = int(input(f'Input index for list from 0 to {SIZE-2}, please: '))
    #TODO user_index to validate the fill
    print(f'Random list:\n{list_one}')
    for i in range(user_index,SIZE):
        list_one[i-1],list_one[i] = list_one[i],list_one[i-1]
    list_one.pop()
    print(f'List after shift:\n{list_one}')

if __name__ == '__main__':
    main()
