X = 109


def main():
    a, b = int(input()), int(input())

    a = (a + X) % X

    print((a * b) % X)


if __name__ == '__main__':
    main()
