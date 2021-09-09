def fun_sum():
    """
    Function of summary two numbers or strings
    :return:
    """
    res = 0
    x = ''
    for i in [1, 2]:
        try:
            x = input('Input number, please: ')
            res += int(x)
        except (ValueError, TypeError):
            res = x if i == 1 else ''.join([str(res), x])  # remove 0 from res

    print(res)


if __name__ == '__main__':
    fun_sum()
