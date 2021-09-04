class MyExc(Exception):
    def __init__(self, value):
        self.msg = value

    def __str__(self):
        return self.msg


if __name__ == '__main__':
    try:
        raise MyExc("My exception")
    except MyExc as e:
        print(e)
