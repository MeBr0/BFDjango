def hello_name(name):
    return 'Hello %s!' % name


def make_abba(a, b):
    return '%s' * 4 % (a, b, b, a)


def make_tags(tag, word):
    return '<%s>%s</%s>' % (tag, word, tag)


def make_out_word(out, word):
    return '%s' * 3 % (out[:2], word, out[2:])


def extra_end(str):
    return '%s' % str[-2:] * 3


def first_two(str):
    return str[:2]


def first_half(str):
    return str[:len(str) / 2]


def without_end(str):
    return str[1:-1]


def combo_string(a, b):
    return '%s' * 3 % ([el for el in (a, b) if len(el) == min(len(a), len(b))][0], \
                       [el for el in (a, b) if len(el) == max(len(a), len(b))][0], \
                       [el for el in (a, b) if len(el) == min(len(a), len(b))][0])


def non_start(a, b):
    return '%s' * 2 % (a[1:], b[1:])


def left2(str):
    return '%s' * 2 % (str[2:], str[:2])
