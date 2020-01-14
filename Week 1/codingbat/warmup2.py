def string_times(str, n):
    return str * n


def front_times(str, n):
    if len(str) < 3:
        return str * n

    return str[:3] * n


def string_bits(str):
    return str[::2]


def string_splosion(str):
    return ''.join([str[:i + 1] for i in range(len(str))])


def last2(str):
    return sum([1 for i in range(len(str) - 2) if str[i:i + 2] == str[-2:]])


def array_count9(nums):
    return sum([1 for num in nums if num == 9])


def array_front9(nums):
    return 9 in nums[:4]


def array123(nums):
    return (1, 2, 3) in zip(nums, nums[1:], nums[2:])


def string_match(a, b):
    return sum([1 for i in range(min(len(a), len(b)) - 1) if a[i:i + 2] == b[i:i + 2]])
