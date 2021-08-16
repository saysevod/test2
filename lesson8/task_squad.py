def main(list_one):
    DEF_CONST=5
    f = lambda x, y=DEF_CONST: x ** y
    list_two=list(map(f,list_one))
    print(list_two)

if __name__ == '__main__':
    list_one = input('Input list of numbers, please: ').split()
    list_one = list(map(int, list_one))
    main(list_one)