def selection_sort(list):
    '''Сортировка списка выбором без отдельной функции нахождения минимального элемента'''
    for i in range(0,len(list)-1):
        min = i
        for n in range(i, len(list)):
            if list[n] < list[min]:
                min = n
        list[i], list[min] = list[min], list[i]

list = [2,5,3,1,4]
selection_sort(list)
print(list)

