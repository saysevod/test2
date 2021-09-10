class Count:
    """"
    Digital count
    """
    min = 0
    max = 100
    cur = 0

    def __init__(self, min, max):
        """

        :param min:
        :param max:
        """
        self.min = min
        self.max = max
        self.cur = min
    def get_cur(self):
        """

        :return:
        """
        return self.cur

    def incr(self):
        """

        :return:
        """

        self.cur = self.cur + 1 if self.cur < self.max else self.cur
        return self.cur


if __name__ == '__main__':
    a = Count(100,102)
    print(a.incr())
    print(a.incr())
    print(a.get_cur())
    print(a.incr())
    print(a.incr())