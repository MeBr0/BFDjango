def powi(x, r):
    j = 0
    res = 1

    if r == 0 and x != 0:
        return 1

    while j != r:
        res *= x

        j += 1

    return res


def main():
    nums = [float(x) for x in input().split()]

    print(powi(nums[0], nums[1]))


if __name__ == '__main__':
    main()
