

def main():
    a = int(input())

    for i in range(2, a + 1):
        if a % i == 0:
            print(i)

            break


if __name__ == '__main__':
    main()
