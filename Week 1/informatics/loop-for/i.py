

def main():
    a = int(input())
    j = 0

    for i in range(1, int((a + 1) ** 0.5)):
        if a % i == 0:
            j += 1

    j *= 2

    if a % a ** 0.5 == 0:
        j += 1

    print(j)


if __name__ == '__main__':
    main()
