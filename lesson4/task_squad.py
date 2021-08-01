def main():
    number = input('Input the number please: ')

    for i in range(1,int(number)+1):
        if str(i**2)[-len(str(i)):] == str(i):
            print('{}'.format(i))

if __name__ == '__main__':
    main()

