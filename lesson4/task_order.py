def main():
    s = input('Input number, please: ')

    i=0
    Answer='Yes'
    while i < len(s)-1 :
        if s[i]*2 in s:
            break
        i += 1
    else:
        Answer='No'
    print(Answer)

if __name__ == '__main__':
    main()

