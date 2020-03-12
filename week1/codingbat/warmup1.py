def sleep_in(weekday, vacation):
    return not weekday or vacation


def diff21(n):
    if n > 21:
        return 2 * (n - 21)

    return 21 - n


def near_hundred(n):
    return n in range(90, 111) or n in range(190, 211)


def missing_char(str, n):
    return str[:n] + str[n + 1:]


def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile


def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)


def pos_neg(a, b, negative):
    return (((a > 0 and b < 0) or (a < 0 and b > 0)) and not negative) or (a < 0 and b < 0 and negative)


def front_back(str):
    size = len(str)

    if size == 1 or size == 0:
        return str

    if size == 2:
        return str[::-1]

    return str[-1] + str[1:-1] + str[0]


def sum_double(a, b):
    if a == b:
        return a * 4

    return a + b


def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10


def not_string(str):
    if str[:3] == 'not':
        return str

    return 'not ' + str


def front3(str):
    if len(str) < 3:
        return str * 3

    return str[:3] * 3
