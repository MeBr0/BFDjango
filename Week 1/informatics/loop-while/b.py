

def main():
    a, j = int(input()), 2

    while j < a + 1:
        if a % j == 0:
            print(j)

            break

        j += 1


if __name__ == '__main__':
    main()
