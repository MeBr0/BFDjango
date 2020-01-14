

def main():
    a, j = int(input()), 1

    while j < int(a ** 0.5) + 1:
        print(j ** 2)

        j += 1


if __name__ == '__main__':
    main()
