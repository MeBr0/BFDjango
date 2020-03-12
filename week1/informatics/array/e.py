

def main():
    x = int(input())

    arr = [int(a) for a in input().split()]

    a = sum([1 for i in range(1, x) if arr[i] / abs(arr[i]) == arr[i - 1] / abs(arr[i - 1])])

    if a:
        print('YES')

    else:
        print('NO')


if __name__ == '__main__':
    main()
