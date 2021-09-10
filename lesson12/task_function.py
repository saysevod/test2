def fun_summ():
    try:
        x, y = input('Input two numbers, please: ')
    except ValueError as e:
        print(e)
    print(x, y)


if __name__ == '__main__':
    fun_summ()
