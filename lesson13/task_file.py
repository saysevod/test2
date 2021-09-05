if __name__ == '__main__':
    with open('user_file.txt', 'w') as f:
        text = input('Input text, please: ')
        while text != '':
            f.write(''.join([text, '\n']))
            text = input('Input text, please: ')

    with open('user_file.txt', 'r') as f:
        print(f.read())
