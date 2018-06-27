import string
array = [-1, 15, -5, 56, -1, 2, -2, 10]
# 1. Найти номер и значение первого положительного элемента списка.


def find_positive_numbers(arr):
    for i in range(len(arr)):
        if arr[i] >= 0:
            return i, arr[i]


# 2. Найти сумму положительных элементов списка.

def sum_of_positive_numbers(arr):
    new_sum = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            new_sum += arr[i]
    return new_sum

# 3. Дан список, содержащий положительные и отрицательные
# числа. Заменить все элементы списка на противоположные по
# знаку. Например, задан список [1, -5, 0, 3, -4]. После
# преобразования должно получиться [-1, 5, 0, -3, 4].


def change_the_sign(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] * (-1)
    return arr

# 4. В списке найти минимальный и максимальный элементы,
# поменять их местами.


def change_max_min(arr):
    new_min = min(arr)
    new_max = max(arr)
    for i in range(len(arr)):
        if arr[i] == min(arr):
            arr[i] = new_max
        elif arr[i] == max(arr):
            arr[i] = new_min
    return arr


# 5. Найти сумму и произведение элементов одномерного числового
# списка.


def sum_product_of_numbers(arr):
    a = sum(arr)
    product_of_numbers = 1
    for i in range(len(arr)):
        product_of_numbers *= arr[i]
    return a, product_of_numbers


# 6. Дан список чисел. Выведите все элементы списка, которые
# больше предыдущего элемента.


def bigger_then_previous(arr):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] > arr[i - 1]:
            new_arr.append(arr[i])
    return new_arr


# 7. Дан список чисел. Если в нем есть два соседних элемента
# одного знака, выведите эти числа. Если соседних элементов
# одного знака нет — не выводите ничего. Если таких пар соседей
# несколько — выведите первую пару.


def two_same_sign(arr):
    for i in range(1, len(arr)):
        if (arr[i] < 0 and arr[i-1] < 0) or (arr[i] > 0 and arr[i-1] > 0):
            return arr[i-1], arr[i]
        else:
            return 'no such elements'


# 8. Дан список чисел. Определите, сколько в этом списке
# элементов, которые больше двух своих соседей, и выведите
# количество таких элементов. Крайние элементы списка никогда не
# учитываются, поскольку у них недостаточно соседей.


def bigger_than_neighbors(arr):
    counter = 0
    elements = []
    for i in range(1, len(arr)-1):
        if arr[i-1] < arr[i] > arr[i+1]:
            counter += 1
            elements.append(arr[i])
    if counter == 0:
        return 'no such elements'
    else:
        return counter, elements


# 9. Из одномерного списка удалить все повторяющиеся элементы
# (дубликаты) так, чтобы каждое значение встречалось в списке
# только один раз.

def delete_same_elements(arr):
    new_arr = []
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr


# 10. В одномерном списке удалить все четные элементы и оставить
# только нечетные.


def remove_even(arr):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            new_arr.append(arr[i])
    return new_arr


# 11. Дан список значений. Превратить список в словарь где
# ключами служат элементы списка, а значениями квадраты этих
# элементов. [1,2,3] -> {1:1, 2:4, 3:9}


def list_to_dict_square(arr):
    new_dict = {}
    for i in arr:
        new_dict[i] = i ** 2
    return new_dict


# 12. Дан список значений. Превратить список в словарь
# поочередно превращая елменты в ключи и значения. [1, 2, 3, 4, 5, 6]
# -> {1: 2, 3: 4, 5: 6}


# def list_to_dict(arr):
#     new_dict = {}
#     for i in range(1, len(arr)-1):
#         new_dict[i] = arr[i + 1]
#     return new_dict


# 14. Программа конвертер валют (для валют: евро, доллар, гривна,
# рубль, фунт) должна переводить из любой валюты в любую. Курсы
# хардкодим.
# Пример:
# ——————————————
# Введите валюту:
# UAH
# Введите сумму:
# 2600
# В какой валюте получить результат?
# USD
# 2600 UAH = 100 USD
# ———————————————


def currency_converter():
    currency_dict = {'UAH': 1, 'USD': 26.02, 'EUR': 30.57, 'RUB': 0.4, 'GBR': 34}
    print('возможные валюты: UAH, USD, EUR, RUB, GBR')
    first_curency = input('Введите валюту: \n')
    money = input('Введите сумму:\n')
    needed_currency = input('В какой валюте получить результат?\n')
    out = currency_dict[first_curency] * int(money) / currency_dict[needed_currency]
    print(money, first_curency, '=', out, needed_currency)


# 15. Программа переводчик на соленый язык.
# # Правило: после каждой гласной вставляем с + сама гласная.
# # Привет -> Приcивеcет
# # Сальса -> саcальсаcа


def from_normal_to_c():
    word = 'fdgdfbberewferwf'
    vowels = 'eyuioa'
    arr = list(word)
    print(arr)
    for i in range(len(word)):
        if arr[i] in range(len(vowels)):
            arr.insert(i, arr['c' + arr[i]])


     # letter in vowels for letter in word:

    return arr


if __name__ == '__main__':
    # print(array)
    # print(list_to_dict(array))
    print(from_normal_to_c())
