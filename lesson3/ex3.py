def input_value():
    a = int(input('input first value \n > '))
    b = int(input('input second value \n > '))
    c = int(input('input third value \n > '))
    return [a, b, c]


def find_max(value):
    maxvalue = value[0]
    for i in value:
        if i > maxvalue:
            maxvalue = i
    return maxvalue


def find_min(value):
    minvalue = find_max(value)
    for i in value:
        if i < minvalue:
            minvalue = i
    return minvalue


# a = input_value()
#
# print('min_value = ', find_min(a))
# print('max_value = ', find_max(a))


def custom_len(value):
    leng = 0
    for i in value:
        leng += 1
    return leng


# g = 'hello'
#
# print(custom_len(g))


def is_prime(value):

    if value % 2:
        return True
    else:
        return False


print(is_prime(3))
print(is_prime(4))

