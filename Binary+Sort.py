from random import randrange


def find_Smallest(arr):  # Нахождение индекса наименьшего значения в списке
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):  # Создание нового отсортированного по возрастанию списка
    newArr = []
    for i in range(len(arr)):
        smallest = find_Smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


def binary_search(list, item):  # Реализация бинарного поиска
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return guess
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def check_elements(list, item):  # Функция проверяет, есть ли в рандомном неупорядоченном списке элемент пользователя
    n = selectionSort(list)
    index_number = binary_search(n, item)
    if type(index_number) == int:
        return 'True'
    else:
        return 'False'


list = [randrange(170) for i in range(40)]
print(list)

item = int(input('Enter any number to check: '))
print(check_elements(list, item))

