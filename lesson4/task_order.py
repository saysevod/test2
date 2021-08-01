def main():
    s = input('Input number, please: ')

    i=0
    Answer='Yes'
    whie i < len(s)-1 :
        if i*2 in s:
            break
    else:
        Answer='No'

if __name__ == '__main__':
    main()

