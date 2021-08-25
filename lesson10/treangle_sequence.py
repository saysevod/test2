def count_first(nums, n):
    if n > 1:
        count_first(nums, n - 1)
    nums += n * str(n) if (len(nums) + n) <= max else (max - len(nums)) * str(n)
    return nums


if __name__ == '__main__':
    max = int(input('Input number, please: '))
    nums = []
    print(' '.join(count_first(nums, max)))
