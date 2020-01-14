

def main():
    a, j = int(input()), 1
    ans = False

    while j <= a:
        if j == a:
            ans = True

            break

        j *= 2

    if ans:
        print('YES')

    else:
        print('NO')


if __name__ == '__main__':
    main()
