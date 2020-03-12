

def main():
    x = int(input())

    arr = [int(a) for a in input().split()]

    print(sum([1 for x in arr if x > 0]))


if __name__ == '__main__':
    main()
