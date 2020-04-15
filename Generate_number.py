def gen_bin(M, prefix=''):
    '''Генерация чисел в двоичной системе счисления,
    M принимает количество цифр в двоичном числе, prefix переменная-строка, в которой генерируются числа'''
    if M == 0:
        print(prefix, end=' ')
        return
    for digit in '0', '1':
        gen_bin(M - 1, prefix + digit)


def generate_number(N: int, M: int, prefix=None):
    '''Генерация чисел в N-системе счисления,
    M принимает количество цифр в числе, prefix переменная-список, в которой генерируются числа'''
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M - 1, prefix)
        prefix.pop()


gen_bin(3)
generate_number(3, 3)
