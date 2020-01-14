

def main():
    for i in range(int(input()), int(input()) + 1):
        j = int(i ** 0.5)

        if j ** 2 == i:
            print(i, end=' ')

    print()


if __name__ == '__main__':
    main()
