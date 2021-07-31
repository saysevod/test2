def main():
    year = input('Input the year from 1900 to 1000000: ')
    if year.isdigit() and \
            int(year) > 1900 and \
            int(year) < 1000000:
        if int(year) % 4 == 0:
            if int(year) % 100 == 0 and int(year) % 400 != 0:
                print('{} is not leap'.format(year))
            else:
                print('{} is leap'.format(year))
        else:
            print('{} is not leap'.format(year))
    else:
        print('{} is not valid'.format(year))

 # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

