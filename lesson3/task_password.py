def main():
    secret_phrase='My password'
    your_phrase = input('Input secret phrase: ')
    if secret_phrase == your_phrase :
        print('Password passed')
    else:
        print('Password mismatched')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

