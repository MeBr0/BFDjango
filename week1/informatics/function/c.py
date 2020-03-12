def xori(x, y):
    if x == y:
        return 0

    return 1


def main():
    nums = [float(x) for x in input().split()]

    print(xori(nums[0], nums[1]))


if __name__ == '__main__':
    main()
