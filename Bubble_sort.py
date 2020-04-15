def bubble_sort(list):
    '''Сортировка пузырьком'''
    n = len(list)
    for bypass in range(1, n):
        for k in range(0, n - bypass):
            if list[k] > list[k + 1]:
                list[k], list[k + 1] = list[k + 1], list[k]


list = [3, 2, 6, 4, 1]
bubble_sort(list)
print(list)
