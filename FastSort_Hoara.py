def fast_sort(list: list):  # Быстрая сортировка Хоара с использованием рекурсии
    '''Сортирует список с O(N*logN)'''
    if len(list) < 2:
        return list
    value = list[0]
    less = [i for i in list[1:] if i <= value]
    larger = [i for i in list[1:] if i > value]
    return fast_sort(less) + [value] + fast_sort(larger)


print(fast_sort([2, 5, 3, 7,1]))
