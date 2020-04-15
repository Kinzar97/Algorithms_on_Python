def find_number(number, A):
    '''Поиск number в A'''
    for x in A:
        if number == x:
            return True
    return False

def number_permutations(N: int, M: int = -1, prefix=None):
    '''Генерация всех перестановок N чисел в M позициях,
    с префиксом prefix'''
    M = N if M == -1 else M  # по умолчанию M чисел в N позициях, если захотим поменять кол-во позиций, тогда M = M
    prefix = prefix or []
    if M == 0:
        print(*prefix, sep = '', end = ', ')
        return
    for number in range(1, N+1):
        if find_number(number, prefix):
            continue
        prefix.append(number)
        number_permutations(N, M - 1, prefix)
        prefix.pop()

number_permutations(3)