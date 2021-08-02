def main():
    number = input('Input the number please: ')

    for i in range(1,int(number)+1):
        if str(i**2)[-len(str(i)):] == str(i):
            print(f'{i} * {i} = {i**2}')

if __name__ == '__main__':
    main()

