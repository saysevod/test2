def main():
    number = input('Input the number please: ')

    i = 0
    Answer = 'Yes'
    while i < len(number)-1 :
        if number.count(str(i)) > 1:
            break
        i += 1
    else:
        Answer = 'No'

    print('{}'.format(Answer))

if __name__ == '__main__':
    main()

