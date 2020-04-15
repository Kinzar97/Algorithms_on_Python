def gcd1(a, b):
    '''Алгоритм Евклида вычитанием с помощью рекурсии'''
    if a == b:
        return a
    elif a > b:
        return gcd1(a - b, b)
    else:  # b<a
        return gcd1(a, b - a)


def gcd2(a, b):
    '''Алгоритм Евклида делением с помощью рекурсии'''
    if b == 0:
        return a
    else:
        return gcd2(b, a % b)


print(gcd1(100, 40))
print(gcd2(100, 40))
