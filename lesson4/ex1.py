def create_arr():
    arr = []
    while True:
        integer = input('input value')
        arr.append(int(integer))
        a = input('input \'stop\' to stop input')
        if a.lower() == 'stop':
            break
    print(arr)
    return arr


def average(array):
    leng = len(array)
    sum1 = 0
    for i in array:
        sum1 += i
    return sum1/leng


def average2(array):
    return sum(array)/len(array)


numbers = [12, 125, -46545, 5498, 656, -10]


def f(n):

    for i in range(len(n)):
        if n[i] < 0:
            n[i] = 'меньше нуля'
        elif 0 < n[i] < 100:
            n[i] = 'меньше 100'
        else:
            n[i] = 'больше 100'
    return n


# print(f(numbers))


numbers1 = [12, 125, -46545, 5498, 656, -10]


def sort():
    li = [5,2,7,4,0,9,8,6]
    n = 1
    while n < len(li):
        for i in range(len(li)-n):
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]
        n += 1
    print(li)


li = [5, -2, -7, 4, -1, -9, 8, -6]


def sort2(arr):
    for i in range(len(arr)):  # range(len(arr), 0 , -1)
        if i == len(arr):
            break
        if arr[i] < 0:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
    return arr


print(sort2(li))