import math

arey = ['', 'sss', '', 'ffff', '']
aaa = [1, 5, 2, 89, 3]
ssss = [{'id': 2, 'value': 25}, {'id':2, 'value': 0}, {'id': 2, 'value': 0}, {'id': 2, 'value': 456}]
wwww = [-12, 5, 2, -3]


def sort_int(arr):
    return sorted(arr)


def sort_string(arr):
    return list(filter(None, arr))


def filter_dict(arr):
    arrey = []
    for value in range(len(arr)):
        if arr[value]['value'] != 0:
            arrey.append(arr[value])
    return arrey


def sort_absolute(arr):
    a = math.copysign



# print(filter_dict(ssss))
# print(filter_1(arey))
print(sort_int(wwww))

