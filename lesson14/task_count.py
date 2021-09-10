class Count:
    """"
    Digital count
    """
    cur = 0

    def __init__(self, _min=0, _max=100):
        """
        Init min, max and current variable
        :param min:
        :param max:
        """
        self._min = _min
        self._max = _max
        self.cur = _min

    def get_cur(self):
        """
        Get current count
        :return:
        """
        return self.cur

    def incr(self):
        """
        Increment count
        :return:
        """
        self.cur = self.cur + 1 if self.cur < self._max else self.cur
        return self.cur


if __name__ == '__main__':
    a = Count(100, 103)
    a._max = 104
    print(a.incr())
    print(a.incr())
    print("Current {}".format(a.get_cur()))
    print(a.incr())
    print(a.incr())
