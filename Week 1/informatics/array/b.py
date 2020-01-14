

def main():
    x = int(input())

    arr = [int(a) for a in input().split()]

    print(' '.join([str(x) for x in arr if x % 2 == 0]))


if __name__ == '__main__':
    main()
