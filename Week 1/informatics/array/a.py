

def main():
    x = int(input())

    arr = [a for a in input().split()]

    print(' '.join(arr[::2]))


if __name__ == '__main__':
    main()
