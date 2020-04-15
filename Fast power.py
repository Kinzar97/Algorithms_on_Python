def pow(a: float, n: int):
    '''Рекурсивная функция для быстрого возведения в степень'''
    if n == 0:
        return 1
    elif n % 2 == 1:  # n-нечетное
        return pow(a, n - 1) * a
    else:  # n-четное
        return pow(a ** 2, n // 2)


print(pow(4, 4))
