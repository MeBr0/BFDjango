

def main():
    x = int(input())

    arr = [int(a) for a in input().split()]

    print(sum([1 for i in range(1, x - 1) if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]]))


if __name__ == '__main__':
    main()
